from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

MAX_FILE_SIZE = 50 * 1024 * 1024
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100