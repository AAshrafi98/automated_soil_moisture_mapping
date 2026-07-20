import pickle
import pandas as pd
import os

# Path to your pickle file
pkl_file = "ssurgo_soil_properties_by_mukey_py3old.pkl"  # Replace with your actual pickle file path
csv_file = os.path.splitext(pkl_file)[0] + ".csv"

# Load pickle file
with open(pkl_file, 'rb') as f:
    data = pickle.load(f)

# Convert to DataFrame if not already
if isinstance(data, pd.DataFrame):
    df = data
else:
    df = pd.DataFrame(data)

# Save to CSV
df.to_csv(csv_file, index=False)

print(f"Successfully converted {pkl_file} to {csv_file}")

#################################
# Path to your CSV file
# csv_file = "ssurgo_soil_properties_by_mukeytest.csv"  # Replace with your actual CSV file path
# pkl_file = os.path.splitext(csv_file)[0] + "_py.pkl"

# # Load CSV file
# df = pd.read_csv(csv_file)

# # Save to pickle
# with open(pkl_file, 'wb') as f:
#     pickle.dump(df, f)

# print(f"Successfully converted {csv_file} to {pkl_file}")