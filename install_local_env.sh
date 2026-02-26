#!/bin/bash

set -e  # stop script if any command fails

echo ""
echo "Updating PIP..."

# Remove old environments
rm -rf .venv venv

# Create new virtual environment (using python3 for Unix)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

echo ""
echo "Updating all packages and resources..."

pip install -r requirements.txt
pip install playwright
playwright install --with-deps
pip install --upgrade pip

echo ""
echo "Packages installed:"
which python
which pip
pip list