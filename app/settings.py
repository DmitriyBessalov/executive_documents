import inspect
import sys
from yaml import load, SafeLoader


class Postgres:
    host = ...
    port = ...
    user = ...
    password = ...
    database = ...
    debug = ...


class Graphql:
    host = ...
    port = ...
    access_log_file = ...
    error_log_file = ...
    debug = ...


CONFIG_FILE = '../config.yaml'


def load_config():
    """
    Load config from CONFIG_FILE
    """
    config = load(open(CONFIG_FILE, 'r+', encoding='utf-8'), SafeLoader)
    classes = inspect.getmembers(
        sys.modules[__name__],
        lambda member: inspect.isclass(member) and member.__module__ == __name__
    )
    for settings_class in classes:
        if class_config := config.get(settings_class[0]):
            for attribute, value in class_config.items():
                setattr(settings_class[1], attribute, value)


load_config()
