import os
from dotenv import load_dotenv

load_dotenv()

MODEL_BASE_URL = os.getenv("MODEL_BASE_URL", "https://api.meta.ai/v1")
MODEL_ID = os.getenv("MODEL_ID", "muse-spark-1.3")

SOURCETRUTH_API_KEY = os.getenv("SOURCETRUTH_API_KEY", "")
SOURCETRUTH_API_URL = os.getenv("SOURCETRUTH_API_URL", "https://api.sourcetruth.io/v1")

MODAL_ENDPOINT_URL = os.getenv("MODAL_ENDPOINT_URL", "")

SOS_SINGAPORE = "1800-221-4444"
