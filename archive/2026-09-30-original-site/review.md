# meghanfabulous.com: honest review (30 Sep 2026)

**Archive:** `/workspace/meghanfabulous/archive-2026-09-30/`
- `site/`: 26 files, 1,814,456 bytes (1.73 MB). That's 2 HTML pages (`/` and the 404) plus 24 assets: the logo, the photo, 2 favicons, the og image, 1 CSS file, 2 JS files, and Google Fonts (1 CSS + 15 woff2).
- Also `content.md`, `inventory.md`, headers, rendered DOM and screenshots.
- **Nothing online was changed.**

## Bottom line
The current site is a well-built one-page **sailing farewell note**. It isn't a home for a 25-year designer. It says goodbye to a business and points everyone to Some Tuesday. It says almost nothing about Meghan's work, her prints, her press, or who she is. Meghan's dislike is justified: the site erases the very thing it's named after.

## What's wrong

### Content
- **No career at all.** No work, collections, lookbooks, press, celebrities, story, or "about".
- The only designer reference is "Thank you for 25 fabulous years!" and "close our business — my life's work".
- The 25-year story (LA Fashion Week 2004–06, Harrods, ASOS, Japan, QVC, Shakira in Bazaar, Grateful Dead Fabulous) is completely absent.
- **It reads as closing, not continuing.** The tone is "business closed", with no invitation to see what she makes now.

### Design
- **The visual identity is someone else's.**
  - A navy and gold nautical palette, sailboat silhouettes and a wave divider. That's yacht-club, not Meghan Fabulous.
  - It clashes with her colourful script logo and with the print, beading and bohemian language that is her signature.
  - The fonts (Cormorant Garamond and Raleway) are generic.

### Links and discovery
- **Every social link goes to Some Tuesday.** None go to Meghan.
  - @meghan_fabulous on Instagram (about 102K followers) and her Facebook page are missing.
  - There's no Substack, Patreon or newsletter link for Some Tuesday either, which is a missed halo.
- **Broken links from the outside world.**
  - The old Shopify URLs all 404 with no redirects: `/blogs/the-daily-fab/*`, `/pages/*`, `/collections/*`, `/products/*`.
  - This includes **`/blogs/the-daily-fab/sailing-into-the-next-chapter`**, which sometuesday.com's own About page links to, and posts Relix and other press link to.
  - The 404 page is a bare "Not Found" with no logo and no link home.
- **SEO is thin.**
  - One page, a generic title ("Meghan Fabulous"), and a meta description about sailing.
  - The og image is a 1200×630 auto-render with the logo caught mid-fade.
  - No sitemap, no robots.txt, and no structured data (Person, CreativeWork).
- **No contact, no signup, and no way to follow Meghan's making.**

### Technical
- It's fast, a single page, SSR, with no analytics.
- The favicon is a 1500×1500 JPEG of 270 KB. The 48×48 .ico exists but isn't linked.
- The route strip is **hard-coded** and already out of date: it doesn't show that they're in Tonga now.

## Facts to fix
- **Departure point.** The site says "cast off from Manhattan Beach, California", and the hero reads "Manhattan Beach → The World".
  - Manhattan Beach is their former home and the boat's hailing port.
  - **Use "Los Angeles"**, as Steve asked. For example: "On December 3, 2025 we cast off from Los Angeles…" and "Los Angeles → The World".
- **"25 years" is inconsistent with other sources:**
  - the brand's own "27 years";
  - the Daily Pilot (2003), which says Megan Noland Inc. was founded 1 Jan 2001;
  - a 2004 bio that says her first lines were "four years ago";
  - brand-start dates given variously as 2004 and 2005;
  - her age when she lost her name, given as "24" in one source and "27" in another.

  "25 years" is fine as a rounded 2001–2026 figure. Confirm the start year with Meghan.
- **meghanla.com**, her former main domain for 2011–2016, **now serves a third-party WordPress site**, "Meghan LA Dresses Official Website", modified 11 Sep 2026. Check who owns the domain and whether this is a trademark or impersonation issue ("Meghan Los Angeles®" is her mark).

## What to keep
- The logo.
- The warm tone of Meghan's first-person farewell.
- The Some Tuesday cross-links, moved into a gentle "What's next" section.
- The fast static SSR build and Netlify hosting.
- The DNS setup: GoDaddy nameservers, with **Google Workspace MX kept intact**.

## Useful sources
Open these individually. **None were bulk-downloaded.**

### Wayback snapshots
| Year | What | URL |
|---|---|---|
| 2004 | First meghanfabulous.com, S & M Fashion Group | https://web.archive.org/web/20041126/http://meghanfabulous.com/ |
| 2004 | Spring '05 runway lookbook slideshow (30 looks) | https://web.archive.org/web/20041206113225/http://meghanfabulous.com:80/Lookbookslide/springslide.html |
| 2004–05 | Press kit slides (35) | https://web.archive.org/web/2005/http://meghanfabulous.com/slides/meghanpresskit_Page_01.html |
| 2005 | Press / news articles (CA Apparel News text) / celebrities | https://web.archive.org/web/20050216121111/http://meghanfabulous.com:80/press.html · https://web.archive.org/web/20050220145405/http://meghanfabulous.com:80/news-articles.html · https://web.archive.org/web/20050215134936/http://meghanfabulous.com:80/celebrity.html |
| 2005 | meghannoland.com ("Meghan", Spring 2005 "Hollywood Hussy") | https://web.archive.org/web/2005*/meghannoland.com |
| 2005 | Collections SS05 "Hollywood Hussy", Fall 05 "Fashion Es Jesus" | https://web.archive.org/web/20050420102114/http://www.meghanfabulous.com:80/collectionss05.html · https://web.archive.org/web/20050420081829/http://www.meghanfabulous.com:80/collectionfall05.html |
| 2005–07 | Spring 06, Fall 06, Summer 06, Spring 07 collections | https://web.archive.org/web/20051126190857/http://www.meghanfabulous.com:80/collectionspring06.html · https://web.archive.org/web/20060527014345/http://www.meghanfabulous.com/collectionfall06.html · https://web.archive.org/web/20070323053919/http://www.meghanfabulous.com:80/collectionspring07.html |
| 2006 | Online stores list | https://web.archive.org/web/20060111075627/http://meghanfabulous.com:80/online_stores.html |
| 2008 | Celebrities | https://web.archive.org/web/20080828031048/http://www.meghanfabulous.com/celebrities.html |
| 2008–14 | MeghanShop.com (about 3,000 captures, peak 2010–12) | https://web.archive.org/web/2011*/meghanshop.com |
| 2010 | "Meghan by Meghan Fabulous" home | https://web.archive.org/web/20100516/http://meghanfabulous.com/ |
| 2011 | meghanla.com Editorials (about 142 clippings), Celebrities (about 84), Press | https://web.archive.org/web/20110116071323/http://meghanla.com/editorials.html · https://web.archive.org/web/20110113091416/http://meghanla.com/celebrities.html · https://web.archive.org/web/20110113091448/http://meghanla.com/press.html |
| 2010–12 | meghanla.com The Daily Fab blog (Japan, QVC, China production) | https://web.archive.org/web/2011*/meghanla.com/blog/* |
| 2014 | Press bio PDF | saved at `/workspace/growth/mf/wb/bio2014.pdf` |
| 2016 | Wix-era site: BOHEME, Meghan LA, Editorials, Media, Japan Love, Collections | https://web.archive.org/web/20160409154258/http://www.meghanfabulous.com:80/boheme.html · https://web.archive.org/web/20160519171709/http://www.meghanfabulous.com:80/editorials.html · https://web.archive.org/web/20160316133431/http://www.meghanfabulous.com:80/japan-love.html · https://web.archive.org/web/20160409155214/http://www.meghanfabulous.com:80/media.html |
| 2017–18 | Blog and lookbook (Wix) | https://web.archive.org/web/20170710175245/http://www.meghanfabulous.com/the-daily-fab.html · https://web.archive.org/web/20170729114058/http://www.meghanfabulous.com:80/lookbook.html |
| 2014–19 | meghanlosangeles.com | https://web.archive.org/web/2017*/meghanlosangeles.com |
| 2020 | Shopify: Press, Celebrities, Lookbook, Retailers | https://web.archive.org/web/20200930080309/https://www.meghanfabulous.com/pages/press · https://web.archive.org/web/20200929191656/https://www.meghanfabulous.com/pages/celebrities · https://web.archive.org/web/20200930175924/https://www.meghanfabulous.com/pages/lookbook · https://web.archive.org/web/20200808081406/https://www.meghanfabulous.com/pages/retailers |
| 2021–23 | bohemelosangeles.com | https://web.archive.org/web/2022*/bohemelosangeles.com |
| 2024 | Shopify: Stockists, Press, Celebrities | https://web.archive.org/web/20240229181650/https://www.meghanfabulous.com/pages/stockists · https://web.archive.org/web/20240415164715/https://www.meghanfabulous.com/pages/press-1 · https://web.archive.org/web/20240415164922/https://www.meghanfabulous.com/pages/celebrity-main |
| 2025 / 2026 | Last Shopify home / the new one-pager | https://web.archive.org/web/20250114185317/https://www.meghanfabulous.com/ · https://web.archive.org/web/20260125054622/https://www.meghanfabulous.com/ |

The Wayback Machine was only reachable through headless Chrome. It was slow and flaky, and some 2016 pages timed out.

### Other sources
- The **Blogspot Daily Fab** (2008–10, live): thedailyfab.blogspot.com, 34 posts, extracted.
- The **Shopify CDN** still serves the press and celebrity images; 32 are saved.
- **Steve's Shopify backups**: 91 posts, 65 pages.
- **The Dropbox image backup**: 598 files, 155 MB.
- The **@meghan_fabulous Instagram**. Logged out, only 12 posts are visible.

See `../press.md`, `../story-and-presentation.md` and `../photos/instagram/photos.md`.
