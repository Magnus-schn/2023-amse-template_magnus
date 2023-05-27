#!/bin/bash

# Execute the data pipeline
python data/data_pipeline.py

# Validate the output files
if [ -f "data/database.db" ]; then
    echo "SQLite database file created successfully."
else
    echo "Error: SQLite database file not found."
fi