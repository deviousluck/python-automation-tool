import os
import sys

# Add the src directory to sys.path to allow imports if running directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import file_handler, processor

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, 'data', 'input.csv')
    output_file = os.path.join(base_dir, 'data', 'output.json')
    
    print("Starting automation tool...")
    
    try:
        # 1. Read Data
        print(f"Reading from {input_file}...")
        raw_data = file_handler.read_csv(input_file)
        print(f"Read {len(raw_data)} rows.")
        
        # 2. Process Data
        print("Processing data...")
        processed_data = processor.process_data(raw_data)
        print(f"Processed {len(processed_data)} valid rows.")
        
        # 3. Output Results
        print(f"Saving to {output_file}...")
        file_handler.save_json(processed_data, output_file)
        
        print("Done!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
