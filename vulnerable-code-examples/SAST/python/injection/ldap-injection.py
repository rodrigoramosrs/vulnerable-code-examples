# The following noncompliant code is vulnerable 
# to LDAP injection because untrusted data is 
# concatenated to an LDAP query without prior 
# sanitization or validation.

from flask import request
import ldap

@app.route("/user")
def user():
    username = request.args.get('username', '')
    if not username:
        return "Username is required"
    
    # Sanitized filter using proper LDAP escaping
    escaped_username = ldap.filter.escape_filter_value(username)
    search_filter = f"(&(objectClass=user)(uid={escaped_username}))"
    
    try:
        ldap_connection = ldap.initialize("ldap://localhost:389")
        user = ldap_connection.search_s("dc=example,dc=org", ldap.SCOPE_SUBTREE, search_filter)
        return user[0] if user else "User not found"
    except Exception as e:
        return f"Error: {str(e)}"