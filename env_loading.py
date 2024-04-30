import os
from dotenv import load_dotenv
load_dotenv()


def load_env_variable(key):
    try:
        return os.getenv(key)
    except Exception:
        raise OSError(f"'{key}' environment variable must be specified")
