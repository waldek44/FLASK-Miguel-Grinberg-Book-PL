import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Bazowa Klasa Config ma ustawienia wspólne dla wszystkich środowisk
# os.environ.get() pozwala najpierw poszukać zmiennej w podklasie środowiska
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CZEGO TO NIE MA NA NETFLIX'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # metoda która jako argument przyjmuje instancję aplikacji - umożliwia dodawanie własnych konfiguracji
    @staticmethod
    def init_app(app):
        pass


# podklasa rozszerzająca klasę Config dla środowiska dev
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


# podklasa rozszerzająca klasę Config dla środowiska testów
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


# podklasa rozszerzająca klasę Config dla środowiska produkcyjnego
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
