#!/usr/bin/env bash

# A script that checks if the user is running Windows or Linux
# and sets up a virtual environment accordingly

# Check if a virtual environment already exists
if [ -d ".venv" ]; then
    echo "Virtual environment already exists"
    exit 1
else
    echo "No virtual environment found"
    mkdir .venv
fi

echo "Creating virtual environment"

# Determine if we are running (Windows/Unix) and setup virtual environment accordingly
if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    echo "Windows detected"

    python -m venv .venv
    source .venv/Scripts/activate
else
    echo "Linux detected"
    python3 -m venv venv
    source .venv/bin/activate
fi

# Check if venv setup was successful
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment"
    exit 2
fi

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Failed to install dependencies"
        exit 3
    fi
    echo "Virtual environment setup complete"
else
    echo "requirements.txt not found"
    exit 4
fi
