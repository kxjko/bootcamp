import os

MILVUS_HOST = os.getenv("MILVUS_HOST", "127.0.0.1")
MILVUS_PORT = os.getenv("MILVUS_PORT", 19530)
VECTOR_DIMENSION = os.getenv("VECTOR_DIMENSION", 2048)
DATA_PATH = os.getenv("DATA_PATH", "tmp/pictures")
DEFAULT_TABLE = os.getenv("DEFAULT_TABLE", "milvus_img_search")
UPLOAD_PATH = "tmp/search-images"
DEFAULT_CACHE_DIR = "./tmp"
