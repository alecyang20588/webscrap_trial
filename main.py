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

# Use regex to find the div containing text like "Number of evaluation cycles..."
pattern = re.compile(r'Number of evaluation cycles.*', re.IGNORECASE)
evaluation_cycles_div = soup.find("div", class_="small", text=pattern)

# Find the next td containing the number of evaluation cycles
if evaluation_cycles_div:
    cycles_td = evaluation_cycles_div.find_next("td", class_="td2")
    cycles_value = cycles_td.div.text.strip() if cycles_td and cycles_td.div else "Not found"
else:
    cycles_value = "Partial match not found"

# Write the extracted number to a log file
with open("log.txt", "a") as file:  # We use 'a' mode to append to the file
    file.write(f"Number of Evaluation Cycles: {cycles_value}\n")

print("Data appended to log.txt")
