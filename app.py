from flask import Flask
from config import Config
from extensions import db, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.device_routes import device_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(device_bp)

    with app.app_context():
        from models.models import User, LoggedUser
        db.create_all()

    @app.route("/ping")
    def ping():
        return "ok"

    return app


app = create_app()