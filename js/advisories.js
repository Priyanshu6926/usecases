/**
 * LLM Advisory Generator Simulator
 * Emulates high-fidelity LLM response streaming based on input criteria.
 */

// Advisory Database Templates
const advisoryTemplates = {
  farmers: {
    extreme: `### 🚨 EMERGENCY AGRICULTURAL DIRECTIVE
**Region:** [REGION]
**Target:** Crop Protection & Livestock Systems
**Severity:** RED ALERT (Extreme Heat stress forecasted)

1. **Evaporative Transpiration Defense:** Apply micro-sprinklers or drip systems strictly during nocturnal window (8 PM - 11 PM) or early morning (3:30 AM - 5:30 AM) to minimize water losses. Maintain 2-inch straw mulch covers on crops.
2. **Livestock Hydration & Cooling:** Shelter dairy cows, goats, and poultry in heavily thatched sheds. Mix potassium carbonate (electrolyte) and cool water in reservoirs. Apply water misting to cows during peak hours (12 PM - 3 PM).
3. **Field Labor Split-Shifts:** Suspend all physical labor in fields between 11:00 AM and 4:00 PM. Establish temporary hydration stations with ORS and drinking water under tree canopies.
4. **Foliar Protection:** Spray a 5% kaolin clay suspension on orchard leaves to form a solar-reflective barrier, minimizing leaf scald and moisture loss.`,
    severe: `### ⚠️ SEVERE AGRICULTURAL ADVISORY
**Region:** [REGION]
**Target:** Crop Protection & Livestock Systems
**Severity:** ORANGE ALERT (High heat stress)

1. **Irrigation Frequency:** Increase watering intervals for shallow-rooted vegetable crops to once every 24-36 hours. Avoid heavy noon watering.
2. **Livestock Heat Management:** Maintain maximum ventilation. Keep feed troughs shaded. Provide ad-libitum clean drinking water.
3. **Labor Precautions:** Restrict manual activities during peak noon (12 PM - 3 PM). Ensure workers take 15-minute hydration breaks every hour.
4. **Soil Moisture Control:** Implement light hoeing to create soil dust mulch, breaking capillary tubes to conserve soil humidity.`,
    mild: `### ℹ️ GENERAL AGRICULTURAL ADVISORY
**Region:** [REGION]
**Target:** Crop Protection & Livestock Systems
**Severity:** YELLOW ALERT (Moderate heat)

1. **Monitoring Crop Turgor:** Check leaves for wilting in the late afternoon. Schedule regular watering cycles.
2. **Ventilation in Animal Barns:** Keep ceiling fans and exhaust systems active in cattle barns and poultry coops.
3. **Hydration:** Ensure workers have access to clean drinking water and shades.`
  },
  health: {
    extreme: `### 🚨 PUBLIC HEALTH SYSTEM EMERGENCY BULLETIN
**Region:** [REGION]
**Target:** Hospital Networks & Community Health Teams
**Severity:** RED ALERT (Critical heatstroke surge risk)

1. **Activation of Cold Wards:** Declare a 'Heat Emergency State' across all district hospitals. Prepare dedicated cooling beds equipped with ice-packs and cooling blankets.
2. **Medical Supplies Reserves:** Stockpile intravenous saline solutions, oral rehydration packets (ORS), and core temperature measuring equipment.
3. **Community Care outreach:** Dispatch health workers to perform daily wellness checks on high-risk demographics, including elderly citizens living alone and roofless individuals.
4. **Symptom Telemetry:** Enforce daily reporting of heat-related illness admissions from all outpatient clinics to monitor hotspot trends.`,
    severe: `### ⚠️ PUBLIC HEALTH SYSTEM WARNING
**Region:** [REGION]
**Target:** Primary Healthcare Providers
**Severity:** ORANGE ALERT (Elevated risk of heat stress)

1. **ORS Corner Setup:** Establish active ORS distribution points in all government clinics and public buildings.
2. **Awareness Dissemination:** Distribute educational flyers detailing symptoms of heat exhaustion versus heatstroke to local schools and workplaces.
3. **Vulnerable Protection:** Coordinate with shelters to ensure adequate ventilation and drinking water access.
4. **Emergency Services Readiness:** Ensure ambulance fleets have working AC units and passive cooling materials.`,
    mild: `### ℹ️ HEALTH & WELLNESS ADVISORY
**Region:** [REGION]
**Target:** Local Clinics & Wellness Centers
**Severity:** YELLOW ALERT (Mild to moderate risk)

1. **Hydration Alerts:** Send SMS alerts warning citizens to drink water regularly.
2. **Clinic Audits:** Verify that local pharmacies maintain adequate ORS inventories.
3. **Vulnerability Advice:** Advise elderly and pediatric outpatient cases to avoid midday outdoor activities.`
  },
  municipal: {
    extreme: `### 🚨 MUNICIPAL MOBILISATION DIRECTIVE
**Region:** [REGION]
**Target:** Urban Development & Utility Agencies
**Severity:** RED ALERT (Urban Heat Island crisis)

1. **Opening Public Cooling Hubs:** Repurpose government offices, community halls, and parks into public 'Cooling Shelters' with running AC and drinking water.
2. **Emergency Water Supply:** Coordinate tank routes to high-density slums facing grid pipe shortages. Ensure public drinking taps are operational.
3. **Power Grid Load Auditing:** Restrict scheduled power shutdowns. Scan distribution transformers in high-load heat pockets using thermal cameras.
4. **Cool Roof Initiative:** Deploy temporary canvas canopy coverings over busy market streets and apply solar-reflective white coatings to slum roofs.`,
    severe: `### ⚠️ MUNICIPAL CORP MITIGATION ORDER
**Region:** [REGION]
**Target:** City Management Teams
**Severity:** ORANGE ALERT (Heatwave mitigation active)

1. **Transit Shelter Shade:** Install green mesh shade sails over major traffic intersections and bus stands.
2. **Water Resource Mobilization:** Fill urban fountains and activate roadside misting booths in dense commercial zones.
3. **Energy Management:** Ask corporate offices to calibrate AC settings to 24°C to avoid power grid overloads.
4. **Waste Management Safety:** Reschedule sanitation worker shifts to end before 11:30 AM to protect crews.`,
    mild: `### ℹ️ URBAN HEAT ADVISORY
**Region:** [REGION]
**Target:** Ward Offices & Public Spaces
**Severity:** YELLOW ALERT (General monitoring)

1. **Public Parks Access:** Keep public parks open during early afternoon hours to offer shaded refuge.
2. **Hydration Stations:** Encourage NGOs to set up drinking water stalls near main transport terminals.
3. **Routine Checks:** Monitor water pressure and grid load levels.`
  },
  citizens: {
    extreme: `### 🚨 URGENT CITIZEN SAFETY PROTOCOL
**Region:** [REGION]
**Target:** Citizens, Commuters, & Outdoor Workers
**Severity:** RED ALERT (Extreme heat index warning)

1. **Outdoor Activity Bans:** Strictly avoid going outdoors between 11:00 AM and 4:00 PM. Do not perform heavy workouts or manual tasks under direct sunlight.
2. **Forced Hydration Schedule:** Drink 3.5 to 5 liters of water daily. Consume buttermilk, lemon juice, or ORS water regularly, even if not feeling thirsty. Avoid caffeinated beverages.
3. **Emergency Symptom Watch:** Monitor yourself and others for heatstroke signs: sudden dry hot skin, rapid heartbeat, confusion, nausea, and throbbing headaches. Call 108 immediately.
4. **Protection of Dependents:** Keep young children, pregnant women, elderly relatives, and domestic animals inside cool, ventilated rooms. Never leave anyone in locked, parked cars.`,
    severe: `### ⚠️ CITIZEN SAFETY GUIDELINES
**Region:** [REGION]
**Target:** General Public & Transit Commuters
**Severity:** ORANGE ALERT (High temperatures warning)

1. **Clothing & Gear:** Wear lightweight, light-colored, loose cotton clothes. Carry an umbrella, hat, and water bottle whenever outdoors.
2. **Home Cooling:** Use damp curtains, night ventilation, and air coolers. Avoid using heat-generating appliances during the hottest hours.
3. **Hydration Habits:** Consume fresh fruits with high water content (watermelon, cucumber, oranges). Keep oral rehydration salts handy.
4. **Pet Safety:** Ensure pets are kept in shaded areas with plenty of fresh water.`,
    mild: `### ℹ️ GENERAL CITIZEN SAFETY TIP
**Region:** [REGION]
**Target:** General Public
**Severity:** YELLOW ALERT (Warm weather precautions)

1. **Sun Exposure:** Wear sunglasses and sunscreen when going outdoors.
2. **Water Intake:** Drink water at regular intervals. Avoid drinking ice-cold water immediately after coming from hot sun.
3. **Pet Advice:** Do not walk dogs on hot asphalt during midday.`
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('advisory-form');
  if (form) {
    form.addEventListener('submit', handleFormSubmit);
  }

  // Parse URL parameters (e.g. ?region=west&severity=severe)
  const urlParams = new URLSearchParams(window.location.search);
  const regionParam = urlParams.get('region');
  const severityParam = urlParams.get('severity');

  const regionSelect = document.getElementById('region');
  const severitySelect = document.getElementById('severity');

  if (regionParam && regionSelect) {
    const matchedOpt = Array.from(regionSelect.options).find(opt => opt.value === regionParam);
    if (matchedOpt) regionSelect.value = regionParam;
  }

  if (severityParam && severitySelect) {
    const matchedOpt = Array.from(severitySelect.options).find(opt => opt.value === severityParam);
    if (matchedOpt) severitySelect.value = severityParam;
  }
});

/**
 * Handles the advisory generation form submission.
 */
function handleFormSubmit(e) {
  e.preventDefault();

  const stakeholder = document.getElementById('stakeholder').value;
  const region = document.getElementById('region').value;
  const severity = document.getElementById('severity').value;
  const generateBtn = document.getElementById('generate-btn');

  // Load template
  let advisoryText = advisoryTemplates[stakeholder]?.[severity] || 'Advisory template not found.';
  advisoryText = advisoryText.replace('[REGION]', region.toUpperCase());

  // Show typing state
  const outputContainer = document.getElementById('advisory-output');
  const badgeContainer = document.getElementById('advisory-status-badge');
  
  if (!outputContainer) return;

  // Disable button
  generateBtn.disabled = true;
  generateBtn.querySelector('span').textContent = 'Generating advisory...';
  
  // Set status badge style
  badgeContainer.textContent = severity.toUpperCase() + ' ALERT';
  if (severity === 'extreme') {
    badgeContainer.className = 'region-detail-badge badge-extreme';
  } else if (severity === 'severe') {
    badgeContainer.className = 'region-detail-badge badge-high';
  } else {
    badgeContainer.className = 'region-detail-badge badge-low';
  }

  // Clear output and add typing class
  outputContainer.innerHTML = '';
  outputContainer.classList.add('typing');

  // Simulate streaming text (typing animation)
  let index = 0;
  // Increase character increment rate to speed up typing of long text blocks
  const speed = 10; // ms
  const charsPerTick = 4; // type 4 characters at a time to look natural but fast

  function streamText() {
    if (index < advisoryText.length) {
      const nextChunk = advisoryText.substring(0, index + charsPerTick);
      // Simple markdown preview parser for bold and lists in typing
      outputContainer.innerHTML = parseMarkdownSimple(nextChunk);
      index += charsPerTick;
      outputContainer.scrollTop = outputContainer.scrollHeight;
      setTimeout(streamText, speed);
    } else {
      // Completed typing
      outputContainer.innerHTML = parseMarkdownSimple(advisoryText);
      outputContainer.classList.remove('typing');
      generateBtn.disabled = false;
      generateBtn.querySelector('span').textContent = 'Generate LLM Advisory';
    }
  }

  streamText();
}

/**
 * High-fidelity lightweight parser to turn basic markdown into stylized HTML in the output window.
 */
function parseMarkdownSimple(text) {
  let html = text;
  
  // Escape HTML
  html = html
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  // Bold headings (### Title)
  html = html.replace(/^### (.*$)/gim, '<h4 style="font-size: 16px; color: #ffffff; margin: 16px 0 8px 0; border-left: 3px solid var(--accent-orange); padding-left: 10px;">$1</h4>');
  
  // Bold text (**text**)
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong style="color: #ffffff;">$1</strong>');

  // Bullet items (1. Text or - Text)
  html = html.replace(/^\d+\.\s(.*$)/gim, '<div style="margin-left: 16px; margin-bottom: 8px; display: flex; gap: 8px;"><span style="color: var(--accent-orange); font-weight: bold;">•</span><span>$1</span></div>');
  html = html.replace(/^-\s(.*$)/gim, '<div style="margin-left: 16px; margin-bottom: 8px; display: flex; gap: 8px;"><span style="color: var(--accent-cyan); font-weight: bold;">-</span><span>$1</span></div>');

  // Convert line breaks to <br> (but not if already block tags)
  html = html.replace(/(?:\r\n|\r|\n)/g, '<br>');

  // Clean empty tags from double brs
  html = html.replace(/(<br>){2,}/g, '<br><br>');

  return html;
}
