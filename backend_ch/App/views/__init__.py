# from .order import order
# from .goods import goods
from .weixin import weixin


blueprints = [
    (weixin, "/"),
]


def blueprint_register(app):
    for blue, pref in blueprints:
        app.register_blueprint(blue, url_prefix=pref)