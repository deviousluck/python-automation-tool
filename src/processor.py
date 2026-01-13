from typing import List, Dict, Any

def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes the raw data.
    Example logic: 
    1. Strip whitespace from keys and values.
    2. Convert 'age' to integer if present.
    3. Filter out rows with missing essential data (e.g., 'name' is empty).
    """
    processed = []
    
    for row in data:
        # Clean keys and values
        clean_row = {k.strip(): v.strip() for k, v in row.items()}
        
        # Example transformation: Convert age to int
        if 'age' in clean_row and clean_row['age'].isdigit():
            clean_row['age'] = int(clean_row['age'])
            
        # Example filtering: Skip if 'name' is missing
        if 'name' in clean_row and not clean_row['name']:
            continue
            
        processed.append(clean_row)
        
    return processed
