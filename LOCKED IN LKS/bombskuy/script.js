// Game Constants
const BOARD_COLS = 15;
const BOARD_ROWS = 10;
const CELL_SIZE = 50;
const GAME_WIDTH = BOARD_COLS * CELL_SIZE;
const GAME_HEIGHT = BOARD_ROWS * CELL_SIZE;

// Game Variables
let player = {
    x: 0,
    y: 0,
    lives: 3,
    bombRange: 1,
    isFrozen: false,
    activeItems: []
};
let dogs = [];
let bombs = [];
let explosions = [];
let items = [];
let gameTime = 0;
let timerInterval;
let gameStarted = false;
let gamePaused = false;
let difficulty = 'easy';
let wallsDestroyed = 0;
let tntCollected = 0;
let iceCubesCollected = 0;

// DOM Elements
const welcomeScreen = document.getElementById('welcome-screen');
const levelScreen = document.getElementById('level-screen');
const countdownScreen = document.getElementById('countdown-screen');
const gameScreen = document.getElementById('game-screen');
const gameoverScreen = document.getElementById('gameover-screen');
const leaderboardScreen = document.getElementById('leaderboard-screen');
const usernameInput = document.getElementById('username');
const playBtn = document.getElementById('play-btn');
const instructionBtn = document.getElementById('instruction-btn');
const instructionPopup = document.getElementById('instruction-popup');
const closeInstructionBtn = document.querySelector('.close-btn');
const pausePopup = document.getElementById('pause-popup');
const continueBtn = document.getElementById('continue-btn');
const saveScoreBtn = document.getElementById('save-score-btn');
const leaderboardBtn = document.getElementById('leaderboard-btn');
const backBtn = document.getElementById('back-btn');
const gameBoard = document.getElementById('game-board');
const countdownElement = document.getElementById('countdown');

// Event Listeners
usernameInput.addEventListener('input', togglePlayButton);
playBtn.addEventListener('click', showLevelScreen);
instructionBtn.addEventListener('click', showInstructions);
closeInstructionBtn.addEventListener('click', hideInstructions);
continueBtn.addEventListener('click', togglePause);
saveScoreBtn.addEventListener('click', saveScore);
leaderboardBtn.addEventListener('click', showLeaderboard);
backBtn.addEventListener('click', hideLeaderboard);

document.querySelectorAll('.level-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        difficulty = this.dataset.level;
        startCountdown();
    });
});

// Keyboard Events
document.addEventListener('keydown', handleKeyDown);

// Initialize Game Board
function initializeGameBoard() {
    gameBoard.innerHTML = '';
    gameBoard.style.width = `${GAME_WIDTH}px`;
    gameBoard.style.height = `${GAME_HEIGHT}px`;

    // Create cells
    for (let row = 0; row < BOARD_ROWS; row++) {
        for (let col = 0; col < BOARD_COLS; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.id = `cell-${col}-${row}`;
            cell.style.width = `${CELL_SIZE}px`;
            cell.style.height = `${CELL_SIZE}px`;
            gameBoard.appendChild(cell);
        }
    }

    // Place stone walls (fixed positions)
    placeStoneWalls();

    // Place brick walls (random positions)
    placeBrickWalls();

    // Place player
    placePlayer();

    // Place dogs based on difficulty
    placeDogs();
}

function placeStoneWalls() {
    // Fixed stone walls pattern (example pattern)
    const stoneWallPositions = [
        [2, 2], [2, 7], [7, 2], [7, 7], [12, 2], [12, 7],
        [4, 4], [4, 5], [10, 4], [10, 5]
    ];

    stoneWallPositions.forEach(pos => {
        const [col, row] = pos;
        const cell = document.getElementById(`cell-${col}-${row}`);
        cell.classList.add('stone-wall');
    });
}

function placeBrickWalls() {
    // Place brick walls randomly, avoiding player start position and stone walls
    for (let row = 0; row < BOARD_ROWS; row++) {
        for (let col = 0; col < BOARD_COLS; col++) {
            // Skip player start position (0,0)
            if (col === 0 && row === 0) continue;
            
            // Skip if it's a stone wall
            const cell = document.getElementById(`cell-${col}-${row}`);
            if (cell.classList.contains('stone-wall')) continue;
            
            // 30% chance to place a brick wall
            if (Math.random() < 0.3) {
                cell.classList.add('brick-wall');
            }
        }
    }
}

function placePlayer() {
    player = {
        x: 0,
        y: 0,
        lives: 3,
        bombRange: 1,
        isFrozen: false,
        activeItems: []
    };
    updatePlayerPosition();
}

function placeDogs() {
    dogs = [];
    const dogCount = difficulty === 'easy' ? 1 : difficulty === 'medium' ? 2 : 3;
    
    for (let i = 0; i < dogCount; i++) {
        let col, row;
        do {
            col = Math.floor(Math.random() * BOARD_COLS);
            row = Math.floor(Math.random() * BOARD_ROWS);
        } while (
            (col === 0 && row === 0) || // Don't place on player
            document.getElementById(`cell-${col}-${row}`).classList.contains('stone-wall') ||
            document.getElementById(`cell-${col}-${row}`).classList.contains('brick-wall')
        );
        
        dogs.push({ x: col, y: row });
        updateDogPosition(i);
    }
}

function updatePlayerPosition() {
    // Remove player class from all cells
    document.querySelectorAll('.cell').forEach(cell => {
        cell.classList.remove('player');
    });
    
    // Add player class to current position
    const playerCell = document.getElementById(`cell-${player.x}-${player.y}`);
    if (playerCell) {
        playerCell.classList.add('player');
    }
}

function updateDogPosition(index) {
    // Remove dog class from all cells
    document.querySelectorAll('.cell').forEach(cell => {
        cell.classList.remove(`dog-${index}`);
    });
    
    // Add dog class to current position
    const dog = dogs[index];
    const dogCell = document.getElementById(`cell-${dog.x}-${dog.y}`);
    if (dogCell) {
        dogCell.classList.add('dog');
        dogCell.classList.add(`dog-${index}`);
    }
}

function movePlayer(dx, dy) {
    if (player.isFrozen || gamePaused || !gameStarted) return;
    
    const newX = player.x + dx;
    const newY = player.y + dy;
    
    // Check boundaries
    if (newX < 0 || newX >= BOARD_COLS || newY < 0 || newY >= BOARD_ROWS) return;
    
    // Check for walls
    const targetCell = document.getElementById(`cell-${newX}-${newY}`);
    if (targetCell.classList.contains('stone-wall') || targetCell.classList.contains('brick-wall')) return;
    
    // Check for bombs
    if (bombs.some(bomb => bomb.x === newX && bomb.y === newY)) return;
    
    // Move player
    player.x = newX;
    player.y = newY;
    updatePlayerPosition();
    
    // Check for items
    checkForItems();
    
    // Check for dogs
    checkForDogs();
}

function placeBomb() {
    if (player.isFrozen || gamePaused || !gameStarted) return;
    
    // Check if there's already a bomb at player's position
    if (bombs.some(bomb => bomb.x === player.x && bomb.y === player.y)) return;
    
    // Place new bomb
    bombs.push({
        x: player.x,
        y: player.y,
        range: player.bombRange,
        timer: 5 // 5 seconds until explosion
    });
    
    // Update bomb display
    const bombCell = document.getElementById(`cell-${player.x}-${player.y}`);
    bombCell.classList.add('bomb');
    
    // Start bomb timer
    setTimeout(() => {
        explodeBomb(bombs.length - 1);
    }, 5000);
}

function explodeBomb(bombIndex) {
    const bomb = bombs[bombIndex];
    
    // Remove bomb from array
    bombs.splice(bombIndex, 1);
    
    // Remove bomb display
    const bombCell = document.getElementById(`cell-${bomb.x}-${bomb.y}`);
    bombCell.classList.remove('bomb');
    
    // Create explosion at bomb position
    createExplosion(bomb.x, bomb.y);
    
    // Create explosions in all 4 directions
    for (let direction of ['up', 'right', 'down', 'left']) {
        let dx = 0, dy = 0;
        if (direction === 'up') dy = -1;
        else if (direction === 'right') dx = 1;
        else if (direction === 'down') dy = 1;
        else if (direction === 'left') dx = -1;
        
        for (let i = 1; i <= bomb.range; i++) {
            const x = bomb.x + dx * i;
            const y = bomb.y + dy * i;
            
            // Stop if out of bounds
            if (x < 0 || x >= BOARD_COLS || y < 0 || y >= BOARD_ROWS) break;
            
            const cell = document.getElementById(`cell-${x}-${y}`);
            
            // Stop at stone walls
            if (cell.classList.contains('stone-wall')) break;
            
            // Destroy brick walls and stop
            if (cell.classList.contains('brick-wall')) {
                destroyWall(x, y);
                break;
            }
            
            // Create explosion
            createExplosion(x, y);
        }
    }
    
    // Check if player is hit by explosion
    checkExplosionDamage();
    
    // Check if dogs are hit by explosion
    checkDogDamage();
    
    // Remove explosions after 0.5 seconds
    setTimeout(() => {
        explosions.forEach(exp => {
            const cell = document.getElementById(`cell-${exp.x}-${exp.y}`);
            cell.classList.remove('explosion');
        });
        explosions = [];
    }, 500);
}

function createExplosion(x, y) {
    explosions.push({ x, y });
    const cell = document.getElementById(`cell-${x}-${y}`);
    cell.classList.add('explosion');
}

function destroyWall(x, y) {
    const cell = document.getElementById(`cell-${x}-${y}`);
    cell.classList.remove('brick-wall');
    wallsDestroyed++;
    document.getElementById('walls-destroyed').textContent = wallsDestroyed;
    
    // 30% chance to spawn an item
    if (Math.random() < 0.3) {
        spawnItem(x, y);
    }
}

function spawnItem(x, y) {
    const cell = document.getElementById(`cell-${x}-${y}`);
    const itemTypes = ['heart', 'tnt', 'ice'];
    const weights = [0.2, 0.4, 0.4]; // 20% heart, 40% tnt, 40% ice
    const random = Math.random();
    let itemType;
    
    if (random < weights[0]) itemType = 'heart';
    else if (random < weights[0] + weights[1]) itemType = 'tnt';
    else itemType = 'ice';
    
    items.push({ x, y, type: itemType });
    
    if (itemType === 'heart') cell.classList.add('heart-item');
    else if (itemType === 'tnt') cell.classList.add('tnt-item');
    else if (itemType === 'ice') cell.classList.add('ice-item');
}

function checkForItems() {
    const itemIndex = items.findIndex(item => item.x === player.x && item.y === player.y);
    if (itemIndex !== -1) {
        const item = items[itemIndex];
        const cell = document.getElementById(`cell-${item.x}-${item.y}`);
        
        // Remove item display
        cell.classList.remove('heart-item', 'tnt-item', 'ice-item');
        
        // Apply item effect
        if (item.type === 'heart') {
            player.lives--;
            document.getElementById('lives').textContent = player.lives;
            
            // Check for game over
            if (player.lives <= 0) {
                gameOver();
            }
        } else if (item.type === 'tnt') {
            player.bombRange++;
            tntCollected++;
            document.getElementById('tnt-collected').textContent = tntCollected;
            player.activeItems.push('tnt');
        } else if (item.type === 'ice') {
            iceCubesCollected++;
            document.getElementById('ice-cubes').textContent = iceCubesCollected;
            player.activeItems.push('ice');
            
            // Freeze player for 5 seconds
            player.isFrozen = true;
            setTimeout(() => {
                player.isFrozen = false;
                const index = player.activeItems.indexOf('ice');
                if (index !== -1) player.activeItems.splice(index, 1);
            }, 5000);
        }
        
        // Remove item from array
        items.splice(itemIndex, 1);
    }
}

function checkForDogs() {
    const dogIndex = dogs.findIndex(dog => dog.x === player.x && dog.y === player.y);
    if (dogIndex !== -1) {
        // Player touched a dog - lose a life
        player.lives--;
        document.getElementById('lives').textContent = player.lives;
        
        // Check for game over
        if (player.lives <= 0) {
            gameOver();
        }
    }
}

function checkExplosionDamage() {
    const playerHit = explosions.some(exp => exp.x === player.x && exp.y === player.y);
    if (playerHit) {
        player.lives--;
        document.getElementById('lives').textContent = player.lives;
        
        // Check for game over
        if (player.lives <= 0) {
            gameOver();
        }
    }
}

function checkDogDamage() {
    dogs.forEach((dog, index) => {
        const dogHit = explosions.some(exp => exp.x === dog.x && exp.y === dog.y);
        if (dogHit) {
            // Remove dog
            dogs.splice(index, 1);
            
            // Update display
            const cell = document.getElementById(`cell-${dog.x}-${dog.y}`);
            cell.classList.remove('dog');
            cell.classList.remove(`dog-${index}`);
        }
    });
}

function moveDogs() {
    if (gamePaused || !gameStarted) return;
    
    dogs.forEach((dog, index) => {
        // Simple AI: move randomly towards player
        const directions = [];
        
        if (dog.x < player.x) directions.push({ dx: 1, dy: 0 });
        if (dog.x > player.x) directions.push({ dx: -1, dy: 0 });
        if (dog.y < player.y) directions.push({ dx: 0, dy: 1 });
        if (dog.y > player.y) directions.push({ dx: 0, dy: -1 });
        
        // Also add some random directions
        directions.push(
            { dx: 1, dy: 0 },
            { dx: -1, dy: 0 },
            { dx: 0, dy: 1 },
            { dx: 0, dy: -1 }
        );
        
        // Try to move in a random valid direction
        const shuffledDirections = directions.sort(() => Math.random() - 0.5);
        
        for (const dir of shuffledDirections) {
            const newX = dog.x + dir.dx;
            const newY = dog.y + dir.dy;
            
            // Check boundaries
            if (newX < 0 || newX >= BOARD_COLS || newY < 0 || newY >= BOARD_ROWS) continue;
            
            // Check for walls
            const targetCell = document.getElementById(`cell-${newX}-${newY}`);
            if (targetCell.classList.contains('stone-wall') || targetCell.classList.contains('brick-wall')) continue;
            
            // Check for bombs
            if (bombs.some(bomb => bomb.x === newX && bomb.y === newY)) continue;
            
            // Check for other dogs
            if (dogs.some((d, i) => i !== index && d.x === newX && d.y === newY)) continue;
            
            // Move dog
            dog.x = newX;
            dog.y = newY;
            updateDogPosition(index);
            
            // Check if dog reached player
            if (dog.x === player.x && dog.y === player.y) {
                player.lives--;
                document.getElementById('lives').textContent = player.lives;
                
                // Check for game over
                if (player.lives <= 0) {
                    gameOver();
                }
            }
            
            break;
        }
    });
}

function updateTimer() {
    gameTime++;
    document.getElementById('timer').textContent = gameTime;
}

function gameOver() {
    gameStarted = false;
    clearInterval(timerInterval);
    
    // Show game over screen
    document.getElementById('gameover-name').textContent = usernameInput.value;
    document.getElementById('gameover-time').textContent = gameTime;
    document.getElementById('gameover-score').textContent = calculateScore();
    
    gameScreen.classList.add('hidden');
    gameoverScreen.classList.remove('hidden');
}

function calculateScore() {
    // Simple scoring formula
    return wallsDestroyed * 10 + tntCollected * 20 + iceCubesCollected * 15 + gameTime * 2;
}

function saveScore() {
    const playerData = {
        name: usernameInput.value,
        time: gameTime,
        score: calculateScore(),
        wallsDestroyed,
        tntCollected,
        iceCubesCollected,
        date: new Date().toISOString()
    };
    
    // Get existing scores from localStorage
    const scores = JSON.parse(localStorage.getItem('bombskuyScores')) || [];
    
    // Add new score
    scores.push(playerData);
    
    // Save back to localStorage
    localStorage.setItem('bombskuyScores', JSON.stringify(scores));
    
    alert('Score saved!');
}

function showLeaderboard() {
    gameoverScreen.classList.add('hidden');
    leaderboardScreen.classList.remove('hidden');
    
    // Get scores from localStorage
    const scores = JSON.parse(localStorage.getItem('bombskuyScores')) || [];
    
    // Sort by score (descending)
    scores.sort((a, b) => b.score - a.score);
    
    const leaderboardContainer = document.getElementById('leaderboard-container');
    leaderboardContainer.innerHTML = '';
    
    // Create header
    const header = document.createElement('div');
    header.className = 'leaderboard-item leaderboard-header';
    header.innerHTML = `
        <span>Rank</span>
        <span>Name</span>
        <span>Score</span>
        <span>Time</span>
        <span>Walls</span>
        <span>TNT</span>
        <span>Ice</span>
    `;
    leaderboardContainer.appendChild(header);
    
    // Add scores
    scores.slice(0, 10).forEach((score, index) => {
        const item = document.createElement('div');
        item.className = 'leaderboard-item';
        item.innerHTML = `
            <span>${index + 1}</span>
            <span>${score.name}</span>
            <span>${score.score}</span>
            <span>${score.time}s</span>
            <span>${score.wallsDestroyed}</span>
            <span>${score.tntCollected}</span>
            <span>${score.iceCubesCollected}</span>
        `;
        leaderboardContainer.appendChild(item);
    });
}

function hideLeaderboard() {
    leaderboardScreen.classList.add('hidden');
    gameoverScreen.classList.remove('hidden');
}

function togglePlayButton() {
    playBtn.disabled = usernameInput.value.trim() === '';
}

function showLevelScreen() {
    welcomeScreen.classList.add('hidden');
    levelScreen.classList.remove('hidden');
    document.getElementById('player-name-display').textContent = usernameInput.value;
}

function startCountdown() {
    levelScreen.classList.add('hidden');
    countdownScreen.classList.remove('hidden');
    
    let count = 3;
    countdownElement.textContent = count;
    
    const countdownInterval = setInterval(() => {
        count--;
        countdownElement.textContent = count;
        
        if (count <= 0) {
            clearInterval(countdownInterval);
            startGame();
        }
    }, 1000);
}

function startGame() {
    countdownScreen.classList.add('hidden');
    gameScreen.classList.remove('hidden');
    
    // Reset game state
    player.lives = 3;
    player.bombRange = 1;
    player.isFrozen = false;
    player.activeItems = [];
    gameTime = 0;
    wallsDestroyed = 0;
    tntCollected = 0;
    iceCubesCollected = 0;
    bombs = [];
    explosions = [];
    items = [];
    
    // Update UI
    document.getElementById('lives').textContent = player.lives;
    document.getElementById('timer').textContent = gameTime;
    document.getElementById('walls-destroyed').textContent = wallsDestroyed;
    document.getElementById('tnt-collected').textContent = tntCollected;
    document.getElementById('ice-cubes').textContent = iceCubesCollected;
    
    // Initialize game board
    initializeGameBoard();
    
    // Start game loop
    gameStarted = true;
    timerInterval = setInterval(updateTimer, 1000);
    
    // Start dog movement
    setInterval(moveDogs, 1000);
}

function showInstructions() {
    instructionPopup.classList.remove('hidden');
}

function hideInstructions() {
    instructionPopup.classList.add('hidden');
}

function togglePause() {
    gamePaused = !gamePaused;
    pausePopup.classList.toggle('hidden');
}

function handleKeyDown(e) {
    if (gamePaused || !gameStarted) {
        if (e.key === 'Escape') {
            togglePause();
        }
        return;
    }
    
    switch (e.key) {
        case 'ArrowLeft':
        case 'a':
        case 'A':
            movePlayer(-1, 0);
            break;
        case 'ArrowRight':
        case 'd':
        case 'D':
            movePlayer(1, 0);
            break;
        case 'ArrowUp':
        case 'w':
        case 'W':
            movePlayer(0, -1);
            break;
        case 'ArrowDown':
        case 's':
        case 'S':
            movePlayer(0, 1);
            break;
        case ' ':
            placeBomb();
            break;
        case 'Escape':
            togglePause();
            break;
    }
}