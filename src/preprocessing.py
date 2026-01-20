import pandas as pd
import os

def clean_data():
    raw_path = 'data/raw/transactions.csv'
    processed_dir = 'data/processed'
    processed_path = os.path.join(processed_dir, 'cleaned_transactions.csv')
    
    print("--- Pipeline Started ---")
    
    if not os.path.exists(raw_path):
        print(f"ERROR: Raw file NOT found at {raw_path}")
        return

    print(f"Reading {raw_path}...")
    df = pd.read_csv(raw_path)

    # Cleaning logic
    df = df.dropna()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    os.makedirs(processed_dir, exist_ok=True)

    print(f"Saving to {processed_path}...")
    df.to_csv(processed_path, index=False)
    
    if os.path.exists(processed_path):
        print(f"VERIFIED: File created! Size: {os.path.getsize(processed_path)} bytes")
    print("--- Pipeline Finished ---")

if __name__ == "__main__":
    clean_data()
