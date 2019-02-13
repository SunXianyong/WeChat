from flask import Flask


# from .settings import config
# from .extensions import extension_init
from .views import blueprint_register


def create_app():
    app = Flask(__name__)

    # 加载配置
    # app.config.from_object(config["default"])
    # 初始化app函数
    # extension_init(app)
    # 蓝本注册函数
    blueprint_register(app)
    return app