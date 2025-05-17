document.addEventListener('DOMContentLoaded', function() {
    // Real-time session updates
    const eventSource = new EventSource('/client/sessions/stream');
    
    eventSource.onmessage = function(e) {
        const data = JSON.parse(e.data);
        updateSessionTable(data);
        updateStats(data);
    };

    function updateSessionTable(session) {
        const table = document.querySelector('table');
        const newRow = table.insertRow(1);
        
        newRow.innerHTML = `
            <td>${session.mac_address}</td>
            <td>${session.internal_ip}</td>
            <td>${new Date(session.start_time).toLocaleString()}</td>
            <td>${(session.data_used / 1024 / 1024).toFixed(2)} MB</td>
        `;
    }

    function updateStats(session) {
        document.querySelector('#total-sessions').textContent = 
            parseInt(document.querySelector('#total-sessions').textContent) + 1;
        
        if(!session.end_time) {
            document.querySelector('#active-sessions').textContent = 
                parseInt(document.querySelector('#active-sessions').textContent) + 1;
        }
    }

    // Chart initialization
    const ctx = document.getElementById('trafficChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
            datasets: [{
                label: 'Использование трафика (MB)',
                data: [],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});