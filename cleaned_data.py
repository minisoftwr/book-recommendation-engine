import pandas as pd
import csv


def clean_book():
    file_path = "books.csv"
    rows = []

    with open(file_path,"r",encoding="utf-8",newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            #Header
            if row[0] == "bookID":
                rows.append(row)
                continue
            #Normal row
            if len(row) == 12:
                rows.append(row)
            # Rows containing an extra comma
            elif len(row) == 13:
                row[2] = row[2] + "," + row[3]
                row.pop(3)
                rows.append(row)
    #Create dataframe
    df = pd.DataFrame(
        rows[1:],
        columns=rows[0]
    )

    df = df.drop_duplicates(subset=["bookID"])

    #Remove the books without title
    df = df.dropna(subset=["title"])
    # Remove invalide reviews
    df["average_rating"] = pd.to_numeric(df["average_rating"],errors="coerce")
    df = df[df["average_rating"] .between(0,5)]
    # drop books with non isb3 as cant be used 
    df = df.dropna(subset=["isbn13"])
    #renaming language code to language
    df = df.rename(columns={"language_code":"language"})
    language_map ={"eng":"English","en-US":"English","en-GB":"English","jpn":"Japanese","jap":"Japanese"}

    df["language"] = (df["language"].map(language_map).fillna("Unknown"))

    #the text columns
    text_col= ["title","authors","publisher"]

    #Ensure the follwing columns are numerical
    num_col =["ratings_count","text_reviews_count","num_pages"]
    # cleaning the Text columns
    for col in text_col:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
            df[col] = df[col].str.strip()
    # Cleaning the  numerical columns
    for col in num_col:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col],errors="coerce")
            df[col] = df[col].astype(int)
    # clean publication date using datetime()
    df["publication_date"] = pd.to_datetime(df["publication_date"],errors="coerce")

    # Resitng the old index number to the new one 
    df = df.reset_index(drop=True)
    return df

if __name__ == "__main__":
    print(" Data Cleaning")
    books = clean_book()
    print("\nFinal Columns:")
    print(books.columns.tolist())
    books.to_csv("cleaned_books.csv",index=False)
    print("The Cleaned Data is saved as cleaned_csv")





     


