from application.models import *
from application.cache import cache


@cache.memoize()
def getAllUsers():
    users = User.query.all()
    return users