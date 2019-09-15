from baskets.config.base_config import Config


class DevelopmentConfig(Config):
    """Development config."""
    DEVELOPMENT = True
    DEBUG = True
