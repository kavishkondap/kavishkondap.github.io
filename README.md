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

## Preview

    python3 -m http.server 8000

then open <http://localhost:8000>.
