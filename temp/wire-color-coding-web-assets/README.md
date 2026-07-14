# Industrial Wire Color Coding — Web Assets

Place this folder under:

`docs/assets/images/wire-color-coding/`

Recommended page location:

`docs/design/wire-color-coding.md`

## Markdown example

```md
<figure class="diagram-card">
  <a href="/Control-System-Tools/assets/images/wire-color-coding/05-plc-24vdc-io-wiring.png">
    <img
      src="/Control-System-Tools/assets/images/wire-color-coding/05-plc-24vdc-io-wiring.png"
      alt="PLC 24 VDC input and output wire color coding example"
      loading="lazy"
    >
  </a>
  <figcaption>PLC 24 VDC I/O wiring and identification example.</figcaption>
</figure>
```

## Responsive gallery example

```html
<div class="diagram-grid">
  <figure>
    <img src="/Control-System-Tools/assets/images/wire-color-coding/02-nfpa79-machinery-panel-us.png"
         alt="NFPA 79 machinery panel wire color convention"
         loading="lazy">
    <figcaption>NFPA 79-style machinery panel convention.</figcaption>
  </figure>

  <figure>
    <img src="/Control-System-Tools/assets/images/wire-color-coding/03-iec60204-machinery-panel.png"
         alt="IEC 60204-1 machinery wire color convention"
         loading="lazy">
    <figcaption>IEC machinery conductor identification.</figcaption>
  </figure>
</div>
```

## CSS

```css
.diagram-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1rem;
  align-items: start;
}

.diagram-grid figure,
.diagram-card {
  margin: 0;
  padding: 0.75rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.5rem;
  background: var(--md-default-bg-color);
}

.diagram-grid img,
.diagram-card img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 0.25rem;
}

.diagram-grid figcaption,
.diagram-card figcaption {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  line-height: 1.35;
}
```

## Recommended page grouping

1. Standards and general conventions
2. Machinery and facility power
3. PLC and control circuits
4. Instrumentation and intrinsically safe systems
5. VFD, servo and motion systems
6. HVAC and semiconductor facilities
7. Industrial networks
8. Legacy systems and field notes

## Important technical note

These graphics should be presented as engineering examples. The page should state that local code, the authority having jurisdiction, customer standards, and project drawings take precedence.
