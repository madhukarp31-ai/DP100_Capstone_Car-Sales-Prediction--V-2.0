# 🚗 DP-100 Capstone Project: Car Sales Price Prediction

This project is part of the **DP-100: Designing and Implementing a Data Science Solution on Azure** certification lab. It demonstrates an end-to-end machine learning workflow on **Azure Machine Learning Studio**, using a sample **car sales dataset** to predict car prices based on various vehicle features.

---

## 🧠 Project Objective

To build, train, evaluate, register, and optionally deploy a regression model that predicts car prices using Azure Machine Learning services, Python, and Scikit-learn.

---

## 🚀 Activities Completed

### ✅ Phase 1: Data Preparation
- Loaded the dataset `car_sales.csv` into a Pandas DataFrame  
- Inspected dataset structure and identified missing values  
- Handled missing values:
  - Imputed missing values for `Rear.seat.room` and `Luggage.room` using **mean**  
- Dropped any remaining nulls for clean training  
- Performed **train-test split** (80/20)  
- Saved cleaned training and test datasets  

### ✅ Phase 2: Model Training & Evaluation
- Trained a **Linear Regression** model using **Scikit-learn**  
- Evaluated model using:
  - **Root Mean Squared Error (RMSE)**  
  - **R-squared (R²)**  
- Plotted **Actual vs Predicted** values using Matplotlib  
- Saved the model as `car_price_model.pkl`  

### ✅ Phase 3: Model Registration & Deployment
- Registered the trained model to Azure ML Workspace  
- Created a **scoring script (`score.py`)** for deployment  
- Defined the **environment dependencies** using `environment.yml`  
- Attempted deployment to **Azure Container Instance (ACI)**  
  - ⚠️ Deployment was skipped due to **Azure trial subscription limitations**

---

## ⚙️ Phase 4: CI/CD with GitHub Actions (MLOps Automation)

Integrated a GitHub Actions workflow to automate model training and registration via Azure ML SDK v2:

- ✅ Created `.github/workflows/azureml_train_register.yml`
- ✅ Configured the pipeline to:
  - Authenticate with Azure using secrets
  - Submit training job to Azure ML
  - Optionally register the model to the workspace
- ✅ Secrets configured in GitHub:
  - `AZURE_CREDENTIALS`
  - `AZURE_SUBSCRIPTION_ID`
  - `AZURE_RESOURCE_GROUP`
  - `AZURE_WORKSPACE_NAME`
- Manual trigger enabled using `workflow_dispatch` event

---

## 🧰 Tools & Technologies Used

- **Azure Machine Learning Studio** (SDK & Portal)  
- **Python 3.x**  
- **Pandas**, **NumPy**, **Scikit-learn**, **Matplotlib**, **Seaborn**  
- **Jupyter Notebooks**  
- **Azure CLI / az ml**  
- **Git & GitHub**  
- **GitHub Actions** for CI/CD automation

---

## 🔗 Repository

GitHub: [DP100_Capstone_Car-Sales-Prediction--V-2.0](https://github.com/madhukarp31-ai/DP100_Capstone_Car-Sales-Prediction--V-2.0)

---

## 📌 Status

✅ Development completed  
🚧 Deployment testing pending Azure subscription upgrade  
✅ GitHub Actions pipeline configured  
📝 Release versioning will follow after successful end-to-end testing


