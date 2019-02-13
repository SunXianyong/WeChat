from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from App import create_app


# 创建app
app = create_app()
CORS(app,supports_credentials=True)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    # manager.run()
    app.run(host="127.0.0.1",port="8099")
