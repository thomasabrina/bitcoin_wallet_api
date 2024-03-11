from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')
    CORS(app)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../bitcoinwallet.db'
    
    db.init_app(app)
    
    with app.app_context():
        from . import models
        db.create_all()
        from .seed import seed_database
        @app.cli.command("seed-db")
        def seed_db_command():
            """Seeds the database with sample data."""
            seed_database()
            print("Database seeded.")
        
    from .routes import bp
    app.register_blueprint(bp)
    
    return app