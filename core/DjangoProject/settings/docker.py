if IN_DOCKER:  # type: ignore
    print("In Docker")

    assert MIDDLEWARE[0] == ['django.middleware.security.SecurityMiddleware']  # type: ignore
