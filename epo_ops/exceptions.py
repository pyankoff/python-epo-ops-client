from requests.exceptions import HTTPError


# Query errors
class InvalidDate(ValueError):
    """User used an invalid date."""


class MissingRequiredValue(ValueError):
    """User did not supply a required value."""


# OPS quota errors
class AnonymousQuotaPerMinuteExceeded(HTTPError):
    """Anonymous per minute quota exceeded."""


class AnonymousQuotaPerDayExceeded(HTTPError):
    """Anonymous per day quota exceeded."""


class IndividualQuotaPerHourExceeded(HTTPError):
    """Anonymous per day quota exceeded."""


class RegisteredQuotaPerWeekExceeded(HTTPError):
    """Anonymous per day quota exceeded."""
