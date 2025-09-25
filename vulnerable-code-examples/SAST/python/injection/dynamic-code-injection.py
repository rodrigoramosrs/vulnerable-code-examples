# The following code is vulnerable to arbitrary code execution because it runs dynamic Python code based on untrusted data.

from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    # Fixed: Use safe alternative instead of eval()
    if not operation:
        return "Operation is required"
    
    allowed_operations = {"add", "multiply"}
    if operation not in allowed_operations:
        return "Invalid operation. Only 'add' or 'multiply' are allowed.", 400
    
    # Safe execution using safe function lookup
    operations_map = {
        "add": lambda a, b: a + b,
        "multiply": lambda a, b: a * b
    }
    
    try:
        result = operations_map[operation](10, 5)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}", 500