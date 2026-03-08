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

// Diagram lightbox with zoom + pan
(function () {
  function initLightbox() {
    var overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Diagram enlarged view');

    var inner = document.createElement('div');
    inner.className = 'lightbox-inner';

    var hint = document.createElement('p');
    hint.className = 'lightbox-hint';
    hint.textContent = 'Scroll to zoom \u00b7 Drag to pan \u00b7 Double-click to reset';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close diagram');
    closeBtn.textContent = '\u00D7';

    inner.appendChild(closeBtn);
    inner.appendChild(hint);
    overlay.appendChild(inner);
    document.body.appendChild(overlay);

    // Pan/zoom state
    var scale = 1, tx = 0, ty = 0;
    var dragging = false, startX, startY, startTx, startTy;
    var currentSvg = null;

    function applyTransform() {
      if (!currentSvg) return;
      currentSvg.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + scale + ')';
    }

    function resetTransform() {
      scale = 1; tx = 0; ty = 0;
      applyTransform();
    }

    inner.addEventListener('wheel', function (e) {
      e.preventDefault();
      var delta = e.deltaY < 0 ? 0.15 : -0.15;
      scale = Math.max(0.3, Math.min(8, scale + delta));
      applyTransform();
    }, { passive: false });

    inner.addEventListener('mousedown', function (e) {
      if (e.target === closeBtn) return;
      dragging = true;
      startX = e.clientX; startY = e.clientY;
      startTx = tx; startTy = ty;
      inner.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', function (e) {
      if (!dragging) return;
      tx = startTx + (e.clientX - startX);
      ty = startTy + (e.clientY - startY);
      applyTransform();
    });

    window.addEventListener('mouseup', function () {
      dragging = false;
      inner.style.cursor = '';
    });

    inner.addEventListener('dblclick', function (e) {
      if (e.target === closeBtn) return;
      resetTransform();
    });

    function close() {
      overlay.classList.remove('is-active');
      if (currentSvg) { inner.removeChild(currentSvg); currentSvg = null; }
      resetTransform();
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
      el.setAttribute('title', 'Click to enlarge \u2014 scroll/drag to zoom & pan');
      el.addEventListener('click', function () {
        var clone = svg.cloneNode(true);
        // Remove fixed dimensions so SVG fills the lightbox naturally
        clone.removeAttribute('width');
        clone.removeAttribute('height');
        clone.style.width = '100%';
        clone.style.height = 'auto';
        clone.style.transformOrigin = 'center center';
        clone.style.transition = 'transform 0.1s ease';
        clone.style.display = 'block';
        currentSvg = clone;
        inner.appendChild(clone);
        resetTransform();
        overlay.classList.add('is-active');
      });
    });
  }

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

// Theme toggle
(function () {
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function updateBtn(theme) {
    btn.textContent = theme === 'dark' ? '\u2600' : '\u263E'; // ☀ or ☾
    btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    btn.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
  }

  // Sync button icon with current theme (set by inline head script)
  var current = document.documentElement.getAttribute('data-theme') || 'light';
  updateBtn(current);

  btn.addEventListener('click', function () {
    var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateBtn(next);
  });
})();
