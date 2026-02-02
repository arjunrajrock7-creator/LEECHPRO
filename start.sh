#!/bin/bash

# Activate virtual environment if it exists (for Local/VPS)
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run the update script to fetch the latest bot code from UPSTREAM_REPO
python3 update.py

# Start the bot
python3 -m bot
