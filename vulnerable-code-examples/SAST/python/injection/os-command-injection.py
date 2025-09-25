# The following code is vulnerable to command injections because 
# it is using untrusted inputs to set up a new process. Therefore 
# an attacker can execute an arbitrary program that is installed 
# on the system.

def ping():
    host = request.args.get("host", "www.google.com")
    cmd = ["ping", "-c", "1", host]
    status = subprocess.run(cmd, capture_output=True).returncode # Compliant
    return str(status == 0)