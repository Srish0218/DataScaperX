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

def get_data(URL):
    page = requests.get(URL, headers=headers)
    if page.status_code != 200:
        st.error("Failed to fetch the page. Please check the URL.")
        return None, None

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find('span', class_='VU-ZEz')
    title = title_element.get_text().strip() if title_element else "Title not found"
    price_element = soup.find('div', class_='Nx9bqj CxhGGd')
    price = price_element.get_text().strip() if price_element else "Price not found"
    st.metric(label="Title", value=title)
    st.metric(label="Price", value=price)
    return title, price

def send_email(title, price, URL):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('srishtijaitly2002@gmail.com', 'esylrglmynyfwyqc')

    subject = f"The Product {title} you want is now {price}! Now is your chance to buy!"
    body = (f"The Product {title} you want is now {price}! Now is your chance to buy! "
            f"Dear User, This is the moment we have been waiting for. Now is your chance to pick up the product of your dreams. Don't miss it! Link here: {URL}")

    msg = MIMEMultipart()
    msg['From'] = 'srishtijaitly2002@gmail.com'
    msg['To'] = 'sjaitly0218@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))

    server.sendmail('srishtijaitly2002@gmail.com', 'sjaitly0218@gmail.com', msg.as_string())
    server.quit()

def scrape_and_track():
    URL = st.text_input("URL","")
    price_threshold = 1000
    if URL:
        title, price = get_data(URL)
        if title is not None and price is not None:
            today = datetime.date.today()
            with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow([title, price, today])

            if float(price.replace('₹', '').replace(',', '')) < price_threshold:
                send_email(title, price, URL)
                st.toast("Email Sent!", icon='🎉')

            # Display recent values from the CSV
            df = pd.read_csv('FlipkartWebScraperDataset.csv')
            df_recent = df.tail(5).rename(columns={0: "Title", 1: "Price", 2: "Date"})
            st.write("Recent values: ")
            st.write(df_recent)
    else:
        st.warning("Enter Flipkart Link")

def gfg():
    URL = st.text_input("URL", "")
    if URL:
        page = requests.get(URL, headers=headers)
        if page.status_code != 200:
            st.error("Failed to fetch the page. Please check the URL.")
            return

        soup = BeautifulSoup(page.content, "html.parser")
        title_element = soup.find('h1', class_='entry-title')
        if not title_element:
            title_element = soup.find('div', class_='article-title')
        title = title_element.get_text().strip() if title_element else "Title not found"

        # Find content
        content_element = soup.find('div', class_='page_content')
        if not content_element:
            content_element = soup.find('article', class_='content')
        content = content_element.get_text() if content_element else "No Content"
        # Exclude specific words from the content
        content_excluded_words = ['Share your thoughts in the comments', 'Please Login to comment', 'Add Your Comment',
                                  'Improve', 'Like Article', 'Like', 'Save', 'Share',
                                  'Report', 'Suggest improvement', 'Previous',
                                  'Next' ]  # Add words you want to exclude
        content = re.sub(r'\b(?:{})\b'.format('|'.join(content_excluded_words)), '', content, flags=re.IGNORECASE)

        st.metric(label="Title", value=title)
        st.write(content)
    else:
        st.warning("Enter Link")

def coursera():
    URL = st.text_input("URL", "")
    if not URL:
        st.warning("Enter Link")
    else:
        page = requests.get(URL, headers=headers)
        if page.status_code != 200:
            st.error("Failed to fetch the page. Please check the URL.")
            return

        soup = BeautifulSoup(page.content, "html.parser")
        title_element = soup.find('h1', class_='cds-119 cds-Typography-base css-1xy8ceb cds-121')
        title = title_element.get_text().strip() if title_element else "Title not found"

        image_element = soup.find('img', class_='css-1f9gt0j')  # Update with the actual class of the image
        image_url = image_element['src'] if image_element else None

        description_element = soup.find('p', class_="css-4s48ix")
        description = description_element.get_text().strip() if description_element else "No Description"
        description_excluded_words = ['Learn more']
        description = re.sub(r'\b(?:{})\b'.format('|'.join(description_excluded_words)), '', description, flags=re.IGNORECASE)

        # Find type
        type_element = soup.find('h2', class_='cds-119 cds-Typography-base css-h1jogs cds-121')
        type = type_element.get_text() if type_element else "No Content"

        rating_element = soup.find('div', class_='cds-119 cds-Typography-base css-h1jogs cds-121')
        rating = rating_element.get_text().strip()

        skills_element = soup.find('ul', class_='css-yk0mzy')  # Update with the actual class of the list
        if skills_element:
            items = [item.get_text() for item in skills_element.find_all('li')]
        else:
            items = []

        st.metric(label="Title", value=title)
        st.image(image_url)
        st.subheader("Description")
        st.write(description)
        st.subheader(type)
        st.metric(label='Rating', value=rating + '⭐')
        st.subheader('Skills You Will Gain')
        st.write(items)


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

website = st.selectbox("Select Website:", ["", "Flipkart", "GeeksForGeeks", "Coursera", "Nykaa"])

if website:
    if website == "Flipkart":
        scrape_and_track()
    elif website == "GeeksForGeeks":
        gfg()
    elif website == "Coursera":
        coursera()
