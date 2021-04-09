# Jijoo
Quick to find Ads. Free Classifieds. Search in Your Region. Buy and Sell Anything. Post Free Ads. Real People, all in Nigeria

## Features

- Django-based backend

    - [Django](https://www.djangoproject.com/)
    - Python 3.6 or later
    - [SPA] Accessible from port `3000` for local development


- Batteries

    - Linting of Python,  [Flake8](http://prospector.landscape.io/),
    - Automated code-formatting using [black](https://black.readthedocs.io) and [prettier](https://prettier.io)
    - Deploy helpers, using [Ansible](https://www.ansible.com/)
    - Media files are can stored in the app but will be stored in a CDN like S3 or Google Cloud Storage in future
    - Out-of-the-box configuration for nginx, gunicorn and logrotate
    - Includes [PyCharm](https://www.jetbrains.com/pycharm/) project config


## Usage

To use run this application

1. Activate the virtualenv

2. Install the requirements of the project by running
    ```
    pip install -r requirements.txt
   
3. Navigate to the directory where you'd like to create your project:
    ```
    cd /jijoo/
    ```

4. Run migrations 
    ```
    python manage.py migrate
    ```
5. You can create a superuser (optional)
    ```
   python manage.py createsuperuser
   ```
   follow the prompts


It will ask you a few questions, e.g. project's name.
To create isomorphic single-page application set `frontend_style == spa`. Then separate node application will be created supported by [Razzle](https://razzlejs.org/)

See README.md in the generated project for instructions on how to set up your development environment.
