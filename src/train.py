import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

def train_model():
    # 1. Load data
    data_path = 'data/processed/cleaned_transactions.csv'
    df = pd.read_csv(data_path)
    
    # 2. Dummy target (Any amount > 900 is 'fraud')
    df['is_fraud'] = (df['amount'] > 900).astype(int)
    X = df[['amount']]
    y = df['is_fraud']
    
    # 3. Train
    print("Training RandomForest model...")
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # 4. Save
    os.makedirs('models', exist_ok=True)
    with open('models/fraud_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Model saved to models/fraud_model.pkl")

if __name__ == "__main__":
    train_model()
