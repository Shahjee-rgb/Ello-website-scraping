# -*- coding: utf-8 -*-
"""Scripting

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1newsWCQevEsF6YZMKErjsqf6zr-pLDPA
"""

import requests
from bs4 import BeautifulSoup

for i in range(85):
    page = i + 1
    url = f'https://www.elo.shopping/collections/mens-tops-collection?page={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    collection_title = soup.select_one('[class="collection-hero__text-wrapper"]').text.strip()
    print(collection_title)

    for card in soup.select('[class="card-wrapper product-card-wrapper underline-links-hover"]'):
        title = card.select_one('[class="card__heading h3"]').text.strip()
        price = card.select_one('[class="price__regular"]').text.strip()

        print(title)
        print(price)

        url = card.select_one('a').get('href')

        url = 'https://www.elo.shopping'+url

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_description = soup.select_one('[class="product__title"]').text.strip() if soup.select_one('[class="product__title"]') else "N/A"
        price = soup.select_one('[class="price-item price-item--regular"]').text.strip() if soup.select_one('[class="price-item price-item--regular"]') else "N/A"
        size = soup.select_one('[class="form__label elo-swatch-option-size"]').text.strip() if soup.select_one('[class="form__label elo-swatch-option-size"]') else "N/A"
        colour = soup.select_one('[class="form__label elo-swatch-option-color"]').text.strip() if soup.select_one('[class="form__label elo-swatch-option-color"]') else "N/A"
        quantity = soup.select_one('[class="quantity__label form__label"]').text.strip() if soup.select_one('[class="quantity__label form__label"]') else "N/A"

        print(title_description)
        print(price)
        print(size)
        print(colour)
        print(quantity)

# Install the TextBlob library if you don't have it
# Run this command in your terminal or notebook:
# !pip install textblob

from textblob import TextBlob

# Input sentence
sentence = "I love programming, it makes me happy!"

# Create a TextBlob object
blob = TextBlob(sentence)

# Perform sentiment analysis
sentiment = blob.sentiment

# Print the results
print(f"Sentence: {sentence}")
print(f"Sentiment Polarity: {sentiment.polarity}")  # Polarity ranges from -1 (negative) to 1 (positive)
print(f"Sentiment Subjectivity: {sentiment.subjectivity}")  # Subjectivity ranges from 0 (objective) to 1 (subjective)

import csv
import requests
from bs4 import BeautifulSoup

# Create and open a CSV file for writing
with open('mens_tops_collection.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row to the CSV file
    csvwriter.writerow(['Collection Title', 'Product Title', 'Price', 'Product URL', 'Description Title', 'Detailed Price', 'Size', 'Colour', 'Quantity'])

    # Iterate through all pages
    for i in range(1):  # Assuming there are 85 pages
        page = i + 1
        url = f'https://www.elo.shopping/collections/mens-tops-collection?page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the collection title
        collection_title = soup.select_one('[class="collection-hero__text-wrapper"]').text.strip()

        # Extract product details
        for card in soup.select('[class="card-wrapper product-card-wrapper underline-links-hover"]'):
            title = card.select_one('[class="card__heading h3"]').text.strip()
            price = card.select_one('[class="price__regular"]').text.strip()
            product_url = card.select_one('a').get('href')
            product_url = 'https://www.elo.shopping' + product_url

            # Fetch product details from the product page
            response = requests.get(product_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            title_description = soup.select_one('[class="product__title"]').text.strip() if soup.select_one('[class="product__title"]') else "N/A"
            detailed_price = soup.select_one('[class="price-item price-item--regular"]').text.strip() if soup.select_one('[class="price-item price-item--regular"]') else "N/A"
            size = soup.select_one('[class="form__label elo-swatch-option-size"]').text.strip() if soup.select_one('[class="form__label elo-swatch-option-size"]') else "N/A"
            colour = soup.select_one('[class="form__label elo-swatch-option-color"]').text.strip() if soup.select_one('[class="form__label elo-swatch-option-color"]') else "N/A"
            quantity = soup.select_one('[class="quantity__label form__label"]').text.strip() if soup.select_one('[class="quantity__label form__label"]') else "N/A"

            # Write the data to the CSV file
            csvwriter.writerow([collection_title, title, price, product_url, title_description, detailed_price, size, colour, quantity])

print("CSV file 'mens_tops_collection.csv' has been created successfully!")





