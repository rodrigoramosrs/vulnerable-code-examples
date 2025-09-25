# The following code is vulnerable to arbitrary code execution because it runs dynamic Python code based on untrusted data.

from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    if operation == "multiply":
        product_multiply()
    elif operation == "add":
        product_add()
    else:
        return "Invalid operation"
    return "OK"