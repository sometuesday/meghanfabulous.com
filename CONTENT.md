# Adding to the site

The site is a static Astro build. Content lives in files. After a change, `npm run build` rewrites `dist/`.

## An era

Add `src/content/eras/your-slug.md`.

```yaml
---
title: "The name of the era"
years: "1999–01"
order: 7
summary: "One sentence for the index and the meta description."
next: "the-slug-that-follows"
lead: "/images/your-lead.webp"
leadAlt: "What the photograph shows."
lookbooks: []
facts:
  - label: "Label"
    text: "The fact, as sourced."
    source: "Publication, date"
    url: "https://example.com/story"
---
```

The body is the intro. Leave `url` off a fact that has no link. `next` on the previous era should point here.

## A lookbook

Add the frames under `public/images/lookbooks/your-slug/`, then an object in `src/data/looks.json`:

```json
{
  "slug": "your-slug",
  "name": "The Name",
  "archetype": "The Name",
  "era": "the-world",
  "cover": "/images/lookbooks/your-slug/01.webp",
  "frames": [
    { "src": "/images/lookbooks/your-slug/01.webp", "w": 1200, "h": 1600, "alt": "What is in the frame." }
  ]
}
```

Do not put a year or a photographer credit on a lookbook, in the alt text or anywhere else. `era` only decides which era page shows the cover. Use `the-runway-years` or `the-world`.

Old Shopify paths redirect from `/pages/your-slug` once that line is in `public/_redirects`.

## A press item

Add an object to the `items` array in `src/data/press.json`. It works with no scan.

```json
{
  "id": "outlet-year",
  "date": "2008-09-11",
  "dateLabel": "11 September 2008",
  "year": 2008,
  "outlet": "Drapers",
  "headline": "The headline",
  "type": "magazine",
  "filters": ["all", "magazines"],
  "url": "https://example.com/story",
  "note": "One sourced sentence.",
  "quote": "",
  "scans": [],
  "featured": false,
  "era": "the-world",
  "coverAlt": ""
}
```

Leave `date` null and `dateLabel` empty when the clipping is undated. Do not guess a date.

Filters the page understands: `all`, `magazines`, `runway`, `tv`, `worn-by`, `japan`, `uk`, `business`. Always include `all`.

`featured: true` puts the first scan on the cover wall. If there is no scan, the wall shows the outlet as type.

### Adding a press scan later

1. Put the photograph in `public/images/press/`, as a `.webp` if you can.
2. Add it to that item’s `scans` array:

```json
{ "src": "/images/press/your-scan.webp", "w": 1400, "h": 1800, "alt": "What the page shows, including the outlet if it is legible." }
```

Nothing else has to change. The row gains a View button, and the lightbox uses the alt text.

## A Journal post

Add `src/content/journal/your-slug.md`.

```yaml
---
title: "Title"
date: 2026-01-02
author: "Meghan Fabulous"
description: "A sentence for the index and for search."
originalPath: "/blogs/the-daily-fab/your-old-handle"
---
```

`originalPath` is the old URL path. Add a matching 301 in `public/_redirects` **above** the `/blogs/the-daily-fab/*` splat, or the splat will catch it and send people to the index.

Images go in `public/images/journal/your-slug/` and are referenced as normal markdown. Give every image alt text. Do not paste internal editing notes into the file.

The Paris Hilton dress is text only. The “See the photo” link lives in `src/data/paris-dress.json` and in the journal story. Do not add a photograph of her.

## Making Now

Add an object to `items` in `src/data/making-now.json`: `id`, `date`, `dateLabel`, `title`, `image`, `width`, `height`, `alt`, `instagram`, `text`, `behind`.

Pieces that are not for sale should keep `"behind": true`. The page prints “Not for sale — made for joy.”

## Meg’s Favorite Things

In `src/data/favorites.json`, add an item under a theme (`boat-life`, `studio-kit`, `beauty-at-sea`):

```json
{ "name": "The thing", "text": "One sentence in her voice.", "url": "https://example.com" }
```

No prices. No affiliate links unless a disclosure line is added on the page at the same time.

## What’s Next

Add a card to `cards` in `src/data/whats-next.json`: `id`, `status`, `title`, `text`. Don’t invent a project that isn’t real.

## Links and the contact address

Instagram, Facebook, the Some Tuesday links, and `hello@meghanfabulous.com` are in `src/config/site.ts`. Change them there once.

## Redirects

`public/_redirects` is copied into the Netlify publish folder. Specific paths go above the splats.
