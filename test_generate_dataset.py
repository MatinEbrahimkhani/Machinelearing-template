import pandas as pd
import numpy as np

# Parameters for dataset
num_samples = 1000
np.random.seed(42)

# Generate synthetic data
data = {
    'customer_id': range(1, num_samples + 1),
    'age': np.random.randint(18, 70, size=num_samples),
    'gender': np.random.choice(['Male', 'Female'], size=num_samples),
    'tenure': np.random.randint(1, 60, size=num_samples),
    'balance': np.random.uniform(-1000, 10000, size=num_samples),
    'products_number': np.random.randint(1, 4, size=num_samples),
    'has_cr_card': np.random.choice([0, 1], size=num_samples),
    'is_active_member': np.random.choice([0, 1], size=num_samples),
    'estimated_salary': np.random.uniform(20000, 120000, size=num_samples),
    'churn': np.random.choice([0, 1], size=num_samples)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('./data/raw/customer_churn.csv', index=False)
print("Synthetic dataset generated and saved to /data/raw/customer_churn.csv")
