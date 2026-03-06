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
