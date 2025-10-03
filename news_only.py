import json
import re
from collections import deque

import httpx
from bs4 import BeautifulSoup

from src.ingestion.page_configurations import headers
import re

import json
from collections import deque

import json
from collections import deque
from bs4 import BeautifulSoup

def extract_related_capabilities_from_next(soup: BeautifulSoup):
    script = soup.find("script", id="__NEXT_DATA__", type="application/json")
    if not script or not script.string:
        return []

    data = json.loads(script.string)

    def to_str(v):
        """Return a best-effort string from arbitrary JSON shapes."""
        if isinstance(v, str):
            return v
        if isinstance(v, dict):
            for k in ("value", "text", "label", "name", "title"):
                if isinstance(v.get(k), str):
                    return v[k]
        if isinstance(v, list):
            # sometimes it’s like ["Related","capabilities"]
            parts = [x for x in v if isinstance(x, str)]
            if parts:
                return " ".join(parts)
        return ""

    candidates = []

    def add_item(item):
        """Normalize a dict-ish link into (text, href)."""
        if not isinstance(item, dict):
            return
        href = item.get("href") or item.get("url")
        text = to_str(item.get("text") or item.get("title") or item.get("label") or item.get("name"))
        if href and text:
            candidates.append((text.strip(), href))

    # Targeted DFS: look for a block titled "Related capabilities" and harvest common list keys.
    def walk(node):
        if isinstance(node, dict):
            title = to_str(node.get("title") or node.get("header") or node.get("heading")).strip().lower()
            if title == "related capabilities":
                for key in ("items", "links", "tags", "capabilities", "related", "children"):
                    val = node.get(key)
                    if isinstance(val, list):
                        for it in val:
                            add_item(it)
            # keep traversing
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)

    # Fallback: generic BFS scanning for any list of dicts that look like links
    if not candidates:
        q = deque([data])
        while q:
            node = q.popleft()
            if isinstance(node, dict):
                for v in node.values():
                    q.append(v)
                for v in node.values():
                    if isinstance(v, list) and any(isinstance(x, dict) for x in v):
                        for it in v:
                            add_item(it)
            elif isinstance(node, list):
                q.extend(node)

    # Dedupe + shape result
    seen = set()
    result = []
    for text, href in candidates:
        print(text, href)
    return result




def extract_article(soup: BeautifulSoup):
    text_locator = soup.select_one("div.Grid_grid__item__Itq8w:has(div[class^='StandFirst_'])")
    if not text_locator:
        text_locator = soup.select_one("div.Grid_grid__item__Itq8w:has(div[class^='RichText_richtext_'])")
    return text_locator



with httpx.Client() as client:
    r=client.get(url='https://www.aoshearman.com/en/news/cdp-financial-eur1-billion-senior-notes-offering',
               headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    text_locator=extract_article(soup)
    text = text_locator.text.strip()
    capacity=extract_related_capabilities_from_next(soup)
    print(capacity)
