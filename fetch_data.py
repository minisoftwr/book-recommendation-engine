import requests
import pandas as pd
import time

books = pd.read_csv("cleaned_books.csv")
results = []

books["isbn13"] = (books["isbn13"].astype(str).str.replace(".0","",regex=False))


MOOD = {
    "Fantasy": ["Surreal", "Thrilling", "Whimsical", "Light"],
    "Horror": ["Dark", "Thrilling"],
    "Romance": ["Romantic", "Light", "Happy"],
    "Mystery": ["Dark", "Thrilling"],
    "Self-Help": ["Thought-provoking", "Light", "Lost", "Happy"],
    "Coming of age": ["Sad", "Thought-provoking", "Lost"],
    "Historical Fiction": ["Thought-provoking", "Sad", "Dark"],
    "Biography": ["Thought-provoking", "Happy", "Sad"],
    "Magic": ["Surreal", "Light", "Whimsical"],
    "Friendship": ["Light", "Happy", "Romantic"],
    "Family": ["Sad", "Light", "Happy"],
    "Young Adult": ["Light", "Thrilling", "Happy"],
    "Science Fiction": ["Surreal", "Thrilling", "Thought-provoking"],
    "Fiction": ["Light", "Happy", "Thought-provoking"],
    "History": ["Thought-provoking", "Dark"],
}
 
ALLOWED_GENRES = ["Fantasy", "Science Fiction", "Mystery", "Romance","Literary Fiction",
                  "Historical Fiction", "Horror", "Young Adult",
                  "Biography", "Self-Help", "History", "Fiction",
                  "Coming of age", "Friendship", "Magic", "Family","Non Fiction"]

 
for isbn in books["isbn13"].head(17):
    try:
        isbn = str(isbn).split(".")[0]
        # your code goes here
        response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data",timeout=10)
        data = response.json()
        book_data = data[f"ISBN:{isbn}"]
        #--------Genre------------
        subjects = book_data["subjects"]
        genre = [x["name"] for x in subjects if x["name"] in ALLOWED_GENRES and len(x["name"])< 20 and ":" not in x["name"] and "(" not in x["name"]]
        genre = list(set(genre)) #no duplicates
        mood = []
        for x in genre:
            mood  += MOOD.get(x,[])
        mood = list(set(mood))
        #---- image-----
        image = book_data["cover"]["medium"]
        #-----title------
        title=book_data['title']
        #---------Save data------
        results.append({
            "isbn13": isbn,
            "openlibrary_title":title,
            "genre":genre,
            "image":image,
            "mood":mood})
        time.sleep(0.5)
    except Exception as e:
        print(f"Skipping {isbn} - {e}")
        continue
enriched = pd.DataFrame(results)
#-- merge with cleaned data
books["isbn13"] = (books["isbn13"].astype(str).str.replace(".0","",regex=False))
enriched ["isbn13"] =(enriched["isbn13"].astype(str))

main_books = books.merge(enriched[["isbn13",
                                   "genre",
                                   "mood",
                                   "image"
                                   ]
                                ],
                                on="isbn13",how="left")
#-----Final book set-----
main_books.to_csv("main_books.csv", index=False)

print("\nDone!")
print(f"Orginal cleaned books: {len(books)}")
print(f"Enriched books: {len(enriched)}")
print(f"Final book: {len(main_books)}")