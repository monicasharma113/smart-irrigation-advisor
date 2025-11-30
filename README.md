# Smart Irrigation Advisor 💧

A Streamlit-based web application that provides intelligent irrigation recommendations for crops using machine learning models. The system analyzes environmental conditions, soil parameters, and crop type to suggest optimal irrigation timing and water requirements.

## Features

- 🌾 **Crop Support**: Currently supports Rice and Maize
- 📊 **Data-Driven**: Uses ML models trained on real crop data
- 🎯 **High Accuracy**: 97.5% classification accuracy, 100% R² score
- 💡 **User-Friendly**: Simple interface with sliders and dropdowns
- 📈 **Visualizations**: Interactive charts showing prediction confidence
- ❓ **Comprehensive FAQs**: Answers to common questions

## Project Structure

```
mpr/
├── app.py                      # Main Streamlit application entry point
├── train_model.py              # Script to train ML models
├── pages/                      # Streamlit pages
│   ├── 2_Irrigation_Advisor.py # Main irrigation recommendation page
│   ├── 3_FAQs.py              # Frequently asked questions
│   └── 4_Dataset.py           # Dataset explorer
├── models/                     # Trained ML models
│   ├── classification_model.pkl
│   ├── regression_model.pkl
│   └── label_encoder.pkl
├── data/                       # Dataset files
│   └── Crop_recommendation.csv
├── .streamlit/                 # Streamlit configuration
│   └── config.toml
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or download this repository**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Training the Models (Optional)

If you want to retrain the models or the model files are missing:

1. **Run the training script**
   ```bash
   python train_model.py
   ```

2. **The script will:**
   - Load and filter the dataset (Rice and Maize only)
   - Create synthetic water requirement targets
   - Create classification labels (Irrigate Now/Soon/Not Needed)
   - Train both regression and classification models
   - Save models to the `models/` directory

3. **Expected output:**
   - Regression R² Score: ~0.99+ (very high accuracy)
   - Classification Accuracy: ~0.95+ (high accuracy)

**Note:** The pre-trained models are already included in the `models/` folder, so you typically don't need to run this unless you want to retrain with different parameters or data.

## Running the Application

1. **Make sure you're in the project root directory**

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```
   

3. **The application will open in your default web browser**
   - Default URL: `http://localhost:8501`

## Usage

1. **Navigate to "Irrigation Advisor"** from the sidebar
2. **Select your crop type** (Rice or Maize)
3. **Input environmental conditions**:
   - Temperature (°C)
   - Humidity (%)
   - Recent Rainfall (mm)
4. **Input soil parameters**:
   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Soil pH
5. **Click "Analyze"** to get recommendations
6. **Review the results**:
   - Irrigation status (Irrigate Now / Soon / Not Needed)
   - Weekly water requirement
   - Extra irrigation needed
   - Prediction confidence
   - Optimal timing suggestions

## Model Details

- **Regression Model**: Predicts weekly water requirement (mm) based on 8 parameters
- **Classification Model**: Classifies irrigation urgency into 3 categories
- **Label Encoder**: Encodes crop types for model input

### Input Parameters
- N, P, K (soil nutrients)
- Temperature, Humidity, Rainfall
- Soil pH
- Crop type (Rice/Maize)

### Output
- Weekly water requirement (mm)
- Extra irrigation needed (mm)
- Irrigation recommendation (Now/Soon/Not Needed)
- Confidence scores

## Technologies Used

- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning models
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **plotly**: Interactive visualizations

## Troubleshooting

### Models not loading
- Ensure all `.pkl` files are in the `models/` directory
- Check file paths in the code match your directory structure

### Data file not found
- Ensure `Crop_recommendation.csv` is in the `data/` directory

### Port already in use
- Streamlit will automatically try the next available port
- Or specify a different port: `streamlit run app.py --server.port 8502`

## Future Enhancements

- Support for more crop types (wheat, cotton, sugarcane, etc.)
- Integration with weather APIs for automatic data input
- Historical data tracking and analysis
- Mobile app version
- Multi-language support

## License

This project is open source and available for educational and research purposes.

## Contact

For questions or issues, please refer to the FAQs page in the application or create an issue in the repository.

---

**Note**: This tool is designed as a decision support system and should be used in conjunction with local agricultural expertise and field experience.

