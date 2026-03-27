import pandas as pd

df = pd.read_csv("books.csv")

print("\nAll Books Data:")
print(df)

author_name = input("\nEnter author name: ")
print(df[df['author'] == author_name])

publisher_name = input("\nEnter publisher name: ")
print(df[df['publisher'] == publisher_name])

print("\nCheapest Book:")
print(df[df['price'] == df['price'].min()])

print("\nCostliest Book:")
print(df[df['price'] == df['price'].max()])

print("\nSorted by Year:")
print(df.sort_values(by='year'))