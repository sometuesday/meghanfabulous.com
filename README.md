# meghanfabulous.com

An editorial retrospective of Meghan Fabulous’s twenty-five years as a designer. The site sells nothing. It links, quietly, to the voyage on *Some Tuesday*.

The site as it stood on 30 September 2026 — a one-page thank-you — is kept at `archive/2026-09-30-original-site/`.

## Build

```bash
npm install
npm run build
```

`npm run build` writes a static site to `dist/`. Netlify uses `netlify.toml` (`NODE_VERSION` 22, publish `dist`).

```bash
npm run dev      # local preview with reload
npm run preview  # serve the built site
```

Canonical host is `https://www.meghanfabulous.com`.

## Content

How to add an era, a lookbook, a press item, a journal post, a Making Now piece, or a redirect is in [CONTENT.md](CONTENT.md).

- Eras and journal posts are Markdown in `src/content/`.
- Press, lookbooks, Making Now, worn-by, runway cards, and the Paris Hilton dress story are JSON in `src/data/`.
- Photographs live in `public/images/` as WebP.
- Old URLs are in `public/_redirects` (copied into `dist` on build). Specific story paths come first; splats come last.

The Paris Hilton dress is told in text only. “See the photo” points at James Sissler’s LiveForLiveMusic feature (25 July 2024); the photograph, by Jeff Kravitz, is not on this site.
