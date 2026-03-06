// Control System Standards Atlas — Main JS

// Sidebar mobile toggle
(function () {
  var toggle = document.getElementById('sidebar-toggle');
  var sidebar = document.getElementById('sidebar');
  if (toggle && sidebar) {
    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('is-open');
    });
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function (e) {
      if (sidebar.classList.contains('is-open') &&
          !sidebar.contains(e.target) &&
          e.target !== toggle) {
        sidebar.classList.remove('is-open');
      }
    });
  }
})();

// Mark active sidebar links
(function () {
  var current = window.location.pathname;
  var links = document.querySelectorAll('.sidebar__links a');
  links.forEach(function (link) {
    var href = link.getAttribute('href');
    if (href && current === href) {
      link.classList.add('active');
      // Open parent details
      var details = link.closest('details');
      if (details) details.open = true;
    }
  });
})();

// Diagram lightbox
(function () {
  function initLightbox() {
    // Build overlay DOM with safe element creation (no dynamic innerHTML)
    var overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Diagram enlarged view');

    var inner = document.createElement('div');
    inner.className = 'lightbox-inner';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close diagram');
    closeBtn.textContent = '\u00D7';

    inner.appendChild(closeBtn);
    overlay.appendChild(inner);
    document.body.appendChild(overlay);

    function close() {
      overlay.classList.remove('is-active');
      var svgs = inner.querySelectorAll('svg');
      svgs.forEach(function (svg) { inner.removeChild(svg); });
    }

    closeBtn.addEventListener('click', close);

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('is-active')) close();
    });

    document.querySelectorAll('.mermaid').forEach(function (el) {
      var svg = el.querySelector('svg');
      if (!svg) return;
      el.setAttribute('title', 'Click to enlarge');
      el.addEventListener('click', function () {
        inner.appendChild(svg.cloneNode(true));
        overlay.classList.add('is-active');
      });
    });
  }

  // Mermaid renders after DOMContentLoaded; use window load + small delay
  if (document.readyState === 'complete') {
    setTimeout(initLightbox, 150);
  } else {
    window.addEventListener('load', function () {
      setTimeout(initLightbox, 150);
    });
  }
})();
