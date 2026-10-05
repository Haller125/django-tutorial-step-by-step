from django import template

register = template.Library()


@register.filter
def percentage(value, total):
    """
    Return how much of ``total`` the given part represents, as a whole number.

    Used by the results page to size the vote bars and to print the share of
    votes each choice received. Returns 0 when there is nothing to divide by.
    """
    try:
        total = float(total)
        value = float(value)
    except (TypeError, ValueError):
        return 0
    if total <= 0:
        return 0
    return round(value / total * 100)