/**
 * IoT AWS Monitoring Simulator
 * Simulates real-time telemetry from Automated Weather Stations.
 */

// Initial station observations
const awsStations = [
  {
    id: 'KJS-AWS-01',
    location: 'SVU Campus, Vidyavihar',
    region: 'Mumbai Coastal',
    temp: 34.2,
    humidity: 68,
    windSpeed: 14.5,
    solarRad: 620,
    variance: -0.1,
    status: 'Online'
  },
  {
    id: 'IMD-AWS-02',
    location: 'Shivajinagar Obs',
    region: 'Pune Central',
    temp: 38.5,
    humidity: 42,
    windSpeed: 12.0,
    solarRad: 810,
    variance: 0.2,
    status: 'Online'
  },
  {
    id: 'IMD-AWS-03',
    location: 'Pashan Meteor Dept',
    region: 'Pune Western',
    temp: 38.8,
    humidity: 41,
    windSpeed: 11.2,
    solarRad: 830,
    variance: 0.0,
    status: 'Online'
  },
  {
    id: 'KJS-AWS-04',
    location: 'Agro Research Stn',
    region: 'Nashik Valley',
    temp: 39.1,
    humidity: 35,
    windSpeed: 15.0,
    solarRad: 860,
    variance: 0.1,
    status: 'Online'
  },
  {
    id: 'IMD-AWS-05',
    location: 'Airport Observatory',
    region: 'Nagpur East',
    temp: 42.6,
    humidity: 22,
    windSpeed: 18.2,
    solarRad: 940,
    variance: -0.3,
    status: 'Online'
  },
  {
    id: 'KJS-AWS-06',
    location: 'Indira Canal Node',
    region: 'Bikaner Border',
    temp: 44.8,
    humidity: 14,
    windSpeed: 22.1,
    solarRad: 980,
    variance: 0.4,
    status: 'Online'
  }
];

document.addEventListener('DOMContentLoaded', () => {
  renderStations();
  
  // Start simulation loops
  setInterval(simulateLiveTicks, 4000);
});

/**
 * Calculates Heat Index using a simplified formula for display purposes.
 */
function calculateHeatIndex(temp, humidity) {
  // Simple heat stress estimation for Celsius
  const index = temp + (humidity * 0.12) - 1.5;
  return index.toFixed(1);
}

/**
 * Renders the initial set of station cards.
 */
function renderStations() {
  const container = document.getElementById('aws-stations-container');
  if (!container) return;

  container.innerHTML = ''; // Clear loading spinner

  awsStations.forEach(station => {
    const heatIndex = calculateHeatIndex(station.temp, station.humidity);
    const varianceColor = station.variance >= 0 ? 'var(--accent-red)' : 'var(--accent-cyan)';
    const varianceSign = station.variance > 0 ? '+' : '';
    
    // Check heat stress severity for glowing card borders
    let glowClass = '';
    if (station.temp > 42) {
      glowClass = 'border-glow-red';
    } else if (station.temp > 39) {
      glowClass = 'border-glow-amber';
    }

    const card = document.createElement('div');
    card.className = `glass-card station-card ${glowClass}`;
    card.id = `card-${station.id}`;
    card.style.transition = 'all 0.5s ease';

    card.innerHTML = `
      <div class="station-card-header">
        <div class="station-info">
          <h3 id="name-${station.id}">${station.location}</h3>
          <span>ID: ${station.id} | ${station.region}</span>
        </div>
        <div class="station-status-pill online">
          <i class="fa-solid fa-circle-nodes"></i>
          <span>${station.status}</span>
        </div>
      </div>
      <div class="station-metrics-grid">
        <div class="metric-box">
          <div class="metric-box-lbl">
            <i class="fa-solid fa-temperature-three-quarters"></i>
            <span>Temp</span>
          </div>
          <div class="metric-box-val" id="temp-${station.id}">${station.temp.toFixed(1)}°C</div>
        </div>
        <div class="metric-box">
          <div class="metric-box-lbl">
            <i class="fa-solid fa-droplet"></i>
            <span>Humidity</span>
          </div>
          <div class="metric-box-val" id="humidity-${station.id}">${station.humidity}%</div>
        </div>
        <div class="metric-box">
          <div class="metric-box-lbl">
            <i class="fa-solid fa-wind"></i>
            <span>Wind Speed</span>
          </div>
          <div class="metric-box-val" id="wind-${station.id}">${station.windSpeed.toFixed(1)} km/h</div>
        </div>
        <div class="metric-box">
          <div class="metric-box-lbl">
            <i class="fa-solid fa-sun"></i>
            <span>Heat Index</span>
          </div>
          <div class="metric-box-val" id="hi-${station.id}">${heatIndex}°C</div>
        </div>
      </div>
      <div class="station-footer">
        <span>Solar Rad: <strong id="solar-${station.id}">${station.solarRad} W/m²</strong></span>
        <span>AI Dev: <strong id="var-${station.id}" style="color: ${varianceColor};">${varianceSign}${station.variance.toFixed(1)}°C</strong></span>
      </div>
    `;

    container.appendChild(card);
  });
}

/**
 * Simulates micro-variations in sensor outputs to mimic live streaming datasets.
 */
function simulateLiveTicks() {
  // Select 1 or 2 random stations to update
  const count = Math.floor(Math.random() * 2) + 1;
  
  for (let i = 0; i < count; i++) {
    const randomIndex = Math.floor(Math.random() * awsStations.length);
    const station = awsStations[randomIndex];

    // Micro variations
    const tempChange = (Math.random() * 0.4 - 0.2); // -0.2 to +0.2
    const humChange = Math.floor(Math.random() * 3) - 1; // -1% to +1%
    const windChange = (Math.random() * 1.0 - 0.5); // -0.5 to +0.5
    const solarChange = Math.floor(Math.random() * 11) - 5; // -5 to +5

    station.temp = Math.max(30, Math.min(48, station.temp + tempChange));
    station.humidity = Math.max(5, Math.min(95, station.humidity + humChange));
    station.windSpeed = Math.max(2, Math.min(40, station.windSpeed + windChange));
    station.solarRad = Math.max(100, Math.min(1100, station.solarRad + solarChange));
    station.variance = Math.max(-0.9, Math.min(0.9, station.variance + (Math.random() * 0.1 - 0.05)));

    // Recalculate Heat Index
    const newHI = calculateHeatIndex(station.temp, station.humidity);

    // Update DOM
    const tempEl = document.getElementById(`temp-${station.id}`);
    const humEl = document.getElementById(`humidity-${station.id}`);
    const windEl = document.getElementById(`wind-${station.id}`);
    const solarEl = document.getElementById(`solar-${station.id}`);
    const hiEl = document.getElementById(`hi-${station.id}`);
    const varEl = document.getElementById(`var-${station.id}`);
    const cardEl = document.getElementById(`card-${station.id}`);

    if (tempEl) tempEl.textContent = `${station.temp.toFixed(1)}°C`;
    if (humEl) humEl.textContent = `${station.humidity}%`;
    if (windEl) windEl.textContent = `${station.windSpeed.toFixed(1)} km/h`;
    if (solarEl) solarEl.textContent = `${station.solarRad} W/m²`;
    if (hiEl) hiEl.textContent = `${newHI}°C`;
    
    if (varEl) {
      const varianceSign = station.variance > 0 ? '+' : '';
      const varianceColor = station.variance >= 0 ? 'var(--accent-red)' : 'var(--accent-cyan)';
      varEl.textContent = `${varianceSign}${station.variance.toFixed(1)}°C`;
      varEl.style.color = varianceColor;
    }

    // Micro flashing feedback loop
    if (cardEl) {
      // Add visual glow border temporarily
      cardEl.style.borderColor = 'rgba(6, 182, 212, 0.4)';
      cardEl.style.transform = 'scale(1.01)';
      
      setTimeout(() => {
        // Reset border based on temperature thresholds
        if (station.temp > 42) {
          cardEl.style.borderColor = 'rgba(239, 68, 68, 0.4)';
        } else if (station.temp > 39) {
          cardEl.style.borderColor = 'rgba(245, 158, 11, 0.4)';
        } else {
          cardEl.style.borderColor = 'var(--border-color)';
        }
        cardEl.style.transform = 'scale(1)';
      }, 500);
    }
  }
}
