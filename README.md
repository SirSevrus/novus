# Novus - fluffy-fudgehead-0.51
A better form of flask webserver for develpoment purposes. The application is python based and saves time by automatically creating the necessary directories like templates, static and also .env file for configuring the server.
## Overview
This project is a Flask-based web application designed for demonstrating structured route handling, error pages, and environment configuration. It includes modular route handling with separate Python files for each route, custom error handling templates, environment configuration, and dynamic CSS-styled error pages.

## Features
- Modular route handling with separate route files.
- Custom error handling for 404 (Not Found) and 405 (Method Not Allowed) errors.
- Environment configuration using a `.env` file.
- Comprehensive logging to track application activity.
- Directory creation functions for setting up the project structure.
- CSS-styled templates for better user experience.
- Each route can be defined seperately inside routes and automatically loaded by server on run.

## Prerequisites
Ensure that the following software is installed on your system:
- [Python](https://www.python.org/downloads/) (version >= 3.x)
- [pip](https://pip.pypa.io/en/stable/installation/) for Python package management

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sirSevrus/novus.git
   cd novus
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application to create the **.env** file automatically and then edit it as per your needs.
```bash
python3 novus.py
```
- if you are on windows then do
```bash
python novus.py
```

## Directory Structure
Necessary directories like **templates**, **static** will be created automatically during first run.
```
novus/
│
├── routes/                # Route files (e.g., home.py, about.py, errors.py) [Automatically Created]
│   └── errors.py          # Error handling routes
│
├── templates/             # HTML template files [Automatically Created]
│   ├── 404.html           # Custom 404 page
│   └── 405.html           # Custom 405 page
│   └── index.html         # Main index page
│
├── static/                # Static files (CSS, JS, images) [Automatically Created]
│   └── css/               # CSS files
│       └── errors.css     # Styling for error pages
│
├── .env                   # Environment variables file [Automatically Created]
├── novus.py                 # Main application script
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Access the application at `http://localhost:5000` in your browser.

3. Test error handling by visiting non-existent routes or using disallowed HTTP methods.

## Error Handling
- **404 - Not Found**: Served by `templates/404.html`
- **405 - Method Not Allowed**: Served by `templates/405.html`

## Logging
Logs are stored in the `logs/` directory to monitor application activity. The directory will be creatd automatically during first run.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the [GPL-2.0] license. See the [LICENSE](./LICENSE) file for more details.

## Acknowledgements
- `Flask` for the web framework
- `tqdm` for progress bars
- `colorama` for colured output
