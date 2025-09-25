# The following code is vulnerable to command injections because 
# it is using untrusted inputs to set up a new process. Therefore 
# an attacker can execute an arbitrary program that is installed 
# on the system.

def ping():
    host = request.args.get("host", "www.google.com")
    try:
        result = subprocess.run([
            "ping",
            "-c",
            "1",
            host
        ], capture_output=True, text=True, timeout=5)
        return str(result.returncode == 0)
    except subprocess.TimeoutExpired:
        return "timeout"
    except Exception as e:
        return f"error: {str(e)}"