from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pony import orm
import csv

# Initialize the SQLite database using Pony ORM
db = orm.Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

# Define the database model for storing prices
class Price(db.Entity):
    name = orm.Required(str)   # Store name (e.g., Amazon, Decathlon)
    price = orm.Required(float)  # Product price
    date_created = orm.Required(datetime)  # Date and time of the price entry

db.generate_mapping(create_tables=True)

# Function to scrape Decathlon product page
def decathlon(session, headers):
    url = "https://www.decathlon.de/p/wanderjacke-winterwandern-sh100-x-warm-wasserdicht-10-c-herren/_/R-p-331992?mc=8641924&c=GRAU"
    try:
        resp = session.get(url, headers=headers)
        resp.raise_for_status()  # Ensure we handle any request failures
        soup = BeautifulSoup(resp.text, "html.parser")
        price = float(soup.select_one("div.sprc__active-price.prc__active-price--sale.font").text.strip().replace("€", ""))
        return "Decathlon", price
    except (AttributeError, requests.RequestException) as e:
        print(f"Error fetching data from Decathlon: {e}")
        return "Decathlon", None

# Function to scrape Amazon product page
def amazon(session, headers):
    url = "https://www.amazon.co.uk/Shure-SM7B-Microphone/dp/B0002E4Z8M"
    try:
        resp = session.get(url, headers=headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        price = float(soup.select_one("span.a-offscreen").text.strip().replace("£", ""))
        return "Amazon", price
    except (AttributeError, requests.RequestException) as e:
        print(f"Error fetching data from Amazon: {e}")
        return "Amazon", None

# Function to scrape Thomann product page
def thomann(session, headers):
    url = "https://www.thomann.de/gb/shure_sm_7b_studiomikro.htm"
    try:
        resp = session.get(url, headers=headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        price = float(soup.select_one("div.price-wrapper div.price").text.strip().replace("£", ""))
        return "Thomann", price
    except (AttributeError, requests.RequestException) as e:
        print(f"Error fetching data from Thomann: {e}")
        return "Thomann", None

# Function to export price data to a CSV file
def export_data_to_csv():
    with orm.db_session:
        data = Price.select_by_sql("SELECT * FROM Price")
        with open('price_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Store", "Price", "Date"])
            for d in data:
                writer.writerow([d.name, d.price, d.date_created])

# Function to compare prices between stores
def compare_prices(data):
    valid_data = [item for item in data if item[1] is not None]
    if valid_data:
        cheapest = min(valid_data, key=lambda x: x[1])
        print(f"The cheapest option is {cheapest[0]} at {cheapest[1]:.2f}")
    else:
        print("No valid price data to compare.")

# Main function to control the workflow
def main():
    # User agent header to mimic browser requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    # Create a session to manage requests
    s = requests.Session()

    # Collect data from all sources
    data = [
        decathlon(s, headers),
        amazon(s, headers),
        thomann(s, headers)
    ]

    print("Collected data:", data)

    # Store the data into the database
    with orm.db_session:
        for item in data:
            if item[1] is not None:  # Ensure we only save valid prices
                Price(name=item[0], price=item[1], date_created=datetime.now())
    
    # Export data to CSV file
    export_data_to_csv()

    # Compare prices and print the cheapest option
    compare_prices(data)

if __name__ == '__main__':
    main()
