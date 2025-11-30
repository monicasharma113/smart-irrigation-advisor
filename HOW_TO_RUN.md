# How to Run Smart Irrigation Advisor 🚀

## Quick Start (3 Steps)

### Step 1: Install Dependencies
Open terminal/command prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Open in Browser
The app will automatically open at `http://localhost:8501`

---

## Detailed Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Option 1: Run Directly (Recommended)

1. **Open Terminal/Command Prompt**
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac: Open Terminal app
   - Linux: Open Terminal

2. **Navigate to Project Folder**
   ```bash
   cd C:\Users\Monica\OneDrive\Desktop\mpr
   ```

3. **Install Dependencies** (First time only)
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

5. **Use the App**
   - Browser will open automatically
   - If not, go to: `http://localhost:8501`
   - Use the sidebar to navigate between pages

### Option 2: Using Virtual Environment (Recommended for Isolation)

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

5. **Deactivate (when done)**
   ```bash
   deactivate
   ```

---

## Optional: Train Models

If you want to retrain the models (models are already included, so this is optional):

```bash
python train_model.py
```

This will:
- Train regression and classification models
- Save them to `models/` folder
- Show performance metrics

---

## Troubleshooting

### Port Already in Use
If port 8501 is busy, use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found Error
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Models Not Loading
- Check that `models/` folder contains:
  - `classification_model.pkl`
  - `regression_model.pkl`
  - `label_encoder.pkl`
- If missing, run: `python train_model.py`

### Python Not Found
- Make sure Python is installed and in PATH
- Try: `python --version` or `python3 --version`

### Permission Errors (Windows)
Run Command Prompt as Administrator

---

## What You'll See

1. **Home Page** - Overview and features
2. **Irrigation Advisor** - Main tool to get recommendations
3. **FAQs** - Common questions
4. **Dataset** - Explore training data

---

## Using the Irrigation Advisor

1. Go to "Irrigation Advisor" from sidebar
2. Select crop type (Rice or Maize)
3. Enter:
   - Temperature (°C)
   - Humidity (%)
   - Recent Rainfall (mm)
   - Soil nutrients (N, P, K)
   - Soil pH
4. Click "Analyze"
5. View recommendations!

---

## Need Help?

- Check `README.md` for detailed documentation
- Check `QUICKSTART.md` for quick reference
- Review the FAQs page in the app

