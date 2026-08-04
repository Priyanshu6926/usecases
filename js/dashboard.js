/**
 * Dashboard Script
 * Manages the interactive SVG map and Chart.js forecast panels.
 */

// Region configuration database
const regionDatabase = {
  northwest: {
    name: 'Northwest India',
    status: 'Extreme Alert',
    badgeClass: 'badge-extreme',
    temp: '44.5°C',
    anomaly: '+5.2°C',
    confidence: '94.6%',
    hotspots: 'Jaipur, Jodhpur, Bikaner',
    forecast: [42.1, 43.5, 44.5, 44.2, 45.0, 44.8, 43.9]
  },
  north: {
    name: 'North India',
    status: 'Extreme Alert',
    badgeClass: 'badge-extreme',
    temp: '43.8°C',
    anomaly: '+4.8°C',
    confidence: '91.2%',
    hotspots: 'Delhi NCR, Lucknow, Chandigarh',
    forecast: [41.2, 42.6, 43.8, 43.5, 44.1, 43.9, 43.0]
  },
  west: {
    name: 'West India',
    status: 'Severe Heat',
    badgeClass: 'badge-high',
    temp: '41.5°C',
    anomaly: '+3.5°C',
    confidence: '89.4%',
    hotspots: 'Ahmedabad, Nagpur, Pune',
    forecast: [39.8, 40.5, 41.5, 42.0, 41.2, 40.8, 41.0]
  },
  central: {
    name: 'Central India',
    status: 'Severe Heat',
    badgeClass: 'badge-high',
    temp: '42.2°C',
    anomaly: '+4.1°C',
    confidence: '90.5%',
    hotspots: 'Bhopal, Raipur, Jhansi',
    forecast: [40.5, 41.2, 42.2, 42.8, 42.5, 41.9, 41.4]
  },
  east: {
    name: 'East India',
    status: 'Mild Heat',
    badgeClass: 'badge-low',
    temp: '39.2°C',
    anomaly: '+2.1°C',
    confidence: '87.0%',
    hotspots: 'Kolkata, Patna, Ranchi',
    forecast: [38.2, 38.9, 39.2, 39.5, 38.8, 38.5, 39.0]
  },
  northeast: {
    name: 'Northeast India',
    status: 'Normal Risk',
    badgeClass: 'badge-normal',
    temp: '34.5°C',
    anomaly: '+0.5°C',
    confidence: '85.3%',
    hotspots: 'Guwahati, Shillong, Imphal',
    forecast: [33.8, 34.2, 34.5, 34.1, 33.9, 34.4, 34.6]
  },
  south: {
    name: 'South India',
    status: 'Mild Heat',
    badgeClass: 'badge-low',
    temp: '38.8°C',
    anomaly: '+1.8°C',
    confidence: '88.7%',
    hotspots: 'Hyderabad, Bengaluru, Chennai',
    forecast: [37.5, 38.2, 38.8, 39.0, 38.5, 38.0, 38.3]
  }
};

let projectionChart = null;
let historicalChart = null;

document.addEventListener('DOMContentLoaded', () => {
  initCharts();
  initMapInteractions();
});

/**
 * Initializes the Chart.js visualisations.
 */
function initCharts() {
  // Chart 1: 7-Day Temp Projections
  const ctxProj = document.getElementById('tempProjectionChart').getContext('2d');
  projectionChart = new Chart(ctxProj, {
    type: 'line',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [{
        label: 'Max Forecasted Temperature (°C)',
        data: regionDatabase.northwest.forecast,
        borderColor: '#f97316',
        backgroundColor: 'rgba(249, 115, 22, 0.15)',
        borderWidth: 3,
        fill: true,
        tension: 0.4,
        pointBackgroundColor: '#ffffff',
        pointBorderColor: '#f97316',
        pointHoverRadius: 7,
        pointRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } },
          min: 30,
          max: 48
        },
        x: {
          grid: { display: false },
          ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } }
        }
      }
    }
  });

  // Chart 2: Historic Heatwave Days
  const ctxHist = document.getElementById('heatwaveDaysChart').getContext('2d');
  historicalChart = new Chart(ctxHist, {
    type: 'bar',
    data: {
      labels: ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'],
      datasets: [{
        label: 'Days Per Year',
        data: [12, 15, 14, 18, 11, 19, 24, 28, 27, 31],
        backgroundColor: 'rgba(239, 68, 68, 0.65)',
        borderColor: '#ef4444',
        borderWidth: 1.5,
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } }
        },
        x: {
          grid: { display: false },
          ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } }
        }
      }
    }
  });
}

/**
 * Adds event listeners to SVG map paths for regional filtering.
 */
function initMapInteractions() {
  const mapPaths = document.querySelectorAll('.map-region-path');
  
  // Set northwest as active initially
  const initialPath = document.querySelector('.map-region-path[data-region="northwest"]');
  if (initialPath) initialPath.classList.add('active-selected');

  mapPaths.forEach(path => {
    path.addEventListener('click', () => {
      // Remove active class from all
      mapPaths.forEach(p => p.classList.remove('active-selected'));
      
      // Add active class to clicked path
      path.classList.add('active-selected');
      
      // Update details card
      const regionKey = path.getAttribute('data-region');
      updateRegionDisplay(regionKey);
    });
  });
}

/**
 * Updates the UI details panel and charts based on selected region.
 */
function updateRegionDisplay(regionKey) {
  const data = regionDatabase[regionKey];
  if (!data) return;

  // Elements
  const nameEl = document.getElementById('selected-region-name');
  const statusEl = document.getElementById('selected-region-status');
  const tempEl = document.getElementById('selected-region-temp');
  const anomalyEl = document.getElementById('selected-region-anomaly');
  const confidenceEl = document.getElementById('selected-region-confidence');
  const hotspotsEl = document.getElementById('selected-region-hotspots');

  // Update text
  nameEl.textContent = data.name;
  statusEl.textContent = data.status;
  tempEl.textContent = data.temp;
  anomalyEl.textContent = data.anomaly;
  confidenceEl.textContent = data.confidence;
  hotspotsEl.textContent = data.hotspots;

  // Reset status badges
  statusEl.className = 'region-detail-badge ' + data.badgeClass;

  // Update advisory button link URL params
  const advisoryBtn = document.getElementById('region-advisory-btn');
  if (advisoryBtn) {
    let severityParam = 'extreme';
    if (data.status === 'Severe Heat') severityParam = 'severe';
    else if (data.status === 'Mild Heat') severityParam = 'mild';
    else if (data.status === 'Normal Risk') severityParam = 'mild';
    
    advisoryBtn.href = `advisories.html?region=${regionKey}&severity=${severityParam}`;
  }

  // Update chart data
  if (projectionChart) {
    projectionChart.data.datasets[0].data = data.forecast;
    
    // Dynamically change chart border color based on severity
    if (data.status === 'Extreme Alert') {
      projectionChart.data.datasets[0].borderColor = '#ef4444';
      projectionChart.data.datasets[0].backgroundColor = 'rgba(239, 68, 68, 0.15)';
    } else if (data.status === 'Severe Heat') {
      projectionChart.data.datasets[0].borderColor = '#f97316';
      projectionChart.data.datasets[0].backgroundColor = 'rgba(249, 115, 22, 0.15)';
    } else if (data.status === 'Mild Heat') {
      projectionChart.data.datasets[0].borderColor = '#f59e0b';
      projectionChart.data.datasets[0].backgroundColor = 'rgba(245, 158, 11, 0.15)';
    } else {
      projectionChart.data.datasets[0].borderColor = '#10b981';
      projectionChart.data.datasets[0].backgroundColor = 'rgba(16, 185, 129, 0.15)';
    }
    
    projectionChart.update();
  }
}
