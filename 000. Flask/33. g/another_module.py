from flask import g


def access_g():
    print(g.any_data)
