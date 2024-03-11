from . import db
from .models import Transaction
from datetime import datetime

def seed_database():
    # Create some sample transactions
    transactions = [
        Transaction(amount=20, spent=False, created_at=datetime.utcnow()),
        Transaction(amount=10, spent=True, created_at=datetime.utcnow()),
        Transaction(amount=30, spent=False, created_at=datetime.utcnow())
    ]

    # Add transactions to the session and commit
    for transaction in transactions:
        db.session.add(transaction)
    db.session.commit()

    print("Database seeded with sample transactions.")