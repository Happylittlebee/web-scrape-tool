from flask import Flask
from flask_cors import CORS

from config import Config
from routes import scrape_bp, analyze_bp, download_bp


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(scrape_bp)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(download_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=Config.FLASK_PORT, debug=True)