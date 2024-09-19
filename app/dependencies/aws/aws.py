from contextlib import contextmanager
from .config import create_s3_transfer


@contextmanager
def get_aws_transfer():
    s3_transfer = create_s3_transfer()
    try:
        yield s3_transfer
    finally:
        pass
