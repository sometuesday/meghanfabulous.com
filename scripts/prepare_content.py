#!/usr/bin/env python3
"""Build public images, journal markdown, look data, and redirects.

Run from the repo root. Does not copy excluded images or Paris Hilton photos.
"""
from __future__ import annotations

import json
import re
import shutil
import urllib.parse
from pathlib import Path

from PIL import Image

ROOT = Path("/workspace")
SCRATCH = Path("/tmp/mf-scratch")
PUBLIC = ROOT / "public" / "images"
JOURNAL_OUT = ROOT / "src" / "content" / "journal"
DATA = ROOT / "src" / "data"

PARIS_URL = "https://liveforlivemusic.com/features/touch-of-glam-meghan-fabulous-grateful-dead/"
SEE_PHOTO = (
    f"[See the photo]({PARIS_URL}) in James Sissler’s LiveForLiveMusic feature "
    "(25 July 2024). Photograph by Jeff Kravitz."
)
EVENT = "the VH1 Big in '04 Awards (December 2004, Shrine Auditorium, Los Angeles)"

PARIS_NAME = re.compile(
    r"paris|gettyimages|cover_image|img_946[4-9]|img_947[0-3]|untitled-design|"
    r"not_like_other|licensed_photo|parishilton",
    re.I,
)


def stem_key(name: str) -> str:
    name = urllib.parse.unquote(name).split("?")[0]
    name = Path(name).name.lower()
    name = re.sub(r"\.(jpg|jpeg|png|webp|gif|heic)$", "", name)
    name = re.sub(r"(_grande|_large|_2x|480x480|2x)$", "", name)
    return re.sub(r"[^a-z0-9]", "", name)


def to_webp(src: Path, dest: Path, max_edge: int = 1800) -> tuple[int, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src)
    im = im.convert("RGB")
    w, h = im.size
    scale = min(1.0, max_edge / max(w, h))
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    im.save(dest, "WEBP", quality=78, method=4)
    return im.size


def save_image(src: Path, rel: str) -> dict:
    rel = str(Path(rel).with_suffix(".webp"))
    dest = PUBLIC / rel
    w, h = to_webp(src, dest)
    return {"src": f"/images/{rel}", "w": w, "h": h}


def index_folder(folder: Path) -> dict[str, Path]:
    found = {}
    if not folder.exists():
        return found
    for p in folder.rglob("*"):
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
            continue
        found.setdefault(stem_key(p.name), p)
    return found


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    raw, body = m.group(1), text[m.end() :]
    data = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("-"):
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data, body


def strip_commerce(md: str) -> str:
    kept = []
    for line in md.splitlines():
        if re.search(r"\b(shop the|shop our|shop my|to shop the|add to cart|buy now)\b", line, re.I):
            continue
        kept.append(line)
    md = "\n".join(kept)

    def repl(match: re.Match) -> str:
        text, url = match.group(1), match.group(2)
        if re.search(r"myshopify|/products/|/collections/|/cart\b", url, re.I):
            if re.fullmatch(r"(here|shop|shop now)", text.strip(), re.I):
                return ""
            return text
        return match.group(0)

    md = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


def rewrite_images(body: str, folder: Path, title: str, allow) -> str:
    files = index_folder(folder)

    def repl(match: re.Match) -> str:
        alt, url = match.group(1), match.group(2)
        name = urllib.parse.unquote(url.split("?")[0])
        if not allow(name):
            return ""
        key = stem_key(name)
        src = files.get(key)
        if not src:
            # loose: key contained
            for k, p in files.items():
                if key and (key in k or k in key) and len(k) > 8:
                    src = p
                    break
        if not src:
            return ""
        info = save_image(src, f"journal/{folder.name}/{src.name}")
        use_alt = alt.strip() or f"Photograph from “{title}”"
        return f"![{use_alt}]({info['src']})"

    body = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def yaml_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_post(slug: str, title: str, date: str, author: str, description: str, original: str, body: str):
    JOURNAL_OUT.mkdir(parents=True, exist_ok=True)
    desc = re.sub(r"\s+", " ", description).strip()
    if len(desc) > 180:
        desc = desc[:177].rsplit(" ", 1)[0] + "…"
    path = original.replace("https://www.meghanfabulous.com", "")
    fm = [
        "---",
        f"title: {yaml_escape(title)}",
        f"date: {date}",
        f"author: {yaml_escape(author or 'Meghan Fabulous')}",
        f"description: {yaml_escape(desc)}",
        f"originalPath: {yaml_escape(path)}",
        "---",
        "",
    ]
    (JOURNAL_OUT / f"{slug}.md").write_text("\n".join(fm) + body.strip() + "\n", encoding="utf-8")
    return path, f"/journal/{slug}"


def first_text(body: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", body)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[#*_>`]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    # drop the h1 echo
    return text


def allow_normal(name: str) -> bool:
    return not PARIS_NAME.search(Path(name).name)


def allow_paris_post(name: str) -> bool:
    base = Path(urllib.parse.unquote(name)).name
    if PARIS_NAME.search(base):
        return False
    return "9480" in base


def allow_none(_name: str) -> bool:
    return False


SPECIAL_TITLES = {
    "2025-02-01-the-paris-hilton-grateful-dead-dress.md": "The Paris Hilton Grateful Dead dress",
    "2025-08-25-bts-behind-the-seams.md": "Behind the seams",
}


def edit_body(filename: str, body: str) -> str:
    body = body.lstrip()
    # drop the repeated h1; the template prints the title
    body = re.sub(r"^#\s+[^\n]+\n+", "", body, count=1)
    if filename == "2023-10-18-skin-cancer-journey.md":
        body = re.sub(r"^.*graphic photos.*\n+", "", body, flags=re.I)
        return body
    if filename == "2025-02-01-the-paris-hilton-grateful-dead-dress.md":
        body = re.sub(
            r"Then THEE moment happened\..*?That’s Hot Award\.”",
            "Then the moment happened. Paris wore my Grateful Dead dress to "
            + EVENT
            + ", to receive the “That’s Hot Award.”\n\n"
            + SEE_PHOTO,
            body,
            count=1,
            flags=re.S,
        )
        return body
    if filename == "2025-08-25-bts-behind-the-seams.md":
        body = re.sub(
            r"Fast forward to 2004, the moment that Paris Hilton wore my Grateful Dead Dress\.?",
            "In 2004, Paris Hilton wore my Grateful Dead dress to " + EVENT + ".",
            body,
            count=1,
        )
        if SEE_PHOTO not in body:
            body = body.rstrip() + "\n\n" + SEE_PHOTO + "\n"
        body = re.sub(r"To Shop the collection.*", "", body, flags=re.I)
        return body
    if filename == "2023-04-03-grateful-dead-fabulous-where-it-all-began.md":
        body = re.sub(
            r"and picture of Paris Hilton wearing my Grateful Dead Dress \(see next blog for that full story\) that I made in 2005\.",
            "and a picture of Paris Hilton in my Grateful Dead dress. She wore it to "
            + EVENT
            + ". The story is [The Paris Hilton Grateful Dead dress](/journal/the-paris-hilton-grateful-dead-dress). "
            + SEE_PHOTO,
            body,
            count=1,
        )
        return body
    if filename == "2021-03-25-the-meghan-design-process.md":
        body = body.replace(
            "And when you shop with us, you’re not buying from a big, faceless company.  You’re buying a quality designer garment that was conceived with love by Meghan herself and manufactured under her watchful eye.",
            "Nothing came from a faceless company. Each piece was conceived by Meghan and made under her eye.",
        )
        body = body.replace(
            "Many of our dresses are cut and sewn by our partners right here in Los Angeles, all of whom are small, family owned businesses that we consider our friends.",
            "Many of the dresses were cut and sewn in Los Angeles, in small family-owned workshops.",
        )
        body = body.replace(
            "The Meghan line offers extraordinary craftsmanship and includes finishing and details that are normally only found in dresses costing much more.  Our all-time best sellers like the LilyPad and the Jasmine are made with more than 7 yards of fabric - something that is simply unheard of with other dress makers at this price.",
            "The Meghan line was finished with a care usually reserved for much more elaborate clothes. The LilyPad and the Jasmine are each made with more than 7 yards of fabric.",
        )
        body = body.replace(
            "BOHEME is launching later this year and we already have interest and budding partnerships with some of the most prestigious specialty boutiques in the country and around the world.",
            "BOHEME, the luxury line, followed: silk, hand-beading, and custom embroidery.",
        )
        body = re.sub(
            r"### ON THE WAY TO YOUR CLOSET\n+The final step is to deliver.*",
            "The clothes went out to boutiques and department stores, and to the women who wrote to her. Meghan still answered many of them herself.\n",
            body,
            count=1,
            flags=re.S,
        )
        body = body.replace("Thank you so much for your business and for the love.  We love you right back.  Stay fabulous!", "")
        return body
    if filename == "2023-10-13-the-perseverance-of-meghan-fabulous-sparkle-never-hurt-anyone.md":
        return """This profile first appeared in *Palos Verdes Pulse* in 2023. Jennifer Boissavy wrote it after a visit to the El Segundo studio. What follows is a short excerpt. [Read the original](https://www.palosverdespulse.com/blog/meghanfabulous).

In her mid-twenties, feeling low after losing the right to use her legal name in commercial ventures, Meghan consoled herself on the beach, beading Grateful Dead T-shirts, which she turned into dresses. Someone said to her, “You can’t give up now, just change your name.” She took that sentiment to heart and thought to herself, “It would have to be something fabulous… it was like a lightening strike.” Meghan Fabulous was born.

Her mother taught her to hand-sew at four. The sewing machine came at six. They bonded through making clothes. Since her mother died, Meghan says, “Every time I see a butterfly, it makes me think of her.”

She loves turquoise because it reminds her of the ocean. “It’s my name on the door” is how she has put the standard she sews to. The profile’s studio photographs are below.
"""
    return body


def build_journal():
    if JOURNAL_OUT.exists():
        shutil.rmtree(JOURNAL_OUT)
    JOURNAL_OUT.mkdir(parents=True)
    redirects = []
    src_root = SCRATCH / "docs/docs/content/journal"
    groups = ["feature", "light-update"]
    for group in groups:
        for path in sorted((src_root / group).glob("*.md")):
            text = path.read_text(encoding="utf-8")
            meta, body = parse_front_matter(text)
            if "editorial_notes" in text and "editorial_notes" in meta:
                pass  # dropped by not copying the field
            filename = path.name
            title = meta.get("title", path.stem).replace("🧵", "").replace("📸😎💋💎", "").strip()
            title = SPECIAL_TITLES.get(filename, title)
            title = re.sub(r"\s+", " ", title).strip(" !")
            date = meta.get("date", "2020-01-01")[:10]
            author = meta.get("author", "Meghan Fabulous")
            slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
            slug = slug.replace("how-you-can-accessorize-for-a-photoshoot-fabulous-look", "sheen-magazine-photoshoot")
            if filename == "2023-10-18-skin-cancer-journey.md":
                allow = allow_none
            elif filename.startswith("2025-02-01"):
                allow = allow_paris_post
            elif filename.startswith("2025-08-25"):
                allow = allow_normal  # paris files are not in the folder; name filter still applies
            else:
                allow = allow_normal
            img_dir = SCRATCH / "images4/images/journal" / path.stem
            body = edit_body(filename, body)
            body = strip_commerce(body)
            body = rewrite_images(body, img_dir, title, allow)
            # thrifted tee alt
            body = body.replace(
                "](/images/journal/2025-02-01-the-paris-hilton-grateful-dead-dress/",
                "](/images/journal/2025-02-01-the-paris-hilton-grateful-dead-dress/",
            )
            body = re.sub(
                r"!\[[^\]]*\]\((/images/journal/2025-02-01[^)]*9480[^)]*)\)",
                r"![The thrifted Grateful Dead T-shirt Meghan kept for years, before it became a dress.](\1)",
                body,
            )
            desc = first_text(body)[:400]
            original = meta.get("original_url", "")
            old, new = write_post(slug, title, date, author, desc, original, body)
            if old:
                redirects.append((old, new))
    # press-source posts redirect to /press
    for path in (SCRATCH / "docs/docs/content/press-source-posts").glob("*.md"):
        meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
        original = meta.get("original_url", "")
        if original:
            redirects.append((original.replace("https://www.meghanfabulous.com", ""), "/press"))
    # condensed sources
    for path in (src_root / "gd-fabulous-condense").glob("*.md"):
        meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
        original = meta.get("original_url", "")
        if original:
            redirects.append((original.replace("https://www.meghanfabulous.com", ""), "/journal/grateful-dead-fabulous"))
    return redirects


def build_looks():
    picks = json.loads((SCRATCH / "docs/docs/photos/_picks.json").read_text())
    alts = {}
    for pick in picks:
        alts[Path(pick["orig"]).name.lower()] = pick["shows"]
    image_map = json.loads((SCRATCH / "images1/images/_image-map.json").read_text())
    names = {
        "boho-bourbon": "Boho Bourbon",
        "california-girl": "California Girl",
        "disco-doll": "Disco Doll",
        "jade-princess": "Jade Princess",
        "la-cita": "La Cita",
        "lady-jamaica": "Lady Jamaica",
        "novel-riviere": "Novel Riviere",
        "prism-butterfly": "Prism Butterfly",
        "rebel-rebel": "Rebel Rebel",
        "rosie": "Rosie",
        "starlight": "Starlight",
        "after-party": "After Party",
        "bf-4-ever": "BF 4 Ever",
        "bella-bijou": "Bella Bijou",
        "lola": "Lola",
    }
    runway = {"disco-doll", "rebel-rebel", "starlight", "after-party", "bella-bijou", "rosie", "lola"}
    looks = []
    for slug, frames in image_map["lookbooks"].items():
        out_frames = []
        for i, frame in enumerate(frames, start=1):
            src = SCRATCH / "images2" / frame["file"]
            if not src.exists():
                continue
            info = save_image(src, f"lookbooks/{slug}/{Path(frame['file']).name}")
            alt = alts.get(Path(frame["orig"]).name.lower()) or f"A look from the {names[slug]} lookbook."
            out_frames.append({**info, "alt": alt})
        cover = out_frames[0]["src"] if out_frames else ""
        looks.append(
            {
                "slug": slug,
                "name": names[slug],
                "archetype": names[slug],
                "era": "the-runway-years" if slug in runway else "the-world",
                "cover": cover,
                "frames": out_frames,
            }
        )
    (DATA / "looks.json").write_text(json.dumps(looks, indent=2), encoding="utf-8")
    return looks


def copy_named(src_root: Path, rel: str, dest_rel: str):
    src = src_root / rel
    if not src.exists():
        raise SystemExit(f"missing {src}")
    return save_image(src, dest_rel)


def build_supporting():
    picks_dir = SCRATCH / "images1/images/picks"
    manifest = {}
    for p in sorted(picks_dir.iterdir()):
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        manifest[p.stem.split("_", 1)[0]] = save_image(p, f"picks/{p.name}") | {"file": p.name}
    # gd campaign
    gd = []
    gd_dir = SCRATCH / "images4/images/gd-fabulous-campaign-2024"
    for p in sorted(gd_dir.iterdir()):
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        info = save_image(p, f"gd-campaign/{p.name}")
        info["alt"] = "Grateful Dead Fabulous campaign photograph, 2024."
        gd.append(info)
    # brand photos, no claims
    brand = []
    for p in sorted((SCRATCH / "images4/images/brand-photos").iterdir()):
        info = save_image(p, f"brand/{p.name}")
        info["alt"] = "A photograph from the Meghan Fabulous studio archive."
        brand.append(info)
    # about page portraits
    pages = []
    for p in (SCRATCH / "images4/images/pages").rglob("*"):
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        rel = p.relative_to(SCRATCH / "images4/images/pages")
        info = save_image(p, f"pages/{rel}")
        info["alt"] = "Meghan Fabulous in the studio."
        pages.append(info)
    # press scans we may reference by original relative path
    press_src = SCRATCH / "images3/images/press-scans"
    press_out = {}
    for p in press_src.rglob("*"):
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        rel = p.relative_to(press_src).as_posix()
        info = save_image(p, f"press/{rel}")
        press_out[rel] = info
    (DATA / "image-manifest.json").write_text(
        json.dumps({"picks": manifest, "gd": gd, "brand": brand, "pages": pages, "press": press_out}, indent=2),
        encoding="utf-8",
    )
    # favicon + apple touch + og
    logo = Image.open(SCRATCH / "images1/images/logo/meghan-fabulous-logo.png").convert("RGBA")
    ico_src = SCRATCH / "images1/images/logo/favicon.ico"
    shutil.copy(ico_src, ROOT / "public/favicon.ico")
    icon = Image.new("RGB", (180, 180), (251, 248, 242))
    lw, lh = logo.size
    scale = min(150 / lw, 80 / lh)
    logo_r = logo.resize((int(lw * scale), int(lh * scale)), Image.Resampling.LANCZOS)
    # paste using alpha
    x = (180 - logo_r.size[0]) // 2
    y = (180 - logo_r.size[1]) // 2
    icon.paste(logo_r, (x, y), logo_r)
    icon.save(ROOT / "public/apple-touch-icon.png", "PNG")
    # og from hero pick, real photo, no type on top of a face: wide crop of the gown's mid band is risky.
    # Place the portrait on ivory so the whole figure remains, uncropped through the face.
    hero = Image.open(next(picks_dir.glob("01_*"))).convert("RGB")
    og = Image.new("RGB", (1200, 630), (251, 248, 242))
    hw, hh = hero.size
    scale = 630 / hh
    hero_r = hero.resize((int(hw * scale), 630), Image.Resampling.LANCZOS)
    og.paste(hero_r, ((1200 - hero_r.size[0]) // 2, 0))
    og.save(ROOT / "public/og.jpg", "JPEG", quality=82)
    return manifest


def main():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    DATA.mkdir(parents=True, exist_ok=True)
    # logo
    save_image(SCRATCH / "images1/images/logo/meghan-fabulous-logo.png", "logo/meghan-fabulous-logo.png")
    redirects = build_journal()
    build_looks()
    build_supporting()
    lines = ["# Generated redirects. Specific stories before the splat.", ""]
    # specific first
    for old, new in sorted(redirects, key=lambda x: len(x[0]), reverse=True):
        if old and old != new:
            lines.append(f"{old}  {new}  301")
    (DATA / "story-redirects.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("journal", len(list(JOURNAL_OUT.glob('*.md'))))
    print("redirects", len(redirects))
    print("images", sum(1 for _ in PUBLIC.rglob('*.webp')))


if __name__ == "__main__":
    main()
