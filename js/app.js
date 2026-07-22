/**
 * Main Application Script
 * Provides common UI behaviors: mobile sidebar drawer toggling, dynamic status, and general telemetry.
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  updateSystemTime();
  setInterval(updateSystemTime, 60000); // Update time every minute
});

/**
 * Initializes mobile responsive sidebar events.
 */
function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const sidebar = document.querySelector('.sidebar');
  
  if (!menuBtn || !sidebar) return;

  // Create backdrop if not exists
  let backdrop = document.querySelector('.sidebar-backdrop');
  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.className = 'sidebar-backdrop';
    document.body.appendChild(backdrop);
  }

  // Toggle open
  menuBtn.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    backdrop.classList.toggle('active');
  });

  // Close when clicking backdrop
  backdrop.addEventListener('click', () => {
    sidebar.classList.remove('active');
    backdrop.classList.remove('active');
  });

  // Close when clicking sidebar links on mobile
  const links = sidebar.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', () => {
      sidebar.classList.remove('active');
      backdrop.classList.remove('active');
    });
  });
}

/**
 * Updates the local time and displays it in the header.
 */
function updateSystemTime() {
  const timeEl = document.querySelector('.system-time-val');
  if (!timeEl) return;
  const now = new Date();
  timeEl.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}
