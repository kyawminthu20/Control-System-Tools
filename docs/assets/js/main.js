// Control System Standards Atlas — Main JS

// Render Mermaid fenced code blocks on normal site pages
(function () {
  if (!window.mermaid) return;

  function convertFencedMermaid() {
    var converted = [];

    document.querySelectorAll('code.language-mermaid').forEach(function (code) {
      var pre = code.parentElement;
      if (!pre) return;

      // Skip blocks that already live inside a Mermaid container.
      if (pre.classList.contains('mermaid') || pre.closest('.mermaid-wrap')) return;

      var wrap = document.createElement('div');
      wrap.className = 'mermaid-wrap';

      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = code.textContent;

      wrap.appendChild(div);
      pre.replaceWith(wrap);
      converted.push(div);
    });

    if (!converted.length) return;

    try {
      window.mermaid.init(undefined, converted);
    } catch (err) {
      console.error('Mermaid render failed on converted fenced blocks:', err);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', convertFencedMermaid);
  } else {
    convertFencedMermaid();
  }
})();

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

// Local section sidebar: active-page TOC + bucket open-state persistence.
// Runs only when <nav class="sidebar sidebar--local"> is present.
(function () {
  var sidebar = document.querySelector('.sidebar.sidebar--local');
  if (!sidebar) return;

  var groupKey = sidebar.getAttribute('data-topic-group') || 'default';
  var storageKey = 'sidebar-buckets:' + groupKey;

  // ---------- 1. Persist open bucket state --------------------------------
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(storageKey) || '{}') || {}; } catch (e) { saved = {}; }

  var buckets = sidebar.querySelectorAll('.sidebar__bucket');
  buckets.forEach(function (bucket) {
    var name = bucket.getAttribute('data-bucket');
    if (!name) return;

    // Always keep the bucket containing the active page open. Otherwise
    // restore last-session state; default-open markup wins if no entry.
    var hasActive = !!bucket.querySelector('.sidebar__item.is-active');
    if (!hasActive && Object.prototype.hasOwnProperty.call(saved, name)) {
      bucket.open = !!saved[name];
    }

    bucket.addEventListener('toggle', function () {
      try {
        saved[name] = bucket.open;
        localStorage.setItem(storageKey, JSON.stringify(saved));
      } catch (e) { /* quota / private mode — ignore */ }
    });
  });

  // ---------- 2. Inject active-page TOC (H2 / H3) -------------------------
  var tocMount = sidebar.querySelector('[data-local-toc]');
  if (!tocMount) return;

  var main = document.querySelector('.main-content');
  if (!main) return;

  var headings = main.querySelectorAll('h2[id], h3[id]');
  if (!headings.length) return;

  var frag = document.createDocumentFragment();
  headings.forEach(function (h) {
    var li = document.createElement('li');
    var a  = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent.trim();
    a.className = h.tagName === 'H3' ? 'toc-h3' : 'toc-h2';
    li.appendChild(a);
    frag.appendChild(li);
  });
  tocMount.appendChild(frag);

  // Highlight the nearest heading as the user scrolls.
  var tocLinks = tocMount.querySelectorAll('a');
  if (!tocLinks.length || !('IntersectionObserver' in window)) return;

  var byId = {};
  tocLinks.forEach(function (a) {
    byId[a.getAttribute('href').slice(1)] = a;
  });

  var visible = new Set();
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      var id = entry.target.id;
      if (entry.isIntersecting) visible.add(id);
      else visible.delete(id);
    });

    tocLinks.forEach(function (a) { a.classList.remove('is-active'); });

    // Pick the first heading currently intersecting in document order.
    for (var i = 0; i < headings.length; i++) {
      if (visible.has(headings[i].id)) {
        var link = byId[headings[i].id];
        if (link) link.classList.add('is-active');
        break;
      }
    }
  }, {
    rootMargin: '-10% 0px -70% 0px',
    threshold: 0
  });

  headings.forEach(function (h) { observer.observe(h); });
})();

// Diagram lightbox with zoom + pan (mouse, touch, keyboard)
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
    hint.textContent = 'Scroll / pinch to zoom \u00b7 Drag to pan \u00b7 +/\u2212/0 keys \u00b7 Double-click to reset';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close diagram');
    closeBtn.textContent = '\u00D7';

    var controls = document.createElement('div');
    controls.className = 'lightbox-controls';
    function makeBtn(label, ariaLabel) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'lightbox-btn';
      b.setAttribute('aria-label', ariaLabel);
      b.textContent = label;
      return b;
    }
    var zoomInBtn  = makeBtn('+', 'Zoom in');
    var zoomOutBtn = makeBtn('\u2212', 'Zoom out');
    var resetBtn   = makeBtn('\u21BA', 'Reset zoom');
    controls.appendChild(zoomInBtn);
    controls.appendChild(zoomOutBtn);
    controls.appendChild(resetBtn);

    inner.appendChild(closeBtn);
    inner.appendChild(controls);
    inner.appendChild(hint);
    overlay.appendChild(inner);
    document.body.appendChild(overlay);

    var scale = 1, tx = 0, ty = 0;
    var dragging = false, startX, startY, startTx, startTy;
    var pinchDist = 0, pinchStartScale = 1;
    var currentSvg = null;

    function applyTransform() {
      if (!currentSvg) return;
      currentSvg.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + scale + ')';
    }
    function resetTransform() { scale = 1; tx = 0; ty = 0; applyTransform(); }
    function zoomBy(delta) {
      scale = Math.max(0.3, Math.min(8, scale + delta));
      applyTransform();
    }

    zoomInBtn.addEventListener('click',  function (e) { e.stopPropagation(); zoomBy(0.2); });
    zoomOutBtn.addEventListener('click', function (e) { e.stopPropagation(); zoomBy(-0.2); });
    resetBtn.addEventListener('click',   function (e) { e.stopPropagation(); resetTransform(); });

    inner.addEventListener('wheel', function (e) {
      e.preventDefault();
      zoomBy(e.deltaY < 0 ? 0.15 : -0.15);
    }, { passive: false });

    inner.addEventListener('mousedown', function (e) {
      if (e.target.closest('.lightbox-close, .lightbox-btn')) return;
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

    inner.addEventListener('touchstart', function (e) {
      if (e.target.closest('.lightbox-close, .lightbox-btn')) return;
      if (e.touches.length === 1) {
        dragging = true;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        startTx = tx; startTy = ty;
      } else if (e.touches.length === 2) {
        dragging = false;
        var dx0 = e.touches[0].clientX - e.touches[1].clientX;
        var dy0 = e.touches[0].clientY - e.touches[1].clientY;
        pinchDist = Math.sqrt(dx0 * dx0 + dy0 * dy0);
        pinchStartScale = scale;
      }
    }, { passive: true });
    inner.addEventListener('touchmove', function (e) {
      if (e.touches.length === 1 && dragging) {
        e.preventDefault();
        tx = startTx + (e.touches[0].clientX - startX);
        ty = startTy + (e.touches[0].clientY - startY);
        applyTransform();
      } else if (e.touches.length === 2 && pinchDist > 0) {
        e.preventDefault();
        var dx = e.touches[0].clientX - e.touches[1].clientX;
        var dy = e.touches[0].clientY - e.touches[1].clientY;
        var d = Math.sqrt(dx * dx + dy * dy);
        scale = Math.max(0.3, Math.min(8, pinchStartScale * (d / pinchDist)));
        applyTransform();
      }
    }, { passive: false });
    inner.addEventListener('touchend', function (e) {
      if (e.touches.length === 0) { dragging = false; pinchDist = 0; }
    }, { passive: true });

    inner.addEventListener('dblclick', function (e) {
      if (e.target.closest('.lightbox-close, .lightbox-btn')) return;
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
      if (!overlay.classList.contains('is-active')) return;
      if (e.key === 'Escape') close();
      else if (e.key === '+' || e.key === '=') { e.preventDefault(); zoomBy(0.2); }
      else if (e.key === '-' || e.key === '_') { e.preventDefault(); zoomBy(-0.2); }
      else if (e.key === '0') { e.preventDefault(); resetTransform(); }
    });

    document.querySelectorAll('.mermaid').forEach(function (el) {
      var svg = el.querySelector('svg');
      if (!svg) return;
      el.setAttribute('title', 'Click to enlarge \u2014 scroll/pinch/keys to zoom, drag to pan');
      el.addEventListener('click', function () {
        var clone = svg.cloneNode(true);
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

// Standards Finder — faceted filter (Phase 29.4)
// Filter logic: OR within a facet row, AND across rows. No URL persistence.
(function () {
  var root = document.querySelector('[data-finder-filters]');
  if (!root) return;

  var chips = Array.prototype.slice.call(root.querySelectorAll('.finder-chip'));
  var clearBtn = root.querySelector('[data-finder-clear]');
  var countEl = root.querySelector('[data-finder-count]');
  var emptyEl = document.querySelector('[data-finder-empty]');
  var sections = Array.prototype.slice.call(document.querySelectorAll('[data-finder-section]'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.scenario-card[data-finder-region]'));
  var totalCards = cards.length;

  // Initialize aria-pressed so the button has a stable accessibility state.
  chips.forEach(function (chip) { chip.setAttribute('aria-pressed', 'false'); });

  function selectedValues(facet) {
    return chips
      .filter(function (c) { return c.dataset.facet === facet && c.getAttribute('aria-pressed') === 'true'; })
      .map(function (c) { return c.dataset.value; });
  }

  function cardTokens(card, facet) {
    var raw = card.getAttribute('data-finder-' + facet) || '';
    return raw.split(/\s+/).filter(Boolean);
  }

  function matches(card, regionSel, domainSel) {
    if (regionSel.length) {
      var rTokens = cardTokens(card, 'region');
      var rHit = regionSel.some(function (v) { return rTokens.indexOf(v) !== -1; });
      if (!rHit) return false;
    }
    if (domainSel.length) {
      var dTokens = cardTokens(card, 'domain');
      var dHit = domainSel.some(function (v) { return dTokens.indexOf(v) !== -1; });
      if (!dHit) return false;
    }
    return true;
  }

  function applyFilter() {
    var regionSel = selectedValues('region');
    var domainSel = selectedValues('domain');
    var anySelected = regionSel.length + domainSel.length > 0;
    var visibleCount = 0;

    cards.forEach(function (card) {
      var show = matches(card, regionSel, domainSel);
      card.classList.toggle('is-hidden', !show);
      if (show) visibleCount++;
    });

    sections.forEach(function (section) {
      var sectionCards = section.querySelectorAll('.scenario-card[data-finder-region]');
      var anyVisible = false;
      for (var i = 0; i < sectionCards.length; i++) {
        if (!sectionCards[i].classList.contains('is-hidden')) { anyVisible = true; break; }
      }
      section.classList.toggle('is-hidden', !anyVisible);
    });

    if (countEl) {
      countEl.textContent = anySelected
        ? 'Showing ' + visibleCount + ' of ' + totalCards + ' scenarios'
        : 'Showing all ' + totalCards + ' scenarios';
    }
    if (clearBtn) {
      if (anySelected) clearBtn.removeAttribute('hidden');
      else clearBtn.setAttribute('hidden', '');
    }
    if (emptyEl) {
      if (anySelected && visibleCount === 0) emptyEl.removeAttribute('hidden');
      else emptyEl.setAttribute('hidden', '');
    }
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var pressed = chip.getAttribute('aria-pressed') === 'true';
      chip.setAttribute('aria-pressed', pressed ? 'false' : 'true');
      applyFilter();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      chips.forEach(function (c) { c.setAttribute('aria-pressed', 'false'); });
      applyFilter();
    });
  }
})();
