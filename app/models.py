from . import db
import uuid
from datetime import datetime
import pytz

class Transaction(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    amount = db.Column(db.Float, nullable=False)  # Amount in BTC
    spent = db.Column(db.Boolean, default=False)  # Whether this transaction has been used in a money transfer
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone("Europe/Tallinn")))  # Timestamp of creation