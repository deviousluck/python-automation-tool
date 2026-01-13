import csv
import json
import os
from typing import List, Dict, Any

def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """Reads a CSV file and returns a list of dictionaries."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    data = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def save_json(data: List[Dict[str, Any]], file_path: str) -> None:
    """Saves a list of dictionaries to a JSON file."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Successfully saved data to {file_path}")
