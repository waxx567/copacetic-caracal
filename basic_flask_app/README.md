# Basic Flask Application

This is a simple Flask-based web application that includes:

- **HTML** for structure
- **CSS** for styling
- **Jinja** templates for dynamic content rendering
- **Flask** for backend routing and server functionality

## Pages Included

1. **Home Page**: The main landing page for the application.
2. **About Page**: A page describing the application or organization.
3. **Services Page**: A page detailing the services offered.
4. **Product Pages**: Three individual pages showcasing different products.

## Prerequisites

To run this application, ensure you have the following installed:

- **Python 3.9 or later**
- **Flask** (a Python web framework)

## How to Run the Program

### On Windows

1. Open a terminal (Command Prompt or PowerShell).
2. Clone the repository or download the application files.
   ```
   git clone https://github.com/waxx567/Dell/tree/main/resume%20projects/flask_website
   cd flask-app
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```
   flask run
   ```
6. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

### On Mac

1. Open a terminal.
2. Clone the repository or download the application files.
   ```
   git clone https://github.com/waxx567/Dell/tree/main/resume%20projects/flask_website
   cd flask-app
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```
5. Run the Flask application:
   ```
   flask run
   ```
6. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

## Application Structure

```
flask-app/
|-- static/
|   |-- css/
|       |-- styles.css
|-- templates/
|   |-- base.html
|   |-- home.html
|   |-- about.html
|   |-- services.html
|   |-- product1.html
|   |-- product2.html
|   |-- product3.html
|-- app.py
|-- requirements.txt
|-- README.md
```

- `static/`: Contains static files like CSS and images.
- `templates/`: Contains HTML templates rendered using Jinja.
- `app.py`: Main application file containing Flask routes.
- `requirements.txt`: Lists dependencies needed for the application.
- `README.md`: Documentation file.

## Customizing the Application

- Update the content of the HTML templates in the `templates/` directory to fit your needs.
- Add additional CSS styling in the `static/css/styles.css` file.
- Add more routes and logic in `app.py` as required.

## Notes

- If you encounter an "Address already in use" error, modify the port in `flask run` using:
  ```
  flask run --port=8080
  ```

- To exit the virtual environment:
  - On Windows: `deactivate`
  - On Mac: `deactivate`

## Dependencies

The required dependencies for this application are listed in `requirements.txt`. Ensure these are installed before running the application:

- Flask

## Contact

For any issues or suggestions, feel free to [email](waynem567@gmail.com) me.
