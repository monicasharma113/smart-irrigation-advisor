"""
Train Machine Learning Models for Smart Irrigation Advisor

This script trains:
1. Regression Model: Predicts weekly water requirement (mm)
2. Classification Model: Classifies irrigation urgency (Irrigate Now/Soon/Not Needed)
3. Label Encoder: Encodes crop types

Usage:
    python train_model.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, accuracy_score, classification_report
import pickle
import os

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

print("=" * 60)
print("Smart Irrigation Advisor - Model Training")
print("=" * 60)

# Load dataset
print("\n[1/6] Loading dataset...")
df = pd.read_csv('data/Crop_recommendation.csv')
print(f"   ✓ Loaded {len(df)} records")

# Filter for rice and maize only
print("\n[2/6] Filtering data for Rice and Maize...")
df = df[df['label'].isin(['rice', 'maize'])].copy()
print(f"   ✓ Filtered to {len(df)} records")
print(f"   ✓ Rice: {len(df[df['label'] == 'rice'])} records")
print(f"   ✓ Maize: {len(df[df['label'] == 'maize'])} records")

# Encode crop labels
print("\n[3/6] Encoding crop labels...")
label_encoder = LabelEncoder()
df['crop_encoded'] = label_encoder.fit_transform(df['label'])
print(f"   ✓ Encoded crops: {label_encoder.classes_}")

# Create synthetic water requirement target
# This is based on crop type, temperature, humidity, and other factors
print("\n[4/6] Creating synthetic water requirement target...")
def calculate_water_requirement(row):
    """
    Calculate weekly water requirement based on:
    - Crop type (rice needs more water)
    - Temperature (higher temp = more water)
    - Humidity (lower humidity = more water)
    - Soil nutrients (affect water efficiency)
    """
    base_water = 150 if row['label'] == 'rice' else 80  # Base weekly requirement
    
    # Temperature effect (optimal around 22-25°C)
    temp_factor = 1.0
    if row['temperature'] < 20:
        temp_factor = 0.9
    elif row['temperature'] > 28:
        temp_factor = 1.3
    
    # Humidity effect (lower humidity = more water needed)
    humidity_factor = 1.0 - (row['humidity'] - 70) / 200  # Normalize around 70%
    humidity_factor = max(0.7, min(1.3, humidity_factor))
    
    # Soil quality effect (better nutrients = slightly less water needed)
    npk_avg = (row['N'] + row['P'] + row['K']) / 3
    soil_factor = 1.0 - (npk_avg - 50) / 500  # Normalize around 50
    soil_factor = max(0.85, min(1.15, soil_factor))
    
    # pH effect (optimal pH = less water stress)
    ph_optimal = 6.5
    ph_factor = 1.0 - abs(row['ph'] - ph_optimal) / 20
    ph_factor = max(0.9, min(1.1, ph_factor))
    
    water_req = base_water * temp_factor * humidity_factor * soil_factor * ph_factor
    
    # Add some randomness to make it more realistic
    water_req += np.random.normal(0, water_req * 0.1)
    
    return max(20, min(350, water_req))  # Clamp between 20-350 mm

df['water_requirement'] = df.apply(calculate_water_requirement, axis=1)
print(f"   ✓ Water requirement range: {df['water_requirement'].min():.1f} - {df['water_requirement'].max():.1f} mm")

# Create classification target based on water requirement vs rainfall
print("\n[5/6] Creating classification labels...")
def classify_irrigation(row):
    """
    Classify irrigation urgency:
    - Irrigate Now: deficit > 40mm (urgent - 30% of typical weekly need)
    - Irrigate Soon: deficit > 15mm (soon - 10% of typical weekly need)
    - No Irrigation Needed: deficit <= 15mm (adequate)
    """
    deficit = row['water_requirement'] - row['rainfall']
    
    # More realistic thresholds based on percentage of water need
    water_req = row['water_requirement']
    deficit_percent = (deficit / water_req * 100) if water_req > 0 else 0
    
    # Use both absolute and relative thresholds
    if deficit > 40 or deficit_percent > 30:
        return "Irrigate Now"
    elif deficit > 15 or deficit_percent > 10:
        return "Irrigate Soon"
    else:
        return "No Irrigation Needed"

df['irrigation_decision'] = df.apply(classify_irrigation, axis=1)
print(f"   ✓ Classification distribution:")
print(df['irrigation_decision'].value_counts().to_string())

# Prepare features
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'crop_encoded']
X = df[features]
y_regression = df['water_requirement']
y_classification = df['irrigation_decision']

# Split data
X_train, X_test, y_reg_train, y_reg_test, y_clf_train, y_clf_test = train_test_split(
    X, y_regression, y_classification, test_size=0.2, random_state=42, stratify=y_classification
)

print(f"\n   ✓ Training set: {len(X_train)} samples")
print(f"   ✓ Test set: {len(X_test)} samples")

# Train Regression Model
print("\n[6/6] Training models...")
print("\n   Training Regression Model...")
reg_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
reg_model.fit(X_train, y_reg_train)
y_reg_pred = reg_model.predict(X_test)
r2 = r2_score(y_reg_test, y_reg_pred)
print(f"   ✓ Regression R² Score: {r2:.4f}")

# Train Classification Model
print("\n   Training Classification Model...")
clf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
clf_model.fit(X_train, y_clf_train)
y_clf_pred = clf_model.predict(X_test)
accuracy = accuracy_score(y_clf_test, y_clf_pred)
print(f"   ✓ Classification Accuracy: {accuracy:.4f}")

# Print detailed classification report
print("\n   Classification Report:")
print(classification_report(y_clf_test, y_clf_pred))

# Save models
print("\n[7/7] Saving models...")
with open('models/regression_model.pkl', 'wb') as f:
    pickle.dump(reg_model, f)
print("   ✓ Saved regression_model.pkl")

with open('models/classification_model.pkl', 'wb') as f:
    pickle.dump(clf_model, f)
print("   ✓ Saved classification_model.pkl")

with open('models/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
print("   ✓ Saved label_encoder.pkl")

print("\n" + "=" * 60)
print("Training completed successfully!")
print("=" * 60)
print("\nModel Performance Summary:")
print(f"  • Regression R² Score: {r2:.4f} ({r2*100:.2f}%)")
print(f"  • Classification Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
print("\nModels saved to 'models/' directory")
print("You can now run the Streamlit app: streamlit run app.py")

