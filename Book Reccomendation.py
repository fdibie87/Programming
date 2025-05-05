import csv

'''Function to load dataset into dictionaries'''
def reading_the_book(file_name):
    with open(file_name,'r',encoding='utf-8-sig') as file:
        # Use 'utf-8-sig' to handle files with a Byte Order Mark (BOM),
        # ensuring compatibility with programs like Excel and proper encoding of special characters.
        reader = csv.DictReader(file)
        books=[dict(row) for row in reader]
    return books
books = reading_the_book('AmazonBooks.csv')

'''Function to retrieve genre from csv file'''

def get_books_by_genre(books,genre):
    genre_book =[]
    for book in books:
      if book['Genre'].lower() == genre.lower():
          genre_book.append(book['Name'])
    return genre_book

'''Function to retrieve author from csv file'''

def get_books_by_author(books,author):
    author_book = []
    for book in books:
        if book['Author'].lower().strip() in author.lower().strip():
            author_book.append(book['Name'])
    return author_book

'''Function to retrieve rating from csv file'''

def get_high_rated_books(books,min_rating):
    rated_books = []
    for book in books:
        if float(book['User Rating']) >= float(min_rating):
            rated_books.append (book['Name'])
    return rated_books

'''Function to retrieve title from csv file &
return None if not book found'''

def get_book_info(books,title):
    for book in books:
        if book['Name'].lower().strip() == title.lower().strip():
            return book
    return None

'''Function for recommendation'''

def recommend_books(books,favorite_book_title):
    '''Function to recommend books based on a favourite book'''
    favorite_book = get_book_info(books,favorite_book_title)
    if not favorite_book:
        return []

    recommendations = []
    for book in books:
        if book['Name'].lower() == favorite_book_title.lower():
            continue
       # else:
           # recommendations.append(book['Name'])
        score = 0
        explanation = []
        #Calculate similarity score

        if book['Genre'] == favorite_book['Genre']:
            score+=3
            explanation.append('Genre Match: Yes')
        else:
            explanation.append('Genre Match: No')
        if book['Author'] == favorite_book['Author']:
            score+=2
            explanation.append('Author Match: Yes')
        else:
            explanation.append('Author Match: No')
        if abs(float(book['User Rating'])) - float(favorite_book['User Rating']) <= 0.5:
            score+=1
            explanation.append('Rating Proximity: Yes')
        else:
            explanation.append('Rating Proximity: No')
        if abs(float(book['Reviews'])) - float(favorite_book['Reviews']) < 1000:
            score+=1
            explanation.append('Review Proximity: Yes')
        else:
            explanation.append('Review Proximity: No')
        if abs(float(book['Price'])) - float(favorite_book['Price']) <= 5:
            score += 1
            explanation.append('Price Proximity: Yes')
        else:
            explanation.append('Price Proximity: No')
        if abs(float(book['Year'])) - float(favorite_book['Year']) < 2:
            score+=1
            explanation.append('Year Proximity: Yes')
        else:
            explanation.append('Year Proximity: No')
        recommendations.append((book,score,explanation))
#score for recommendation
    recommendations.sort(key=lambda x: x[1], reverse=True)
    #this is one-line function taking each item from recommendation &picks second item(x[1])

    top_recommendation = recommendations[:2]

    # picking the first top books in the list

    result = []

    for book,score,explanation in top_recommendation:
        result.append({'Title':book['Name'],
                            'Author':book['Author'],
                            'Genre':book['Genre'],
                            'Rating':book['User Rating'],
                            'Price':book['Price'],
                            'Reviews':book['Reviews'],
                            'Year':book['Year'],
                            'Score':score,
                            'Explanation':explanation})
    return result

def menu():
    print('\nBook Recommendation System for a Library ')
    books = reading_the_book('AmazonBooks.csv')
    if not books:
        print('No books available')
        return
    '''this shows the menu'''
    while True:
        print('\nMenu:')
        print('1. Search by Genre')
        print('2. Search by Author')
        print('3. Search by Rating')
        print('4 Search by book Name')
        print('5. Search Favourite Book Title')
        print('6. Exit Program')

        num = input('\nEnter the number you want to search by: ').strip()
# option 1=5 amd the function each number represent
        if num == '1':
            genre = input('Enter the Genre: ').strip()
            result = get_books_by_genre(books,genre)
            print('Book in Genre:', result)
        elif num == '2':
            author = input("Enter the Author's name: ").strip()
            result = get_books_by_author(books,author)
            print("Books in Author: ", result)
        elif num == '3':
            min_rating = float(input("Enter the Minimun Rating: "))
            result = get_high_rated_books(books,min_rating)
            print('High Rated Books:', result)
        elif num == '4':
            title = input("Enter the Book's Name: ").strip()
            result = get_book_info(books,title)
            print('Book Info:', result)
        elif num =='5':
            favorite_title = input('Enter the title of your favourite book: ')
            recommendations = recommend_books(books,favorite_title)
            if recommendations:
                print(f"If you liked'{favorite_title}', you may also like: ")
                for rec in recommendations:
                    print(f"-Title:{rec['Title']}, \n Score:{rec['Score']}")
                    print("Explanation:")
                    for explanation in rec['Explanation']:
                        print(f'    {explanation}')# 4 space for better readability
            else:
                 print('Book not found, please try again or input a different book')
        elif num == '6':
            print('Thank you for using Book Recommendation System')
            break
        else:
            print('Invalid input enter a nuber between 1-5')
        ask_again = input('Would you like to try another search (yes/no): ').strip()
        if ask_again.lower() != 'yes':
            print('Thank you for using Book Recommendation System')
            break
menu()

# put in text file
import sys
from contextlib import redirect_stdout
'''Run the program and capture output in a file'''
def save_in_textfile(file_name):
    with open(file_name, 'w') as f:
        with redirect_stdout(f): #redirects all print statement to the file
            menu()
'''Saves the output prints in textfile'''
save_in_textfile('Book_recommendations_output.txt')
