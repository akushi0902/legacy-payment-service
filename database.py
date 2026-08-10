import sqlite3
import uuid
from datetime import datetime

DATABASE = "payments.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL,
            card_number TEXT,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_payment(payment):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO payments
        (id, user_id, amount, status, card_number, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            payment["id"],
            payment["user_id"],
            payment["amount"],
            payment["status"],
            payment["card_number"],
            payment["created_at"]
        )
    )

    connection.commit()
    connection.close()


def get_payment(payment_id):
    connection = get_connection()

    result = connection.execute(
        "SELECT * FROM payments WHERE id = ?",
        (payment_id,)
    ).fetchone()

    connection.close()

    if result:
        return dict(result)

    return None


initialize_database()
