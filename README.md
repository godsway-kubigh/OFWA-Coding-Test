# Galamsay Mining Sites Analysis Project

## Project Overview
This project analyzes illegal small-scale mining (Galamsay) sites across various cities and regions in Ghana.

## Features
- Data analysis of Galamsay sites
- Django REST API to expose analysis results
- Database storage of site information and analysis

## Prerequisites
- Python 3.9+
- pip
- virtualenv (recommended)

## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/godsway-kubigh/OFWA-Coding-Test.git
cd OFWA-Coding-Test
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup Django database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run data upload script
```bash
python upload_data.py
```

## Running the Application
```bash
python manage.py runserver
```

## Running Tests
```bash
export DJANGO_SETTINGS_MODULE=root.settings
# set DJANGO_SETTINGS_MODULE=root.settings - use this command on windows
pytest
```

## API Endpoints
- `/api/v1/sites/`: List all Galamsay sites
- `/api/v1/analysis/`: List historical analysis results
