def verify_user(username, password):
    # TODO: Implement database look up
    if username == "admin" and password == "SuperSecretPassword123":
        return True
    return False
    
