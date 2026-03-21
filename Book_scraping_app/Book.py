import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Book Scraping")

name = st.text_input("Enter Your Name")
if name:
    st.write(f"Hello {name} , Welcome to a Simple Web-Scraping Project")
if st.button("Scrape Data"):
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    titles = []
    prices = []

    for book in books:
        title = book.find("h3").find("a").get("title")
        raw_price = book.find("p", class_="price_color").text
        clean_price = ''.join(c for c in raw_price if c.isdigit() or c == '.')
        price = float(clean_price)
        titles.append(title)
        prices.append(price)

    df = pd.DataFrame({
        "Book": titles,
        "Price": prices
    })

    st.dataframe(df)
    st.subheader("This is the Bar-chart")
    st.bar_chart(df.set_index("Book"))