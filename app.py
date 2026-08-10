from flask import Flask, request, jsonify
from database import get_payment, save_payment
from payment import process_payment

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Legacy Payment Service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/payments", methods=["POST"])
def create_payment():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    user_id = data.get("user_id")
    amount = data.get("amount")
    card_number = data.get("card_number")

    if not user_id or not amount or not card_number:
        return jsonify({
            "error": "user_id, amount and card_number are required"
        }), 400

    result = process_payment(
        user_id=user_id,
        amount=amount,
        card_number=card_number
    )

    save_payment(result)

    return jsonify(result), 201


@app.route("/payments/<payment_id>", methods=["GET"])
def get_payment_details(payment_id):
    payment = get_payment(payment_id)

    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    return jsonify(payment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
