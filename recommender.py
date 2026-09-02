import pandas as pd
import ast 
from pathlib import Path

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).parent
INPUT_CSV = BASE_DIR/"main_books.csv"


#Striping the spaces and making them all lower case so it is easier for testing 
def normalization(value):
    if pd.isna(value):
        return []
    try:
        return ast.literal_eval(value)
    except (ValueError,SyntaxError):
        return []


#----- Load Books ----
def load_books():
    books = pd.read_csv(INPUT_CSV)
    books["genre"] = books["genre"].apply(normalization)
    books["mood"] = books["mood"].apply(normalization)

    return books
def features(books):
    # Combine the genre list,mood list and the book title into one text so that TF-IDF can understand
    books["features"] = books.apply(
        lambda book:
        " ".join(book["genre"]) + " " + " ".join(book["mood"]) + " " + str(book["title"]),axis=1
    )# Apply this to every book

    # Return the dataframe with new "features" column
    return books
#------ Recommendation ----
def get_recommendations(genre, mood):
    books = load_books()

    if not genre or not mood:
        return []
    
    # find books matching the mood
    genre_books = books[books["genre"].apply(lambda genres: genre in genres)]
    mood_books = genre_books[genre_books["mood"].apply(lambda moods: mood in moods)]

    mood_books = mood_books.dropna(subset=["average_rating"])

    # return the best-rated books
    recommendations = mood_books.sort_values(by="average_rating",ascending=False).head(10)

    result = recommendations.to_dict(orient="records")

    return result
