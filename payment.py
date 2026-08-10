import uuid
from datetime import datetime

from config import PAYMENT_PROVIDER, PAYMENT_TIMEOUT


def process_payment(user_id, amount, card_number):

    print("Using payment provider:", PAYMENT_PROVIDER)
    print("Payment timeout:", PAYMENT_TIMEOUT)

    if amount <= 0:
        return {
            "status": "failed",
            "message": "Amount must be greater than zero"
        }

    if len(card_number) < 12:
        return {
            "status": "failed",
            "message": "Invalid card number"
        }

    payment_id = str(uuid.uuid4())

    # Simulating communication with an external payment provider.
    payment_status = "success"

    return {
        "id": payment_id,
        "user_id": user_id,
        "amount": amount,
        "status": payment_status,
        "card_number": card_number,
        "created_at": datetime.utcnow().isoformat()
    }
