import os
import time
import subprocess
from tqdm import tqdm

def setup_flask_project(add_dirs=None):
    try:
        # Step 1: Create directories
        dirs = ["templates", "static", "static/images", "static/css", "static/js", "static/other"]
        if add_dirs:
            dirs.extend(add_dirs)

        pbar = tqdm(total=len(dirs), desc="Checking directories...", ascii="█▒░", colour="green")
        for directory in dirs:
            pbar.set_description(f"Creating {directory}")
            os.makedirs(directory, exist_ok=True)
            time.sleep(0.5)  # Simulate work
            pbar.update(1)

        pbar.close()
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("[✔] Directories checked successfully!")

        # Step 2: Create .env file
        file_path = ".env"
        if not os.path.exists(file_path):
            default_content = {
                "APP_NAME": '"Novus"',
                "HOST": '"localhost"',
                "DEBUG": "true",
                "PORT": "5000",
                "DATABASE_URL": "sqlite:///mydatabase.db"
            }
            with open(file_path, "w") as env_file:
                for key, value in default_content.items():
                    env_file.write(f"{key}={value}\n")
            print(f"[✔] '{file_path}' created with default content.")
        else:
            print(f"[✔] '{file_path}' already exists.")

        # Step 3: Create index.html
        index_html_path = "templates/index.html"
        if not os.path.exists(index_html_path):
            html_content = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
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
    <div class=\"container\">
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
        <pre>python novus.py</pre>
        <p>Enjoy building your Flask app!</p>
    </div>
</body>
</html>
"""
            os.makedirs(os.path.dirname(index_html_path), exist_ok=True)
            with open(index_html_path, "w", encoding="utf-8") as file:
                file.write(html_content)
            print("[✔] 'index.html' created successfully.")
        else:
            print("[✔] 'index.html' already exists.")

        # Step 4: Create home.py route
        home_route_path = "routes/home.py"
        if not os.path.exists(home_route_path):
            home_code_content = """from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')
"""
            os.makedirs(os.path.dirname(home_route_path), exist_ok=True)
            with open(home_route_path, "w", encoding="utf-8") as file:
                file.write(home_code_content)
            print("[✔] 'home.py' created successfully.")
        else:
            print("[✔] 'home.py' already exists.")

        # Step 5: Create errors.py route
        errors_path = 'routes/errors.py'
        if not os.path.exists(errors_path):
            route_content = """from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return render_template('405.html'), 405
"""
            os.makedirs(os.path.dirname(errors_path), exist_ok=True)
            with open(errors_path, 'w') as file:
                file.write(route_content)
            print("[✔] `errors.py` route file created successfully")
        else:
            print("[✔] 'errors.py' already exists.")

        # Step 6: Create error HTML templates
        error_templates = {
            "404.html": """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>404 - Not Found</title>
    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/errors.css') }}\">
</head>
<body>
    <div class=\"error-container\">
        <h1>404 - Page Not Found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
    </div>
</body>
</html>
""",
            "405.html": """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>405 - Method Not Allowed</title>
    <link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/errors.css') }}\">
</head>
<body>
    <div class=\"error-container\">
        <h1>405 - Method Not Allowed</h1>
        <p>Sorry, the method used is not allowed for this request.</p>
    </div>
</body>
</html>
"""
        }

        for file_name, content in error_templates.items():
            file_path = os.path.join('templates', file_name)
            with open(file_path, 'w') as file:
                file.write(content)
        print("[✔] Error HTML templates created successfully")

        # Step 7: Create error.css
        css_content = """.error-container {
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
"""
        css_path = 'static/css/errors.css'
        with open(css_path, 'w') as file:
            file.write(css_content)
        print("[✔] `errors.css` file created successfully")

    except Exception as e:
        print(f"[X] An error occurred: {e}")