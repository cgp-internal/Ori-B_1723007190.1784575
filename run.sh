#!/bin/bash

# Install Python
sudo apt-get update
sudo apt-get install python3 -y

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Deactivate virtual environment
deactivate

# Run the Flask application
python app.py