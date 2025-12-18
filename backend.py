from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_URL = "http://apilayer.net/api/live"
ACCESS_KEY = "220e0f99e8f49664daa4e027a455f265"

@app.route("/convert", methods=["POST"])
def convert():

    data = request.get_json()
    from_currency = data.get("from", "").upper()
    to_currency   = data.get("to", "").upper()
    amount_str    = data.get("amount", "0")

    try:
        amount = float(amount_str)
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    params = {
        "access_key": ACCESS_KEY,
        "currencies": f"{from_currency},{to_currency}",
        "source": "USD",
        "format": 1
    }

    response = requests.get(API_URL, params=params)
    result_json = response.json()
    print("Currencylayer response:", result_json)

    if not result_json.get("success", False):
        print("API ERROR:", result_json)
        return jsonify({"error": result_json}), 400


    quotes = result_json.get("quotes", {})

    try:
        rate_from = quotes["USD" + from_currency] if from_currency != "USD" else 1
        rate_to   = quotes["USD" + to_currency]   if to_currency   != "USD" else 1
        conversion_rate = rate_to / rate_from
        result = round(amount * conversion_rate, 4)
    except KeyError:
        return jsonify({"error": "Currency not supported"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
