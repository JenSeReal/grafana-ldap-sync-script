import os
import random
import string

path = os.getcwd() + "\\export-script"


def get_random_alphanumerical():
    """
    Creates a random alphanumerical string with a length of 16 characters.
    :return: A random alphanumerical string with a length of 16 characters.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def lock():
    """
    Creates a local .lock-file when called. If the .lock-file already exists, false is returned.
    :return: True if the lock-file was newly created, False if the lock-file already existed.
    """
    if os.path.exists("./.lock"):
        return False
    lock_file = open("./.lock", "w+")
    lock_file.close()
    return True


def unlock():
    """
    Removes the .lock-file.
    """
    os.remove("./.lock")


def get_user_attr(user, attribute):
    """
    Takes a user and an attribute. Retrieves the value found with the given attribute and strips it off of unwanted
    pre- and suffixes. Then the value is returned.
    :param user: The user the attribute should be retrieved from.
    :param attribute: The attribute which should be retrieved from the user.
    :return:The value found in the given attribute stripped off of unwanted pre- and suffixes.
    """
    return str(user["raw_attributes"][attribute][0])[2: len(user["raw_attributes"][attribute][0]) + 2]