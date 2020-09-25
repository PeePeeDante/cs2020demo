import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluateSecretMessage(): # cannot have same method name 
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"],test_case["text"]))

    logging.info("My result: {}".format(result))
    return jsonify(result)

def encrypt(n, text):
    result = ""
    processed = ""

    for ch in text:
        if ch.isalnum():
            processed += ch

    c_len = len(processed)

    if (c_len < n):
        return processed.upper()

    cipher = [None]*c_len
    for i in range(c_len):
        cipher[i*n % c_len] = processed[i]

    result = "".join(cipher)
    return result.upper()


