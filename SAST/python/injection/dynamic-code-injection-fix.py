# Fixed version: removed eval and replaced with safe mapping
from flask import request, abort

@app.route("/")
def example():
    operation = request.args.get("operation")
    # Define allowed operations
    allowed_ops = {
        "add": product_add,
        "subtract": product_subtract,
    }
    func = allowed_ops.get(operation)
    if not func:
        abort(400, description="Invalid operation")
    func()
    return "OK"
