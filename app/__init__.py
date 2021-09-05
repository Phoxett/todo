from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from os import environ

login_manager = LoginManager()
socketio = SocketIO()
sqlalchemy = SQLAlchemy()


def create_app():


    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///db.db"#environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = b'\x1f\xa1f\xaf\xd2\xc9\x9d\xcf\xc4\x87\xc8~Y\xe5c`\x97\xd6;\x0b\xd9M\x0f\x9b@\\p\xef\xdfvl\xd2\xf8\xfc\xbf\xc0uZ<:E\x8b\xc4N\xa9\x91;D\x80\x81\xe5\xc2-{\x12\x0f3\x17:\x11\x0b\xb9]\xb7\x16\x0b\xe5\xc6:\xdc4k\xd8\x89T\x01P7f\xf3\xd4;\xd7t\xb0\xac_\x16e\xdf\x8aA\x99\x1c\x9d\x9e>\xc6>H'


    sqlalchemy.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userID):
        return sqlalchemy.get(userID)
    
    with app.app_context():


        from .main import main


        app.register_blueprint(main.mainbp)
        sqlalchemy.create_all()

        return app