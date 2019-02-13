from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate(db=db)

def extension_init(app):
    db.init_app(app)

    login_manager.init_app(app)
    migrate.init_app(app)


    # 设置session不同等级的安全   None basic strong
    # 设置为strong, flask_login会记录客户端IP地址和浏览器代理信息, 如果发生任何的异常 则退出登录
    login_manager.session_protection = "strong"

