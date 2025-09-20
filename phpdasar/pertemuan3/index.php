<?php
// PENGULANGAN
// For
// for ($i=0; $i<10; $i ++) {
//     echo "woi php, <br>";
// }

// While
// selagi kondisi nya true lakukan apa aja yang ada didalam kode itu
// $a=0;
// while ($a <= 10) {
//     echo "woi h <br>";
//     $a++;
// }

// Do.. While
// dia bakal melakukan sesuatu selagi kondisinya true
// kalau di operasi whilenya false, dia akan run sekali aja
$a = 0;
$b=1;
do {
    echo "perulangan ke-$b <br>";
    $a++;
    $b++;
} while ($a < 10);
?>
