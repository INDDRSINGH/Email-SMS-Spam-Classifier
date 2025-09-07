# Email-SMS-Spam-Classifier

![DatabaseSchema](https://github.com/INDDRSINGH/Email-SMS-Spam-Classifier/blob/main/email%20logo.jpg)

##  Overview  
This project uses machine learning to classify given text as **“SPAM”** or **“NOT SPAM”**. Built using Python's NLP tools and deployed via a web interface, it demonstrates a complete pipeline—from data ingestion to model deployment.

##  Project Goals  
- Train a reliable spam classifier to enhance communication filtering  
- Showcase core analytics and ML skills: data preprocessing, model evaluation, and deployment  
- Deliver an interactive application accessible through a web browser

##  Tools & Technologies  
- **Python**  
- **Jupyter Notebook** for experimentation  
- **Pandas & Numpy** for data handling  
- **NLTK** (for stemming/tokenization)  
- **TF-IDF Vectorizer** for feature extraction  
- **Multinomial Naive Bayes** classifier  
- **scikit-learn** for model training and evaluation  
- **Streamlit** for web app (via `app.py`)  
- **Render** for cloud deployment  
- **Pickle** for model persistence (`model.pkl`, `tfidf.pkl`)

##  Project Flow  
1. **Data Loading & Exploration**  
   - Loaded dataset from Kaggle, performed exploratory analysis (text length, word frequency, class balance)  
2. **Preprocessing**  
   - Cleaned text (lowercasing, punctuation removal)  
   - Applied stemming using NLTK  
   - Vectorized text using TF-IDF  
3. **Model Training**  
   - Evaluated Multiple ML algorithms  
   - Selected Multinomial Naive Bayes as the best-performing model  
4. **Evaluation**  
   - Metrics: accuracy, precision, recall, F1-score (found in Jupyter Notebook)  
   - Visualized results with confusion matrix  
5. **Deployment**  
   - Built a Streamlit app to expose prediction interface  
   - Deployed live to Render (viewable at the project’s GitHub link)

##  Live Demo  
Try the classifier live [here](https://email-sms-spam-classifier-meag.onrender.com)

## Dataset
- **Source**: Kaggle ([Link](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=CEAS_08.csv))
- **Contains labeled text messages/emails (spam vs. ham)**

## Key Insights
- Stemming helps reduce vocabulary size and improves model generalization
- TF-IDF provides a strong representation behind Naive Bayes for text classification
- The classifier shows high precision on spam detection (specific metrics available in notebook)

## What I Learned
- Hands-on experience with NLP preprocessing and feature engineering
- Practical model selection and evaluation methods
- Building and deploying a production-ready ML web app using Streamlit



- Managing end-to-end ML workflow from Jupyter to live deployment

