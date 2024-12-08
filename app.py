import os
import importlib
import logging
from dotenv import load_dotenv
from flask import Flask, Blueprint
from libs.__init__ import *  # Ensure this import is necessary or adjust accordingly

# Ensure the 'logs' directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging to write to a file and print to the console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Logs will be printed to the console
        logging.FileHandler('logs/app.log')  # Logs will be written to a file in the logs directory
    ]
)

# Automatically import and register all Blueprints from the `routes` directory
def register_routes(app, routes_folder='routes'):
    try:
        for file in os.listdir(routes_folder):
            if file.endswith('.py') and file != '__init__.py':
                module_name = f"{routes_folder}.{file[:-3]}"
                module = importlib.import_module(module_name)

                # Register any object in the module that is a Blueprint
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, Blueprint):  # Check if it's a Blueprint
                        app.register_blueprint(obj)
                        logging.info(f"Registered blueprint '{attr}' from '{module_name}'")
    except Exception as e:
        logging.error(f"Error occurred while registering routes: {e}")

# Initial setup for the Flask app
def setup_app():
    logging.info("Starting setup for the Flask app...")
    createDirs()          # Creates necessary directories
    create_index_html() # Creates the default index.html
    create_error_html()
    create_error_css()
    create_error_route()
    create_home_route()   # Creates the home route in routes/home.py
    create_env_file()     # Creates .env file for environment variables
    load_dotenv()         # Load environment variables from the .env file

    app_name = os.getenv("APP_NAME")
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "false").lower() in ["true", "1", "t", "yes"]

    app = Flask(app_name)
    register_routes(app)

    logging.info(f"App configured with name '{app_name}', running on http://{host}:{port}, debug={debug}")
    return app, host, port, debug

if __name__ == "__main__":
    app, host, port, debug = setup_app()
    logging.info(f"Starting Flask server on http://{host}:{port}...")
    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        logging.error(f"An error occurred while running the Flask server: {e}")
