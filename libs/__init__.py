import os
import time
import subprocess
from tqdm import tqdm

def createDirs(add_dirs=None):
    try:
        # Base directories
        dirs = ["templates", "static", "static/images", "static/css", "static/js", "static/other"]
        
        # Add custom directories
        if add_dirs:
            dirs.extend(add_dirs)

        # Initialize progress bar
        pbar = tqdm(total=len(dirs), desc="Checking directories...", ascii="█▒░", colour="green")
        for directory in dirs:
            # Update progress bar description
            pbar.set_description(f"Creating {directory}")
            os.makedirs(directory, exist_ok=True)
            time.sleep(0.5)  # Simulate work
            pbar.update(1)

        pbar.close()

        # Clear the console (Windows only)
        subprocess.run("cls", shell=True)
        print("[✔] Directories checked successfully!")
    except Exception as e:
        print("[X] An error occurred during directory creation!")
        print(f"Error details: {e}")

def create_env_file(default_content=None, file_path=".env"):
    """
    Creates a .env file with default content if it doesn't exist.

    Args:
        default_content (dict): Default key-value pairs to write in the .env file.
        file_path (str): Path to the .env file (default is ".env").
    """
    if os.path.exists(file_path):
        print(f"[✔] '{file_path}' already exists.")
        return

    # Default content if not provided
    if default_content is None:
        default_content = {
            "APP_NAME": '"My Flask APP"',
            "HOST": '"localhost"',
            "DEBUG": "true",
            "PORT": "5000",
            "DATABASE_URL": "sqlite:///mydatabase.db"
        }

    try:
        # Create the .env file and write default content
        with open(file_path, "w") as env_file:
            for key, value in default_content.items():
                env_file.write(f"{key}={value}\n")
        
        print(f"[✔] '{file_path}' created with default content.")
    except Exception as e:
        print(f"[X] An error occurred while creating '{file_path}': {e}")

import os

def create_index_html(file_path="templates/index.html"):
    """
    Creates a default index.html file with congratulatory message and Python setup steps.
    """
    if os.path.exists(file_path):
        print("[✔] 'index.html' already exists.")
        return

    try:
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Server Running</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: green;
        }
        p {
            font-size: 1.2em;
        }
        pre {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Congratulations!</h1>
        <p>The Flask server is running and up. Your configuration is correct, and the server is ready to serve your app.</p>
        <h2>Documentation</h2>
        <p>This page is a basic index showing that the Flask server is running. You can add more content and customize it according to your needs.</p>
        <h2>Python Setup Steps</h2>
        <p>Ensure you have Python installed and properly configured. You can verify your installation with:</p>
        <pre>python --version</pre>
        <p>Install Flask using:</p>
        <pre>pip install flask</pre>
        <p>Start your Flask application with:</p>
        <pre>python app.py</pre>
        <p>Enjoy building your Flask app!</p>
    </div>
</body>
</html>
"""
        # Create the templates directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write the content to the index.html file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        
        print("[✔] 'index.html' created successfully.")
    except Exception as e:
        print(f"[X] An error occurred while creating 'index.html': {e}")

def create_home_route(file_path="routes/home.py"):
    """
    Creates a home route script at the specified file path.
    """
    if os.path.exists(file_path):
        print("[✔] 'home.py' already exists.")
        return

    try:
        code_content = """from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
# Home route serving the flask server's '/' route.
def home():
    return render_template('index.html')
"""
        # Create the 'routes' directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the content to home.py
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code_content)

        print("[✔] 'home.py' created successfully.")
    except Exception as e:
        print(f"[X] An error occurred while creating 'home.py': {e}")

def create_error_route():
    route_content = '''
from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return render_template('405.html'), 405
    '''

    # Write to the `errors.py` file
    errors_path = 'routes/errors.py'
    os.makedirs(os.path.dirname(errors_path), exist_ok=True)
    with open(errors_path, 'w') as file:
        file.write(route_content)
    print("[✔] `errors.py` route file created successfully")

# Function to create the HTML templates for errors
def create_error_html():
    # Content for 404.html
    html_404 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 - Not Found</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/errors.css') }}">
</head>
<body>
    <div class="error-container">
        <h1>404 - Page Not Found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
    </div>
</body>
</html>
    '''

    # Content for 405.html
    html_405 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>405 - Method Not Allowed</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/errors.css') }}">
</head>
<body>
    <div class="error-container">
        <h1>405 - Method Not Allowed</h1>
        <p>Sorry, the method used is not allowed for this request.</p>
    </div>
</body>
</html>
    '''

    # Write the HTML files to the `templates` directory
    os.makedirs('templates', exist_ok=True)
    with open('templates/404.html', 'w') as file:
        file.write(html_404)
    with open('templates/405.html', 'w') as file:
        file.write(html_405)
    
    print("[✔] Error HTML templates created successfully")

def create_error_css():
    css_content = '''
.error-container {
    text-align: center;
    margin-top: 100px;
    font-family: Arial, sans-serif;
}

.error-container h1 {
    font-size: 48px;
    color: #d9534f; /* Red color for error */
}

.error-container p {
    font-size: 24px;
    color: #333; /* Dark gray color for text */
}
    '''

    # Create the `static/css/` directory if it doesn't exist
    os.makedirs('static/css', exist_ok=True)
    
    # Write the CSS content to the `static/css/errors.css` file
    with open('static/css/errors.css', 'w') as file:
        file.write(css_content)
    
    print("[✔] `errors.css` file created successfully")