const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar', // Tipe grafik: bar, line, pie, dll.
    data: {
        labels: ['Sektor Transportasi', 'Sektor Perdagangan', 'Sektor Industri', 'Sektor Pariwisata', 'Sektor Pertanian'],
        datasets: [{
            label: 'Kontribusi terhadap Perekonomian (%)',
            data: [25, 30, 20, 15, 10], // Data kontribusi
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(153, 102, 255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});