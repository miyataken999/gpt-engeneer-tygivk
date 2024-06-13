#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py runserver 0.0.0.0:8000
