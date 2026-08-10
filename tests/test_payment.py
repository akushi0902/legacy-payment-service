from payment import process_payment


def test_successful_payment():
    result = process_payment(
        user_id="user-001",
        amount=100,
        card_number="4111111111111111"
    )

    assert result["status"] == "success"


def test_invalid_amount():
    result = process_payment(
        user_id="user-001",
        amount=-10,
        card_number="4111111111111111"
    )

    assert result["status"] == "failed"
