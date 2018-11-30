"""Errors for articles module."""


class BodyNotFoundError(ValueError):
    """Error indicating there is no body in html."""
    pass


class HeaderNotFoundError(ValueError):
    """Error indicating there is no header in html."""
    pass
