#!/bin/bash

# Check if the venv directory exists
if [ -d "venv" ]; then
    # Check if the script is running on Windows or Unix-based system
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        # Windows activation
        source venv/Scripts/activate
    else
        # macOS/Linux activation
        source venv/bin/activate
    fi
    echo "Virtual environment activated."
else
    echo "Virtual environment 'gold-venv' not found."
fi
