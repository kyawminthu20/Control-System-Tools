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

// Client-side search (lunr.js)
(function () {
  var searchInput = document.getElementById('search-input');
  var searchDropdown = document.getElementById('search-dropdown');
  if (!searchInput || !searchDropdown) return;

  var lunrIndex = null;
  var docs = [];
  var selectedIndex = -1;

  var searchUrl = searchInput.getAttribute('data-search-url');

  fetch(searchUrl)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      docs = data;
      lunrIndex = lunr(function () {
        this.field('title', { boost: 10 });
        this.field('section', { boost: 5 });
        this.field('content');
        this.ref('url');
        data.forEach(function (doc) { this.add(doc); }, this);
      });
    })
    .catch(function () { /* search unavailable — silent fail */ });

  function sectionLabel(s) {
    if (!s) return '';
    return s.charAt(0).toUpperCase() + s.slice(1).replace(/-/g, ' ');
  }

  function clearDropdown() {
    while (searchDropdown.firstChild) {
      searchDropdown.removeChild(searchDropdown.firstChild);
    }
  }

  function buildResultNode(doc) {
    // Use safe DOM methods — no innerHTML with dynamic data
    var a = document.createElement('a');
    a.className = 'search-result';
    a.href = doc.url;
    a.setAttribute('role', 'option');

    var sec = sectionLabel(doc.section);
    if (sec) {
      var secSpan = document.createElement('span');
      secSpan.className = 'search-result__section';
      secSpan.textContent = sec;
      a.appendChild(secSpan);
    }

    var titleSpan = document.createElement('span');
    titleSpan.className = 'search-result__title';
    titleSpan.textContent = doc.title;
    a.appendChild(titleSpan);

    return a;
  }

  function renderResults(results) {
    selectedIndex = -1;
    clearDropdown();

    if (!results.length) {
      var empty = document.createElement('div');
      empty.className = 'search-dropdown__empty';
      empty.textContent = 'No results';
      searchDropdown.appendChild(empty);
      searchDropdown.classList.add('is-open');
      return;
    }

    results.slice(0, 8).forEach(function (r) {
      var doc = docs.find(function (d) { return d.url === r.ref; });
      if (!doc) return;
      searchDropdown.appendChild(buildResultNode(doc));
    });

    searchDropdown.classList.add('is-open');
  }

  function close() {
    searchDropdown.classList.remove('is-open');
    clearDropdown();
    selectedIndex = -1;
  }

  searchInput.addEventListener('input', function () {
    var q = searchInput.value.trim();
    if (!q || !lunrIndex) { close(); return; }
    var results = lunrIndex.search(q + '*');
    if (!results.length) results = lunrIndex.search(q);
    renderResults(results);
  });

  searchInput.addEventListener('keydown', function (e) {
    var items = searchDropdown.querySelectorAll('.search-result');
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
      items.forEach(function (el, i) { el.classList.toggle('is-selected', i === selectedIndex); });
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = Math.max(selectedIndex - 1, -1);
      items.forEach(function (el, i) { el.classList.toggle('is-selected', i === selectedIndex); });
    } else if (e.key === 'Enter' && selectedIndex >= 0) {
      e.preventDefault();
      items[selectedIndex].click();
    } else if (e.key === 'Escape') {
      close();
      searchInput.blur();
    }
  });

  document.addEventListener('click', function (e) {
    if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
      close();
    }
  });
})();
