#!/usr/bin/env python3
"""
Batch download posters from typographicposters.com archive.

Source:
  - https://www.typographicposters.com/archive
  - https://www.typographicposters.com/api/tg/posters-recent?page=N&itemsPerPage=M

What it does:
  1. Pulls paginated archive poster metadata from the public API.
  2. Downloads poster images from the CDN.
  3. Saves a JSONL manifest alongside the images.

This is meant for personal reference / inspiration libraries.
Respect copyright and usage rights for any images you store locally.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


ARCHIVE_API = "https://www.typographicposters.com/api/tg/posters-recent"
IMAGE_CDN = "https://images.typographicposters.com"


def http_get_json(url: str, timeout: int = 30) -> Dict[str, Any]:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_download(url: str, dest: Path, timeout: int = 60) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=timeout) as resp, dest.open("wb") as f:
        f.write(resp.read())


def slugify(text: str, fallback: str = "poster") -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text, flags=re.UNICODE)
    text = text.strip("-")
    return text or fallback


def build_image_url(image_path: str, variant: str = "poster") -> str:
    if not image_path:
        raise ValueError("missing image path")
    base = image_path.lstrip("/").rsplit(".", 1)[0] + ".jpg"
    return urljoin(IMAGE_CDN, f"{variant}/{base}")


@dataclass
class DownloadedPoster:
    id: str
    title: str
    year: Optional[int]
    profile_name: Optional[str]
    profile_id: Optional[str]
    image_url: str
    local_path: str


def fetch_page(page: int, items_per_page: int) -> Dict[str, Any]:
    params = urlencode({"page": page, "itemsPerPage": items_per_page})
    url = f"{ARCHIVE_API}?{params}"
    return http_get_json(url)


def iterate_hits(items_per_page: int, max_items: Optional[int], sleep_s: float) -> Iterable[Dict[str, Any]]:
    page = 0
    seen = 0
    total = None

    while True:
        payload = fetch_page(page, items_per_page)
        hits = payload.get("hits", [])
        if total is None:
            total = payload.get("total")

        if not hits:
            break

        for hit in hits:
            yield hit
            seen += 1
            if max_items and seen >= max_items:
                return

        if total is not None and seen >= total:
            return

        page += 1
        if sleep_s > 0:
            time.sleep(sleep_s)


def download_posters(
    output_dir: Path,
    items_per_page: int,
    max_items: Optional[int],
    sleep_s: float,
    variant: str,
    download_manifest: bool = True,
) -> List[DownloadedPoster]:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "manifest.jsonl"
    downloaded: List[DownloadedPoster] = []

    with manifest_path.open("a", encoding="utf-8") as mf:
        for hit in iterate_hits(items_per_page=items_per_page, max_items=max_items, sleep_s=sleep_s):
            poster_id = str(hit.get("id") or hit.get("objectID") or "")
            title = str(hit.get("title") or "poster")
            profile_name = hit.get("profileName")
            profile_id = hit.get("profileId")
            year = hit.get("year")
            image = hit.get("image") or {}
            image_path = image.get("path")

            if not image_path:
                continue

            ext = ".jpg"
            year_dir = output_dir / (str(year) if year else "unknown-year")
            profile_dir = year_dir / slugify(profile_id or profile_name or "unknown-profile")
            filename = f"{slugify(title)}-{poster_id}{ext}"
            local_path = profile_dir / filename

            image_url = build_image_url(image_path, variant=variant)
            if not local_path.exists():
                try:
                    http_download(image_url, local_path)
                except (HTTPError, URLError, TimeoutError) as e:
                    print(f"[skip] {title} ({poster_id}) -> {e}", file=sys.stderr)
                    continue

            record = DownloadedPoster(
                id=poster_id,
                title=title,
                year=year if isinstance(year, int) else None,
                profile_name=profile_name,
                profile_id=profile_id,
                image_url=image_url,
                local_path=str(local_path.relative_to(output_dir.parent)),
            )
            downloaded.append(record)

            if download_manifest:
                mf.write(json.dumps(record.__dict__, ensure_ascii=False) + "\n")

            print(f"[ok] {record.local_path}")

    return downloaded


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download typographic posters archive images into a local Banners library."
    )
    parser.add_argument(
        "--output",
        default="90_Meta/Banners/Typographic Posters Archive",
        help="Output directory for downloaded posters (default: %(default)s)",
    )
    parser.add_argument(
        "--items-per-page",
        type=int,
        default=100,
        help="Number of posters to request per page (default: %(default)s)",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=200,
        help="Maximum number of posters to download (default: %(default)s). Use 0 for no cap.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.2,
        help="Sleep seconds between page requests (default: %(default)s)",
    )
    parser.add_argument(
        "--variant",
        choices=["poster", "thumb", "search", "search-mobile"],
        default="poster",
        help="CDN rendition to download (default: %(default)s)",
    )
    parser.add_argument(
        "--no-manifest",
        action="store_true",
        help="Do not write manifest.jsonl",
    )
    args = parser.parse_args()

    max_items = None if args.max_items == 0 else args.max_items
    output_dir = Path(args.output)
    download_posters(
        output_dir=output_dir,
        items_per_page=args.items_per_page,
        max_items=max_items,
        sleep_s=args.sleep,
        variant=args.variant,
        download_manifest=not args.no_manifest,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
