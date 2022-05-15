import os

class Config:
    SECRET_KEY='secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQALCHEMY_TRACK_MODIFICATIONS = True
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
        """
        Production configuration child class
            
            Args:
                Config: The parent configuration class with General configuration settings
            """
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
         SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abrighthuman:bright@localhost/blog'
DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
