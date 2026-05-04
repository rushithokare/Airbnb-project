# Airbnb Price Prediction and Analysis

A comprehensive data analysis and machine learning project to understand Airbnb listings and predict rental prices. This project uses exploratory data analysis (EDA) and advanced feature engineering to build a price prediction model.

## Project Overview

This project analyzes Airbnb listings data to:
- Understand listing characteristics and pricing patterns
- Identify key factors influencing rental prices
- Build a predictive model for listing prices using machine learning
- Generate insights for hosts and analysts

## Project Structure

```
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── notebooks/                         # Jupyter notebooks for analysis
│   ├── 01_data_loading.ipynb         # Load raw data and initial exploration
│   ├── 02_data_cleaning.ipynb        # Data cleaning and preprocessing
│   ├── 03_eda.ipynb                  # Exploratory Data Analysis
│   ├── 03_advanced_eda.ipynb         # Advanced EDA visualizations
│   ├── 04_feature_engineering.ipynb  # Feature creation and transformation
│   └── 05_modeling.ipynb             # Model training and evaluation
├── src/                              # Reusable Python modules
│   ├── data_cleaning.py              # Data cleaning functions
│   ├── feature_engineering.py        # Feature engineering utilities
│   ├── modeling.py                   # Model training and evaluation
│   └── utils.py                      # General utility functions
├── data/                             # Data directory
│   ├── raw/                          # Original datasets
│   │   ├── listings.csv              # Airbnb listing information
│   │   ├── reviews.csv               # Guest reviews and ratings
│   │   ├── calendar.csv              # Booking calendar data
│   │   └── neighbourhoods.csv        # Neighborhood information
│   └── processed/                    # Cleaned and processed data
│       ├── cleaned_listings.csv      # Processed listings data
│       └── merged_data.csv           # Combined dataset
├── models/                           # Saved model artifacts
├── dashboards/                       # Dashboard configurations (if any)
├── reports/                          # Generated reports and visualizations
└── images/                           # Project images and screenshots
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook/Lab

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd "c:\Users\thoka\Downloads\Airbnb project"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Data Overview

### Raw Data Files

- **listings.csv** - Core listing information including:
  - Property details (bedrooms, bathrooms, amenities)
  - Pricing information
  - Host information
  - Location and neighborhood data

- **reviews.csv** - Guest reviews containing:
  - Listing IDs and review dates
  - Review text and ratings
  - Reviewer information

- **calendar.csv** - Booking availability data:
  - Daily availability status
  - Pricing variations
  - Booking patterns

- **neighbourhoods.csv** - Neighborhood information:
  - Neighborhood names and boundaries
  - Geographic data

### Processed Data

- **cleaned_listings.csv** - Preprocessed listings with:
  - Missing values handled
  - Data type conversions
  - Cleaned price information
  - Feature normalization

- **merged_data.csv** - Combined dataset with:
  - Listings and review aggregations
  - Calendar features
  - Neighborhood attributes

## Notebooks

Follow these notebooks in order for a complete analysis:

### 1. 01_data_loading.ipynb
- Load raw CSV files
- Initial data shape and structure exploration
- Preview of data samples
- Basic data integrity checks

### 2. 02_data_cleaning.ipynb
- Handle missing values
- Data type conversions (e.g., price to numeric)
- Remove duplicates and invalid records
- Clean text fields

### 3. 03_eda.ipynb & 03_advanced_eda.ipynb
- Summary statistics and distributions
- Correlation analysis
- Price distribution by features
- Location-based analysis
- Amenities and their impact on pricing
- Time-based trends

### 4. 04_feature_engineering.ipynb
- Create derived features from raw data
- Encode categorical variables
- Aggregate review statistics
- Build temporal features
- Create neighborhood-based features

### 5. 05_modeling.ipynb
- Train predictive models
- Model evaluation and comparison
- Feature importance analysis
- Price prediction results
- Model performance metrics

## Source Modules

### data_cleaning.py
Reusable functions for data preprocessing:
- `clean_price()` - Convert currency text to numeric values

### feature_engineering.py
Feature creation and transformation utilities

### modeling.py
Machine learning model utilities:
- `train_model()` - Train RandomForestRegressor for price prediction
- `save_model()` - Save trained models to disk

### utils.py
General utility functions for the project

## Model Details

### Price Prediction Model
- **Algorithm:** Random Forest Regressor
- **Target Variable:** Listing price
- **Approach:** Supervised learning regression
- **Model Storage:** Saved as `models/price_model.pkl`

### Key Features Used
- Property characteristics (bedrooms, bathrooms, type)
- Amenities
- Location/neighborhood data
- Review ratings and counts
- Availability patterns

## Usage

### Running the Analysis

1. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Run notebooks sequentially** (01 → 05) for the complete workflow

3. **Train and save a model:**
   ```python
   from src.modeling import train_model, save_model
   
   # Assuming X_train, y_train are prepared
   model = train_model(X_train, y_train)
   save_model(model, "../models/price_model.pkl")
   ```

4. **Use for predictions:**
   ```python
   import joblib
   model = joblib.load("models/price_model.pkl")
   predictions = model.predict(X_new)
   ```

## Key Findings

*Add your analysis findings and insights here as you complete the project*

- Price distribution and patterns
- Most important factors affecting pricing
- Seasonal trends
- Location-based pricing differences
- Recommendations for hosts

## Dependencies

Main libraries used in this project:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning
- **matplotlib** & **seaborn** - Data visualization
- **joblib** - Model serialization

See `requirements.txt` for the complete list.

## Next Steps

- [ ] Add specific requirements to requirements.txt
- [ ] Train and evaluate final model
- [ ] Generate insights and visualizations
- [ ] Create interactive dashboard
- [ ] Document key findings and recommendations
- [ ] Test model on new data

## Author

*Your Name/Team*

## License

*Specify license if applicable*

## Contributing

Contributions are welcome! Please follow these guidelines:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## Questions or Issues

For questions about this project, please [create an issue or contact the maintainers].
