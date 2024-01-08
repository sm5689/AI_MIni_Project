# Diet Recommendation System

## Overview
The Diet Chart Recommendation System is an innovative application designed to provide personalized diet recommendations based on a user's physical attributes and dietary preferences. Utilizing Python, Pandas, NumPy, Tkinter, Sklearn's KMeans clustering, and RandomForestClassifier, this system processes user data and suggests optimal dietary options.

## Features
- **User Input Interface**: Built with Tkinter, it allows users to input age, dietary preference (vegetarian or non-vegetarian), weight, and height.
- **BMI Calculation**: Calculates Body Mass Index (BMI) to categorize the user's weight status.
- **Diet Recommendations**: Based on the BMI and user data, it suggests suitable food items for weight loss, weight gain, or maintaining a healthy diet.

## Functionality
- **Data Handling**: Uses Pandas and NumPy for data manipulation and analysis.
- **K-Means Clustering**: Segregates food items based on their nutritional content.
- **Random Forest Classifier**: Predicts the category of food suitable for the user's diet plan.

## How It Works
1. **Data Loading**: Reads food data from 'food.csv' and nutritional distribution from 'nutrition_distriution.csv'.
2. **User Data Collection**: Tkinter interface to collect user inputs.
3. **BMI Analysis**: Determines the user's weight category.
4. **Diet Category Identification**: Uses K-Means to classify food items and RandomForestClassifier to suggest a diet based on the user's goal (Weight Loss, Weight Gain, Healthy Living).

## Usage
The application can be used by anyone looking for a personalized diet recommendation. It's particularly useful for individuals focusing on weight management or maintaining a healthy lifestyle.

## Installation
1. Clone the repository.
2. Install required libraries: `pandas`, `numpy`, `sklearn`, `tkinter`.
3. Run the script to start the application.

## Limitations
- The recommendations are based on general nutritional data and may not consider specific health conditions or allergies.
- The GUI is basic and might not provide the most user-friendly experience.

## Future Enhancements
- Incorporating a more advanced and user-friendly GUI.
- Adding a feature to consider user allergies and health conditions.
- Integrating with fitness trackers for real-time health data analysis.

---

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Sklearn](https://img.shields.io/badge/Sklearn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-306998?style=for-the-badge&logo=python&logoColor=white)

*Note: The stickers are for visual representation only and do not imply any official endorsement.*
