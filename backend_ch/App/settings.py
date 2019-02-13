import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 没有密钥，不能flash
    SECRET_KEY = "abc123"

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


# 开发环境
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:aithu@2018@127.0.0.1:3306/jj"


# 测试环境
class TestConfig(Config):
    pass


# 生产环境
class ProductionConfig(Config):
    pass


config = {
    "development": DevelopConfig,
    "testing": TestConfig,
    "production": ProductionConfig,

    # 默认开发环境
    "default": DevelopConfig
}

# 节点名字对应节点id
node_table = {
    "snail":1,
}

# 三个平台的对应码
platform_table = {
    "1": "Fac",
    "2": "Ins",
    "3": "Twi"
}

status_code = {
    # 通用
    "fbd_401": {"code": 401, "msg": "无权限"},

    "add_200": {"code": 200, "msg": "add success"},
    "del_200": {"code": 200, "msg": "del success"},
    "edit_200": {"code": 200, "msg": "edit success"},
    "setting_200": {"code": 200, "msg": "setting success"},

    "add_403": {"code": 403, "msg": "添加失败"},
    "del_403": {"code": 403, "msg": "删除失败"},
    "update_403": {"code": 403, "msg": "修改失败"},
    "setting_403": {"code": 403, "msg": "配置失败"},
    "param_error":{"code": 400, "msg": "参数错误"},
    
    # 用户相关
    "code_add_200": {"code": 200, "msg": "create success"},

    "user_add_200": {"code": 200, "msg": "create success"},
    "user_del_200": {"code": 200, "msg": "del success"},
    "user_update_200": {"code": 200, "msg": "update success"},
    "user_sear_200": {"code": 200, "msg": "search success"},

    "username_409": {"code": 409, "msg": "用户名已存在"},
    "register_code_409": {"code": 409, "msg": "无效的注册码"},

    "user_del_403": {"code": 403, "msg": "删除失败"},
    "user_update_403": {"code": 403, "msg": "修改失败"},
    "user_sear_403": {"code": 403, "msg": "查询失败"},

    "login_200": {"code": 200, "msg": "login success"},
    "login_403": {"code": 403, "msg": "用户名或密码错误"},
    "login_fbd_401": {"code": 401, "msg": "该账号已被禁用"},
    "logout_200": {"code": 200, "msg": "logout success"},

    # 账号相关
    "account_add_200": {"code": 200, "msg": "add success"},
    "account_del_200": {"code": 200, "msg": "del success"},
    "account_update_200": {"code": 200, "msg": "update success"},
    "account_sear_200": {"code": 200, "msg": "search success"},

    "account_del_403": {"code": 403, "msg": "删除失败"},
    "account_update_403": {"code": 403, "msg": "修改失败"},
    "account_sear_403": {"code": 403, "msg": "查询失败"},


}