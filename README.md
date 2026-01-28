Customer Segmentation using K-Means

## Project Overview

This project implements **Customer Segmentation** using the **K-Means clustering algorithm**. The goal is to group customers into meaningful segments based on their demographic information, spending behavior, and engagement metrics. These segments can help businesses design targeted marketing strategies and improve customer retention.

The project covers the **entire machine learning lifecycle**:

* Data preprocessing & feature engineering
* Model training using K-Means
* Model serialization
* Deployment using **Streamlit** for real-time predictions

---

## Tech Stack

* **Python 3.10 / 3.11**
* **scikit-learn** – K-Means, StandardScaler
* **pandas, numpy** – Data processing
* **matplotlib, seaborn** – Visualization
* **joblib** – Model persistence
* **Streamlit** – Deployment

---

## Project Structure

```
Customer_Segmentation_Project/
│
├── Customer Segmentation.ipynb              # EDA + Feature Engineering + Modeling
├── Customer_Segmentation_Deployment.ipynb   # Deployment logic validation
├── app.py                                   # Streamlit application
├── scaler.pkl                               # Saved StandardScaler
├── kmeans_model.pkl                         # Trained K-Means model
├── requirements.txt                         # Project dependencies
└── README.md                                # Project documentation
```

---

## Dataset Description

The dataset contains customer demographic, spending, and interaction information. Key preprocessing steps include:

* Handling missing values (Income)
* Outlier treatment using IQR capping
* Feature engineering (Age, Total_Spent, Total_Purchases, Children, Tenure)
* Encoding categorical features (Education)

---

## Features Used for Clustering

The final K-Means model was trained using the following features **in this exact order**:

1. Income
2. Age
3. Total_Spent
4. Children
5. Tenure_Days
6. NumWebVisitsMonth
7. Education

⚠️ **Important:** This feature order is strictly maintained during deployment to ensure correct predictions.

---

## Model Training

* Algorithm: **K-Means Clustering**
* Optimal number of clusters selected using:

  * Elbow Method (WCSS)
  * Silhouette Score
* Final model trained with **4 clusters**
* Data scaled using **StandardScaler** before clustering

---

## Model Serialization

The trained model and scaler were saved using `joblib`:

* `scaler.pkl` – Stores feature scaling parameters
* `kmeans_model.pkl` – Stores trained K-Means cluster centroids

These files are reused during deployment without retraining.

---

## Deployment (Streamlit)

The project is deployed locally using **Streamlit**, allowing users to input customer details and instantly receive a predicted customer segment.

### Steps to Run the Application

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

4. Open the browser link displayed in the terminal to access the application.

---

## How Prediction Works

1. User enters customer details via Streamlit UI
2. Input data is converted into a NumPy array
3. Data is scaled using the saved `StandardScaler`
4. The scaled data is passed to the trained K-Means model
5. The predicted cluster label is returned as the customer segment

---

## Output

* The application displays a **Customer Segment (Cluster ID)** ranging from 0 to 3
* Each segment represents a distinct customer behavior group identified during analysis

---

## Key Notes

* The model **does not retrain** during deployment
* The same scaler and feature order used in training are reused
* This deployment demonstrates a **complete and correct ML workflow**

---

## Future Improvements

* Map clusters to business-friendly labels (e.g., High Value, Low Engagement)
* Add cluster visualization in the Streamlit app
* Deploy the app on Streamlit Cloud or similar platforms

---

## Author

**Customer Segmentation Project**
Machine Learning | K-Means Clustering | Streamlit Deployment
