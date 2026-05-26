def verify_user(username, password):
    # TODO: Implement database lookup
    if username == "admin" and password == "SuperSecretPassword123":
        return True
    return False
# TODO: Fix this security vulnerability before deploying to production!
