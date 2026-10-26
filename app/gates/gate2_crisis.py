import re
from app.config import SOS_SINGAPORE

_PATTERNS = [
    r"\bsuicid",
    r"\bkill myself\b",
    r"\bend my life\b",
    r"\bdon.t want to live\b",
    r"\bcan.t go on\b",
    r"\bno reason to live\b",
    r"\bwant to die\b",
    r"\bwish i.?m? dead\b",
    r"\bhurt myself\b",
]

_compiled = [re.compile(p, re.IGNORECASE) for p in _PATTERNS]


def check_crisis(text: str) -> dict | None:
    for pattern in _compiled:
        if pattern.search(text):
            return {
                "triggered": True,
                "message": (
                    "I hear how much pain you're in right now. "
                    "Please reach out to SOS Singapore — they are available 24 hours a day: "
                    f"{SOS_SINGAPORE}. You don't have to face this alone."
                ),
                "hotline": SOS_SINGAPORE,
            }
    return None
