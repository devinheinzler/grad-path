class Config:
    DEBUG = True  # Set this to False for production
    SECRET_KEY = 'your_secret_key_here'  # Replace with a strong secret key

    # Database configuration for SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False