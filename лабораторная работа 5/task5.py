import string
from random import sample


def get_random_password() -> str:
    return ''.join(sample((string.ascii_letters + string.digits), 8))


print(get_random_password())
