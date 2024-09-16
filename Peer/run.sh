#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
else
    echo "Python3 is already installed."
fi

# Install required Python packages
if [ -f requirements.txt ]; then
    echo "Installing required Python packages..."
    pip3 install -r requirements.txt
else
    echo "No requirements.txt found. Skipping package installation."
fi

# Start the service.py script
echo "Starting service.py..."
python3 service.py