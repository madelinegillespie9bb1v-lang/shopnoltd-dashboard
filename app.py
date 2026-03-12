from flask import Flask
import os
from config import Config
from extensions import db, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # Import blueprints
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp
    from routes.device_routes import device_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(device_bp)

    # Create database tables
    with app.app_context():
        from models.models import User, LoggedUser
        db.create_all()

    # Health check
    @app.route("/ping")
    def ping():
        return "ok", 200

    return app


app = create_app()

# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)