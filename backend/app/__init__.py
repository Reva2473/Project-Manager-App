from flask import Flask, send_from_directory
from .extensions import bcrypt, jwt, cors
import os
import datetime
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(current_dir, '..', '..', 'frontend')
    app = Flask(__name__, static_folder=os.path.abspath(frontend_dir), static_url_path='')

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret-collabtask-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    
    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.projects import projects_bp
    from .routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    
    @app.route('/')
    def serve_index():
        return app.send_static_file('index.html')
        
    @app.route('/<path:path>')
    def serve_static(path):
        return app.send_static_file(path)

    return app
