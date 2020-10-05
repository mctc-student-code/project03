import sqlite3 # Import SQLite3
import os

database = "art.sqlite3" # For ease, make "database" a Global Variable always associated with "art.sqlite"

def create_artists_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists (artist_name TEXT, artist_email TEXT)")
    conn.close()

def create_artworks_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artworks (artwork_name TEXT, artist_name TEXT, price REAL, available BOOLEAN")
    conn.close()

def add_new_artist():
    new_artist_name = input("What is the name of the artist you would like to add? ") # Prompt useer for new artist's name
    new_artist_email = input("Please enter the e-mail address of the artist you would like to add: ") # Prompt user for new artist's e-mail address
    
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artists VALUES (? , ?)", (new_artist_name , new_artist_email))
    conn.close()

def add_new_artwork():
    new_artwork = input("What is the name of the artwork you would like to add? ") # Prompt user for new artworks's name
    new_artist = input("What is the name of the artist attributed to that artwork? ") # Prompt user for new artwork's artist
    new_price = float(input("How much does the artwork cost? $")) # Prompt user for new artwork's price.
    new_avaiability = input("Is the artwork currently available for purchase? ") # Prompt user for new artwork's availability
    with sqlite3.connect(database) as conn:
        conn.execute(f"INSERT INTO artworks VALUES (? , ?, ?, ?)", (new_artwork, new_artist, new_price, new_avaiability))
    conn.close()

def search_by_artist():
    search_artist = input("What is the name of the artist whose artworks you want to see? ")
    with sqlite3.connect(database) as conn:
        results = conn.execute("SELECT artwork_name FROM artworks WHERE artist_name like ?", (search_artist, ))
        return(results)
    conn.close()

def delete_artwork():
    delete_artwork = input("What is the name of the artwork you would like to remove? ")
    with sqlite3.connect(database) as conn:
        conn.execute(f"DELETE FROM artworks WHERE artwork_name = ?", (delete_artwork, ))
    conn.close()

# def change_availability():
    # available_update = input("What is the name of the artwork whose availability you would like to update? ")
        # with sqlite3.connect(database) as conn:
        # results = conn.execute("SELECT available FROM artworks WHERE artwork_name = ?", (available_update, ))
        # if results = True:
        #
        #return(results)
    #conn.close()

def available_artwork():
    search_artist = input("What is the name of the artist whose available artworks you want to see? ")
    with sqlite3.connect(database) as conn:
        results = conn.execute("SELECT artwork_name FROM artworks WHERE artist_name = ? AND available IS TRUE", (search_artist, ))
        return(results)
    conn.close()

# Code functions as-is when called

create_artists_table()
create_artworks_table()
add_new_artist()
add_new_artwork()
search_by_artist()
delete_artwork()
available_artwork()
