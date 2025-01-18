import requests
from bs4 import BeautifulSoup
from googlesearch import search
import sqlite3

# Function to perform a Google search and return a list of links
def google_search(query, num_results=10):
    return list(search(query, num_results=num_results))

# Function to scrape quotes from a webpage
def scrape_quotes(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all quote elements (this may vary depending on the webpage structure)
        quotes = []
        for quote in soup.find_all("blockquote"):
            text = quote.get_text(strip=True)
            quotes.append(text)
        
        return quotes
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return []

# Function to save quotes to an SQLite database
def save_quotes_to_db(quotes, db_name="starwars_quotes.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL
        )
    """)
    
    # Insert quotes into the table
    for quote in quotes:
        cursor.execute("INSERT INTO quotes (quote) VALUES (?)", (quote,))
    
    conn.commit()
    conn.close()

def main():
    query = "Star Wars quotes"
    links = google_search(query)
    all_quotes = []
    
    for link in links:
        quotes = scrape_quotes(link)
        all_quotes.extend(quotes)
    
    save_quotes_to_db(all_quotes)
    print(f"Saved {len(all_quotes)} quotes to the database.")

if __name__ == "__main__":
    main()