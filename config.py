import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://neondb_owner:npg_ykqbLfrN12Sj@ep-cold-shadow-a476tq5y-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("Shopnoltd Support", os.getenv("MAIL_USERNAME"))

    DEBUG = bool(os.environ.get("FLASK_DEBUG", False))