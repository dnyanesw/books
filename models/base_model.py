import datetime

from db import db


class BaseModel:
    def __init__(self):
        self.id = None
        self.deleted_at = None

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return str(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        # db.session.commit()
        try:
            db.session.commit()
        except:
            db.session.rollback()

    # Soft delete
    def delete_from_db(self) -> None:
        self.deleted_at = datetime.datetime.now()
        db.session.add(self)
        # db.session.commit()
        try:
            db.session.commit()
        except:
            db.session.rollback()

    # Soft delete
    def hard_delete_from_db(self) -> None:
        db.session.delete(self)
        # db.session.commit()
        try:
            db.session.commit()
        except:
            db.session.rollback()
