
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('schedule-form');
    const resultsDiv = document.getElementById('results');
    const resourceChartCtx = document.getElementById('resourceChart').getContext('2d');

    let resourceChart;  // Will hold the chart instance

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/schedule', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Clear previous results
            resultsDiv.innerHTML = '';
            
            // Show the scheduling results in text
            if (data.results) {
                data.results.forEach(result => {
                    const p = document.createElement('p');
                    p.textContent = result;
                    resultsDiv.appendChild(p);
                });
            }

            // Plot the resource distribution in a graph
            if (data.distribution) {
                const labels = data.distribution.map((_, index) => `Job ${index + 1}`);
                const distributionData = data.distribution;

                // If a chart already exists, destroy it before creating a new one
                if (resourceChart) {
                    resourceChart.destroy();
                }

                resourceChart = new Chart(resourceChartCtx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Resource Assigned',
                            data: distributionData,
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
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
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

/*
document.getElementById('scheduler-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    fetch('/schedule', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
        createChart(data);
    })
    .catch(error => console.error('Error:', error));
});

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results
    
    data.results.forEach(result => {
        const p = document.createElement('p');
        p.textContent = result;
        resultsDiv.appendChild(p);
    });
    
    const stepsDiv = document.getElementById('steps');
    stepsDiv.innerHTML = '<h2>Steps:</h2>';
    
    data.steps.forEach(step => {
        const stepP = document.createElement('p');
        stepP.textContent = step;
        stepsDiv.appendChild(stepP);
    });
}

function createChart(data) {
    const ctx = document.getElementById('resultsChart').getContext('2d');
    const chartData = {
        labels: data.labels,
        datasets: [{
            label: 'Job Distribution',
            data: data.chartData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };
    
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
*/
