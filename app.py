import re
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
import datetime
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Function to get data from URL
def get_data(URL):
    try:
        page = requests.get(URL, headers=headers)
        page.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Failed to fetch the page. Error: {e}")
        return None, None

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find('span', class_='VU-ZEz')
    title = title_element.get_text().strip() if title_element else "Title not found"
    price_element = soup.find('div', class_='Nx9bqj CxhGGd')
    price = price_element.get_text().strip() if price_element else "Price not found"
    st.metric(label="Title", value=title)
    st.metric(label="Price", value=price)
    return title, price

# Function to send email
def send_email(title, price, URL):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('srishtijaitly2002@gmail.com',  'esylrglmynyfwyqc')
    except smtplib.SMTPException as e:
        st.error(f"Failed to connect to email server. Error: {e}")
        return

    subject = f"The Product {title} you want is now {price}! Now is your chance to buy!"
    body = (f"The Product {title} you want is now {price}! Now is your chance to buy! "
            f"Dear User, This is the moment we have been waiting for. Now is your chance to pick up the product of your dreams. Don't miss it! Link here: {URL}")

    msg = MIMEMultipart()
    msg['From'] = 'srishtijaitly2002@gmail.com'
    msg['To'] =  'sjaitly0218@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))

    try:
        server.sendmail('srishtijaitly2002@gmail.com',  'sjaitly0218@gmail.com', msg.as_string())
        st.toast("Email sent successfully!" , icon='🎉')
    except smtplib.SMTPException as e:
        st.error(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

# Function to scrape and track data from Flipkart
def scrape_and_track():
    URL = st.text_input("URL", "")
    price_threshold =1000
    if URL:
        title, price = get_data(URL)
        if title is not None and price is not None:
            today = datetime.date.today()
            try:
                with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow([title, price, today])
            except IOError as e:
                st.error(f"Failed to write to CSV file. Error: {e}")
                return

            try:
                price_value = float(price.replace('₹', '').replace(',', ''))
                if price_value < price_threshold:
                    send_email(title, price, URL)
            except ValueError as e:
                st.error(f"Failed to parse price. Error: {e}")

            try:
                df = pd.read_csv('FlipkartWebScraperDataset.csv', header=None)
                df_recent = df.tail(5).rename(columns={0: "Title", 1: "Price", 2: "Date"})
                st.write("Recent values: ")
                st.write(df_recent)
            except (IOError, pd.errors.ParserError) as e:
                st.error(f"Failed to read CSV file. Error: {e}")
    else:
        st.warning("Enter Flipkart Link")

# Function to scrape data from GeeksForGeeks
def gfg():
    URL = st.text_input("URL", "")
    if URL:
        try:
            page = requests.get(URL, headers=headers)
            page.raise_for_status()
        except requests.RequestException as e:
            st.error(f"Failed to fetch the page. Error: {e}")
            return

        soup = BeautifulSoup(page.content, "html.parser")
        title_element = soup.find('h1', class_='entry-title') or soup.find('div', class_='article-title')
        title = title_element.get_text().strip() if title_element else "Title not found"

        content_element = soup.find('div', class_='page_content') or soup.find('article', class_='content')
        content = content_element.get_text() if content_element else "No Content"

        excluded_words = [
            'Share your thoughts in the comments', 'Please Login to comment', 'Add Your Comment',
            'Improve', 'Like Article', 'Like', 'Save', 'Share',
            'Report', 'Suggest improvement', 'Previous', 'Next'
        ]
        content = re.sub(r'\b(?:{})\b'.format('|'.join(excluded_words)), '', content, flags=re.IGNORECASE)

        st.metric(label="Title", value=title)
        st.write(content)
    else:
        st.warning("Enter Link")

# Function to scrape data from Coursera
def coursera():
    URL = st.text_input("URL", "")
    if not URL:
        st.warning("Enter Link")
    else:
        try:
            page = requests.get(URL, headers=headers)
            page.raise_for_status()
        except requests.RequestException as e:
            st.error(f"Failed to fetch the page. Error: {e}")
            return

        soup = BeautifulSoup(page.content, "html.parser")
        title_element = soup.find('h1', class_='cds-119 cds-Typography-base css-1xy8ceb cds-121')
        title = title_element.get_text().strip() if title_element else "Title not found"

        image_element = soup.find('img', class_='css-1f9gt0j')
        image_url = image_element['src'] if image_element else None

        description_element = soup.find('p', class_="css-4s48ix")
        description = description_element.get_text().strip() if description_element else "No Description"
        description_excluded_words = ['Learn more']
        description = re.sub(r'\b(?:{})\b'.format('|'.join(description_excluded_words)), '', description, flags=re.IGNORECASE)

        type_element = soup.find('h2', class_='cds-119 cds-Typography-base css-h1jogs cds-121')
        type = type_element.get_text() if type_element else "No Content"

        rating_element = soup.find('div', class_='cds-119 cds-Typography-base css-h1jogs cds-121')
        rating = rating_element.get_text().strip() if rating_element else "No Rating"

        skills_element = soup.find('ul', class_='css-yk0mzy')
        skills = [item.get_text() for item in skills_element.find_all('li')] if skills_element else []

        st.metric(label="Title", value=title)
        if image_url:
            st.image(image_url)
        st.subheader("Description")
        st.write(description)
        st.subheader(type)
        st.metric(label='Rating', value=rating + '⭐')
        st.subheader('Skills You Will Gain')
        st.write(skills)

# Main UI
st.header("DataScaperX 🕸️")
st.markdown("---")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

website = st.selectbox("Select Website:", ["", "Flipkart", "GeeksForGeeks", "Coursera"])

if website:
    if website == "Flipkart":
        scrape_and_track()
    elif website == "GeeksForGeeks":
        gfg()
    elif website == "Coursera":
        coursera()
