---
layout: default
title: "Glossary"
description: "Definitions of key terms, acronyms, and abbreviations used in industrial control systems and machine safety standards."
breadcrumb:
  - name: "Reference"
  - name: "Glossary"
last_reviewed: "2026-03-08"
redirect_from:
  - /glossary/
  - /glossary/index.html
review:
  standard: "Terminology across the standards library"
  edition: "n/a — cross-standard glossary"
  status: "Review pending"
  coverage: "Paraphrased term definitions for education; each standard's own definitions govern."
  last_reviewed: "April 2026"
---

<div class="page-header">
  <span class="page-header__label">Reference</span>
  <h1>Glossary</h1>
  <p>Key terms, acronyms, and abbreviations used across industrial control systems, machine safety, and electrical standards.</p>
</div>

{% assign sorted_terms = site.data.glossary | sort: "acronym" %}

{% comment %}Build the set of first letters present{% endcomment %}
{% assign letters_present = "" %}
{% for entry in sorted_terms %}
  {% assign first = entry.acronym | slice: 0 | upcase %}
  {% unless letters_present contains first %}
    {% assign letters_present = letters_present | append: first | append: "," %}
  {% endunless %}
{% endfor %}
{% assign letter_list = letters_present | split: "," %}

<nav class="glossary-az" aria-label="Jump to letter">
{% for letter in letter_list %}{% if letter != "" %}<a href="#letter-{{ letter }}">{{ letter }}</a>{% endif %}{% endfor %}
</nav>

{% assign current_letter = "" %}
{% for entry in sorted_terms %}
{% assign first = entry.acronym | slice: 0 | upcase %}
{% if first != current_letter %}
  {% assign current_letter = first %}
  <h2 class="glossary-letter" id="letter-{{ first }}">{{ first }}</h2>
{% endif %}

<div class="glossary-entry" id="{{ entry.acronym | downcase | replace: ' ', '-' | replace: '/', '-' }}">
  <div class="glossary-entry__header">
    <span class="glossary-entry__acronym">{{ entry.acronym }}</span>
    <span class="glossary-entry__term">{{ entry.term }}</span>
    <span class="badge badge--domain badge--domain-{{ entry.domain }}">{{ entry.domain | replace: "-", " " }}</span>
  </div>
  <p class="glossary-entry__definition">{{ entry.definition }}</p>
  <dl class="glossary-entry__meta">
    {% if entry.standard_pages.size > 0 %}
    <dt>Standard</dt>
    <dd>{% for s in entry.standard_pages %}<a href="{{ s.url | relative_url }}">{{ s.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
    {% if entry.lifecycle_stages.size > 0 %}
    <dt>Lifecycle</dt>
    <dd>{% for stage in entry.lifecycle_stages %}{% assign stage_url = site.data.lifecycle_stage_urls[stage.slug] %}<a href="{{ stage_url | relative_url }}">{{ stage.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
    {% if entry.related_terms.size > 0 %}
    <dt>See also</dt>
    <dd>{% for rel in entry.related_terms %}<a href="#{{ rel | downcase | replace: ' ', '-' | replace: '/', '-' }}">{{ rel }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</dd>
    {% endif %}
  </dl>
</div>
{% endfor %}
