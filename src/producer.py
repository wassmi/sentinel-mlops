import pandas as pd
import numpy as np
import os

def generate_transaction_data(n=500):
    """Simulates financial transactions for fraud detection."""
    np.random.seed(42) 
    data = {
        'timestamp': pd.date_range(start='now', periods=n, freq='min'),
        'amount': np.round(np.random.uniform(1.0, 5000.0, n), 2),
        'location_id': np.random.randint(100, 999, n),
        'is_fraud': np.random.choice([0, 1], size=n, p=[0.98, 0.02])
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    os.makedirs('data/raw', exist_ok=True)
    print("🚀 Generating Sentinel transaction data...")
    df = generate_transaction_data(500)
    
    output_path = 'data/raw/transactions.csv'
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Data saved to: {output_path}")