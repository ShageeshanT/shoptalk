from __future__ import annotations

def tag_normalizer(tags: list[str]) -> list[str]:
    seen=set(); out=[]
    for tag in tags:
        clean=tag.strip().lower().replace(" ", "_")
        if clean and clean not in seen:
            seen.add(clean); out.append(clean)
    return out