from flask import Flask, render_template , request
import pandas as pd
from recommender import get_recommendations
from pathlib import Path


app = Flask(__name__)
BASE_DIR = Path(__file__).parent
INPUT_CSV = BASE_DIR/"main_books.csv"

@app.route('/')
def index():
    return render_template('homepage.html')  

@app.route('/recommendations')
def recommendations():
    genre = request.args.get("genre")
    mood = request.args.get("mood")
    #calling function
    books = get_recommendations(genre,mood)
    return render_template('recommendation.html',books=books,genre=genre,mood=mood)
     
if __name__ == '__main__':
    app.run(debug=True)   
