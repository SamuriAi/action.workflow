from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration settings can be added here
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    with app.app_context():
        # Import and register blueprints or modules
        from . import routes
        app.register_blueprint(routes.bp)
    
    return app
