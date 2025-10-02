from .app import create_app
from .extension import db

app = create_app()

__all__ = ["app", "db"]