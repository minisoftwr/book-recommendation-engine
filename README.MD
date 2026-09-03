# Book Recommendation Engine
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-2e7d32?style=flat-square)

## What it does

This Book Recommendation Engine was built using Flask and Python. The project uses the dataset from Kaggle and enriches the dataset using Open Library API.This was necessary because some of the information required for the recommendation system,such as book genres and cover images, was not available in the origanl dataset.After cleaning and processing the data, the application recommends books based user's selected **genre** and **mood**.
The recommendation system uses **TF-IDF** and **Cosine Similarity** to compare user preferences with book features and rank the most relevant books.

---
### Features 

 - **TF-IDF :** This method is used to evaluate how important a word is to the document in relation to a larger collection.
 - **Cosine Similarity :** This is a metric used to measure the similiarity between the two vectors irrespctive of their sizes.
 - **Mood Filtering :** Each genre is mapped to set of moods. Books are filtered to only return the results that match the selected  genre and mood, ensuring that the recommendation is precise.
---
### Dataset Enrichment
The original dataset was enriched using the Open Library API to obtain additional information.
- Book genres
- Book cover images
- Additional book metadata
---
### How to run it
*Ensure the python version3 is used.*

### 1. Clone the repository
```bash
git clone https://github.com/minisoftwr/book-recommendation-engine.git 
cd book-recommendation-engine
```

### 2. Install dependencies 
```bash
pip install -r requirement.txt
```
### 3. Run
```bash
python app.py
```
then navigate to :   
http://127.0.0.1:5000
### What I learned
---
- How to clean and preprocess a real-world dataset.
- How to enrich a dataset using an external API(Open Library) when the original dataset is missing key fields.
- How **TF-IDF** converts the text into numerical vectors so it can be mathematically compared.
- How to map the genre by ranking them by similarity.
- How **Cosine Similarity** measures the angle between the two vectors to find the closet matching book. If the angle is 0 degrees, then the two vectors overlap proving similarity. 
- How to build and deploy a full-stack Flask web application.
---
### Future Improvements
- Improving the mood classification system.
- Adding the user accounts and saving the users recommendation history.
- Allow the users to enter books they have previously read.
