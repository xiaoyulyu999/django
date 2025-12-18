
if IN_DOCKER: # type: ignore
    print("In Docker")

    assert MIDDLEWARE[:1] == [ # type: ignore
    'django.middleware.security.SecurityMiddleware']