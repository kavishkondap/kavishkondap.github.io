# kavishkondap.github.io

Personal site — bio, papers, experience, projects. Live at <https://kavishkondap.github.io>.

Static single page: `index.html` (all CSS inline), assets in `assets/`.
`.nojekyll` disables Jekyll so files are served as-is.

## Editing

- **Content** — everything lives in `index.html`, in `<section>` blocks (`#papers`,
  `#experience`, `#projects`). Copy an existing `.entry` or `.job` block to add one.
- **Colors** — CSS custom properties on `:root`, with a dark-mode override below it.
- **Photo** — `assets/portrait.jpg`, square crop. If missing, the header falls back
  to a "KK" placeholder.

## Things to keep out of this repo

- **No CV / resume.** It carries a phone number and home-adjacent details; keep it
  off the public site.
- **No plaintext email.** The address never appears in the page source — it is
  base64 in a `data-e` attribute on `a.js-email` and assembled by JS on click.
  Don't replace those with a plain `mailto:` link.
- Commit with the GitHub noreply author address, not a personal one:
  `git config user.email 65979777+kavishkondap@users.noreply.github.com`

## Conventions

- **No em dashes** anywhere in the copy.
- **Every external link** gets `target="_blank" rel="noopener noreferrer"`.
- **Paper entries** link from the title only, with no separate link row underneath.
  Author lists use full first and last names, with `<span class="me">` on mine.
- **Fonts** are Source Serif 4 (body) and IBM Plex Mono (labels, dates, venues),
  set as `--serif` and `--mono` on `:root`. To swap, change those two variables
  and the Google Fonts `<link>`.
- **Older papers** live in `#older-papers`, hidden behind the toggle at the bottom
  of the Papers section.
- **Paper media** sits in `.entry-media`, a fixed 240px x 135px (16:9) box.
  Every asset is authored at exactly **480x270** so nothing is cropped at render
  time; do the cropping when generating the asset, not in CSS. Videos are muted,
  looping, `playsinline`, carry a matching `.jpg` poster, and pause when the
  viewer prefers reduced motion.

## After changing anything in assets/

GitHub Pages serves assets with `cache-control: max-age=600`, and replacing a
file in place keeps its URL, so browsers can keep showing the old version. Run:

    python3 tools/stamp-assets.py

It appends a content hash to each asset URL (`assets/robosq.jpg?v=4be898ea`), so
a changed file always gets a new URL. Commit the result alongside the asset.

## Preview

    python3 -m http.server 8000

then open <http://localhost:8000>.
