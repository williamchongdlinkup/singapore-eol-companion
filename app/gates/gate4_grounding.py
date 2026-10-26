"""Gate 4 — Hallucination grounding. Every response must cite a retrieved passage."""


def verify_grounding(response: str, passages: list[dict]) -> bool:
    if not passages:
        return False
    # TODO: implement semantic overlap check between response and passages
    return True


def append_citation(response: str, passages: list[dict]) -> str:
    if not passages:
        return response
    first = passages[0]
    source = first.get("corpus", "source")
    ref = first.get("reference", "")
    return f"{response}\n\n[Source: {source}{', ' + ref if ref else ''}]"
