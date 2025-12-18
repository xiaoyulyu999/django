if IN_DOCKER:  # type: ignore # noqa: F821
    print("In Docker")

    assert MIDDLEWARE[0] == ['django.middleware.security.SecurityMiddleware']  # type: ignore # noqa: F821
