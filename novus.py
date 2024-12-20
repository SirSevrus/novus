import os
import importlib
import logging
from dotenv import load_dotenv
from colorama import Fore, init, Back
from flask import Flask, Blueprint
from libs.__init__ import *
from libs.ver import tellVersion
from libs.check_root import is_user_admin

init(autoreset=True)

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
    setup_flask_project()    
    load_dotenv()         # Load environment variables from the .env file

    app_name = os.getenv("APP_NAME")
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "false").lower() in ["true", "1", "t", "yes"]
    if debug == True:
        print(Fore.CYAN + "[" + Fore.YELLOW + "Novus" + Fore.CYAN + "] " + Fore.CYAN + "Debug mode active, to turn of it set DEBUG to 'false' in .env file.")
    else:
        print(Fore.CYAN + "[" + Fore.YELLOW + "Novus" + Fore.CYAN + "] " + Fore.CYAN + "Debug mode is not active, to turn it on set DEBUG to 'true' in .env file.")
    app = Flask(app_name)
    register_routes(app)

    logging.info(f"App configured with name '{app_name}', running on http://{host}:{port}, debug={debug}")
    return app, host, port, debug

if __name__ == "__main__":
    if is_user_admin():
        print(Fore.CYAN + '[' + Fore.YELLOW + "Novus" + Fore.CYAN + '] ' + Fore.RED + "Administrator Privleges found, you may get file issues while running the server with non-admin priveleges!")
    app, host, port, debug = setup_app()
    tellVersion()
    logging.info(Fore.CYAN + f"Starting Flask server on " + Back.BLUE + f"http://{host}:{port}" + Back.RESET + Fore.CYAN + "...")
    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        logging.error(f"An error occurred while running the Flask server: {e}")
