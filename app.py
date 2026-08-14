from flask import Flask, render_template , request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')  

@app.route('/recommendations')
def recommendations():
    try:
        genre = request.args.get('genre')
        df = pd.read_csv("enriched_books.csv")
        #Filtering the dataframe 
        filtering = df[df['genre'] == genre].head(20)
        # converting the list into a dictionary
        books = filtering.to_dict(orient ='records')
    except Exception as e:
        print(f"Error: {e}")
        return render_template("homepage.html")
    
    return render_template('recommendations.html',books=books,genre=genre)    

if __name__ == '__main__':
    app.run(debug=True)   
