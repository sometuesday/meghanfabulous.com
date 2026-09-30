# meghanfabulous.com: full content capture
Captured 30 Sep 2026, 17:26 Tonga time (UTC+13), from https://www.meghanfabulous.com/ (Netlify; TanStack Start/React SSR build).
The site has **one page** (`/`). Every other path returns the 404 page described at the end of this file. The server-rendered HTML and the headless-Chrome render produce the same visible text (1,374 characters after whitespace normalisation), so no text on the site is client-only.

Files: `site/index.html` (served HTML), `rendered-dom-index.html` (DOM after JS), `screenshot-desktop-1440.png`, `screenshot-mobile-390.png`.

---
## Page: Home (`/`)
- **`<title>`:** Meghan Fabulous
- **Meta description:** Thank you for 25 fabulous years! Follow our sailing journey around the world.
- **og:image:** https://www.meghanfabulous.com/.netlify/og-image/862157d5681f61cc2839e97cdde9338e.jpg (1200×630; a Netlify-generated screenshot of the hero with the logo caught half-faded mid-animation). There's no og:title, og:description, twitter:card or canonical link.
- **Favicon:** `/favicon.jpg` (1500×1500 JPEG, "MF" monogram in print-filled letters on black). `/favicon.ico` (48×48) also exists but isn't linked.
- **Language:** `en`

### 1. Hero (full viewport, navy-to-teal ocean gradient, faint sailboat silhouette SVG, wave divider)
- Eyebrow: **A New Adventure Begins**
- Image: `/meghan-fabulous-logo.png`, alt "Meghan Fabulous" (the print-filled "MEGHAN FABULOUS®" wordmark, 640×335). Preloaded.
- Subtitle: **Manhattan Beach → The World** (rendered with double spaces around the arrow)
- Scroll cue: animated line + **Scroll**

### 2. Story (cream background)
- Heading (h2): **Thank you for *25 fabulous years!*** ("25 fabulous years!" in italic)
- Paragraph 1: "Steve and I have made the very difficult decision to close our business — my life's work and dream since childhood — in order to follow a new dream: sailing around the world."
- Paragraph 2: "On December 3, 2025 we cast off from Manhattan Beach, California with a plan to circumnavigate the Earth over five years. We sailed south through Mexico to El Salvador, then crossed the Pacific Ocean in April, 2026. We spent 28 days at sea before landing in the Marquesas Islands."
- Image: `/steve-and-meg.jpg`, alt "Steve and Meg" (1290×1612 portrait: Meghan in a turquoise printed maxi dress and white sunglasses and Steve in a matching print shirt, both in green leis, on a boat bow among sailboats). Sits between paragraphs 2 and 3. Preloaded.
- Paragraph 3: "We'll explore the South Pacific through 2027, and then sail on to Australia and New Zealand, across the Indian Ocean and into the Mediterranean for a year or more. Next we'll cross the Atlantic to spend 2029 in the Caribbean and finally return home via the Panama Canal in 2030."
- Ornament (line, diamond, line)
- Italic teal line: **Follow our Journey! Links below!**

### 3. Route strip (navy background)
Label: **The Route — 2025 to 2030**. Eight stops on a horizontal line (a filled gold dot means completed):
| # | Stop | Date | Dot |
|---|---|---|---|
| 1 | Manhattan Beach | Dec 2025 | filled |
| 2 | Mexico & El Salvador | Jan–Mar 2026 | filled |
| 3 | Marquesas Islands | Apr 2026 | filled |
| 4 | South Pacific | 2026–2027 | open |
| 5 | Australia & New Zealand | 2027–2028 | open |
| 6 | Indian Ocean / Mediterranean | 2028–2029 | open |
| 7 | Caribbean | 2029 | open |
| 8 | Panama Canal / Home | 2030 | open |
(These are hard-coded. Tonga, where they are now, isn't marked.)

### 4. Social links (cream background)
Label: **Follow the Journey** · Heading: **Find Us Online**. Six cards in a grid. Each card has an icon, a name, a handle and an arrow, and opens in a new tab.
| Card | Handle shown | URL |
|---|---|---|
| Some Tuesday | sometuesday.com | https://sometuesday.com |
| YouTube | @SailingSomeTuesday | https://www.youtube.com/@SailingSomeTuesday |
| Instagram | @SailingSomeTuesday | https://www.instagram.com/SailingSomeTuesday |
| Facebook | SomeTuesday | https://www.facebook.com/SomeTuesday/ |
| PredictWind Tracking | SV Some Tuesday | https://www.predictwind.com/tracking/SV-SomeTuesday |
| TikTok | @sailingsometuesday | https://www.tiktok.com/@sailingsometuesday |

### 5. Footer (navy)
- Image: `/meghan-fabulous-logo.png`, alt "Meghan Fabulous" (smaller)
- Note: **Sailing Some Tuesday · Around the World 2025–2030**

---
## 404 page (any other path, e.g. `/about`, `/products`, `/blogs/the-daily-fab/...`)
Same `<head>` as the home page (title "Meghan Fabulous", same description and og:image). Body text: **Not Found**. There's no styling, no logo and no link home. Saved as `site/404.html`.

## Image reference summary
| File | Alt text | Where it appears |
|---|---|---|
| /meghan-fabulous-logo.png | Meghan Fabulous | Hero (large) and footer (small) |
| /steve-and-meg.jpg | Steve and Meg | Story section, between paragraphs 2 and 3 |
| /favicon.jpg | (icon) | Browser tab |
| /.netlify/og-image/862157d5….jpg | (meta) | Social share previews |
| inline SVGs | none | Sailboat silhouette, wave divider, 6 social icons, arrows, ornament |
