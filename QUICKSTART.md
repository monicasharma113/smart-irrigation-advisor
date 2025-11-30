# Quick Start Guide 🚀

## Installation & Setup (5 minutes)

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed.
```bash
python --version
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## Project Structure

```
mpr/
├── app.py                      # Main home page
├── train_model.py              # Model training script
├── pages/                      # Additional pages
│   ├── 2_Irrigation_Advisor.py # Main feature page
│   ├── 3_FAQs.py              # FAQ page
│   └── 4_Dataset.py           # Data explorer
├── models/                     # ML models (already included)
├── data/                       # Dataset (already included)
└── requirements.txt            # Dependencies
```

## Training Models (Optional)

If you need to retrain the models:
```bash
python train_model.py
```

**Note:** Pre-trained models are already included, so training is optional.

## Troubleshooting

**Port already in use?**
```bash
streamlit run app.py --server.port 8502
```

**Models not loading?**
- Check that all `.pkl` files are in the `models/` folder
- Verify file paths in the code

**Module not found?**
```bash
pip install -r requirements.txt
```

## Next Steps

1. Open the app in your browser
2. Navigate to "Irrigation Advisor" from the sidebar
3. Enter your field data and get recommendations!

For detailed documentation, see `README.md`

