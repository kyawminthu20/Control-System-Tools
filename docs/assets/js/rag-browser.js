(function () {
  'use strict';

  var fileBody  = document.getElementById('rag-file-body');
  var filePath  = document.getElementById('rag-file-path');
  var rawLink   = document.getElementById('rag-raw-link');
  var activeBtn = null;

  function escHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function safeSetHtml(el, html) {
    // Sanitize with DOMPurify when available, otherwise fall back to text-only
    if (window.DOMPurify) {
      el.innerHTML = DOMPurify.sanitize(html, { USE_PROFILES: { html: true } });
    } else {
      el.textContent = html; // should not happen — DOMPurify is loaded in layout
    }
  }

  function setLoading(path) {
    filePath.textContent = path;
    rawLink.style.display = 'none';
    safeSetHtml(fileBody, '<p class="rag-loading">Loading\u2026</p>');
  }

  function setError(path, msg) {
    safeSetHtml(fileBody,
      '<p class="rag-error">Failed to load <code>' +
      escHtml(path) + '</code>: ' + escHtml(msg) + '</p>');
  }

  function renderFile(path, servePath) {
    // Fetch from same-origin static asset — works for private repos too.
    var url = window.RAG_SERVE_BASE + servePath;
    setLoading(path);

    fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.text();
      })
      .then(function (text) {
        filePath.textContent = path;
        rawLink.href = url;
        rawLink.style.display = 'inline';

        var html = (typeof marked !== 'undefined')
          ? marked.parse(text)
          : '<pre>' + escHtml(text) + '</pre>';

        safeSetHtml(fileBody, html);
        fileBody.scrollTop = 0;

        // Re-run mermaid on any fenced code blocks tagged as mermaid
        if (window.mermaid) {
          fileBody.querySelectorAll('code.language-mermaid').forEach(function (code) {
            var pre = code.parentElement;
            var div = document.createElement('div');
            div.className = 'mermaid';
            div.textContent = code.textContent;
            pre.replaceWith(div);
          });
          var mermaidDivs = fileBody.querySelectorAll('.mermaid');
          if (mermaidDivs.length) {
            mermaid.init(undefined, mermaidDivs);
          }
        }
      })
      .catch(function (err) {
        setError(path, err.message);
      });
  }

  function attachHandlers() {
    document.querySelectorAll('.rag-file-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (activeBtn) activeBtn.classList.remove('rag-file-btn--active');
        activeBtn = btn;
        btn.classList.add('rag-file-btn--active');

        // Ensure ancestor <details> are open so the file stays visible in tree
        var el = btn.parentElement;
        while (el && el !== document.body) {
          if (el.tagName === 'DETAILS') el.open = true;
          el = el.parentElement;
        }

        renderFile(btn.dataset.path, btn.dataset.servePath);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachHandlers);
  } else {
    attachHandlers();
  }
})();
