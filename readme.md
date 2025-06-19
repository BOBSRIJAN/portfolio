# Portfolio Django Project
under devlopment!!!!
## Project Description
This is a Django web application that serves as a personal portfolio website. It features a home page, a contact form, and a custom admin panel for managing projects and contact messages. The backend uses MongoDB for data storage, accessed via pymongo. The admin panel allows for managing project entries and viewing contact submissions.

## Features
- Home page displaying portfolio overview.
- Contact page with a form to submit messages.
- Custom admin panel for managing projects and contacts.
- MongoDB integration for storing projects and contact data.
- Uses Django Tailwind for styling.

## Installation
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   ```
   pip install -r portfolio/requirements.txt
   ```
4. Set up MongoDB and configure connection in `app/dbconf.py`.
5. Run the Django development server:
   ```
   python portfolio/manage.py runserver
   ```

## Usage
- Access the home page at `http://localhost:8000/`.
- Use the contact form to send messages.
- Access the admin panel at `http://localhost:8000/custom-admin/` to manage projects and contacts.

## Folder Structure
- `portfolio/` - Django project settings and configuration.
- `app/` - Main application containing views, URLs, models, and templates.
- `app/templates/app/` - HTML templates for the app.
- `app/static/` - Static files including CSS, JS, and images.
- `portfolio/requirements.txt` - Project dependencies.

## Technologies Used
- Python 3.x
- Django 5.2.3
- MongoDB (via pymongo)
- Django Tailwind
- dotenv for environment variable management

## License
This project is licensed under the MIT License.
