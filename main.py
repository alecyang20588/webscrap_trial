import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage
webpage_url = "https://raw.githubusercontent.com/alecyang20588/webscrap_trial/main/Test_Scanware.html"

# Fetch the content of the webpage
response = requests.get(webpage_url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div containing text like "End of production..."
pattern_production = re.compile(r'End of production.*', re.IGNORECASE)
end_of_production_div = soup.find("div", class_="small", text=pattern_production)

if end_of_production_div:
    timestamp_td = end_of_production_div.find_next("td", class_="tdalt2")
    timestamp = timestamp_td.div.text.strip() if timestamp_td and timestamp_td.div else "Timestamp not found"
else:
    timestamp = "End of production text not found"

# Find the div containing text like "Number of evaluation cycles..."
pattern_cycles = re.compile(r'Number of evaluation cycles.*', re.IGNORECASE)
evaluation_cycles_div = soup.find("div", class_="small", text=pattern_cycles)

if evaluation_cycles_div:
    cycles_td = evaluation_cycles_div.find_next("td", class_="td2")
    cycles_value = cycles_td.div.text.strip() if cycles_td and cycles_td.div else "Evaluation cycles not found"
else:
    cycles_value = "Number of evaluation cycles text not found"

# Write the extracted data to a log file
with open("log.txt", "w") as file:  # We use 'w' mode to overwrite the file
    file.write(f"End of Production Timestamp: {timestamp}\n")
    file.write(f"Number of Evaluation Cycles: {cycles_value}\n")

print("Data written to log.txt")
