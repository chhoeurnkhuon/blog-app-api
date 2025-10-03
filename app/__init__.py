from .app import create_app
from .extension import db
from .get_user import current_user_id
from .role_required import role_required

app = create_app()

__all__ = ["app", "db", "current_user_id", "role_required"]