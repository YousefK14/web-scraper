import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically set up the ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the Oxylabs blog
driver.get('https://oxylabs.io/blog')

# Extract page source and parse it with BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Quit the Selenium WebDriver
driver.quit()

# Create empty lists to store results
results = []
other_results = []

# Scrape blog post titles
for a in soup.find_all(attrs={'class': 'blog-card__content-wrapper'}):
    name = a.find('h2')
    if name and name.text.strip():
        results.append(name.text.strip())

# Scrape blog post dates
for b in soup.find_all(attrs={'class': 'blog-card__date-wrapper'}):
    date = b.find('p')
    if date and date.text.strip():
        other_results.append(date.text.strip())

# Create a DataFrame and save the data to a CSV file
df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
