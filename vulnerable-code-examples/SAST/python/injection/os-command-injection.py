import subprocess

def ping():
    host = request.args.get("host", "www.google.com")
    try:
        result = subprocess.run([
            "ping",
            "-c",
            "1",
            host
        ], capture_output=True, text=True)
        return str(result.returncode == 0)
    except Exception as e:
        return f"Erro: {str(e)}"