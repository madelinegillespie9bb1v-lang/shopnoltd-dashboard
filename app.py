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

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)