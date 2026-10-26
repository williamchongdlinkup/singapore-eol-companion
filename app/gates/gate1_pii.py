"""Gate 1 — PII screening. Strip or redact personal identifiers before logging."""
import re

_NRIC = re.compile(r"\b[STFG]\d{7}[A-Z]\b")
_PHONE = re.compile(r"\b[689]\d{7}\b")


def screen(text: str) -> str:
    text = _NRIC.sub("[NRIC REDACTED]", text)
    text = _PHONE.sub("[PHONE REDACTED]", text)
    return text
