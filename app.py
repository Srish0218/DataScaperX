import streamlit as st
from bs4 import BeautifulSoup
import requests
import time as t
import datetime
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


st.header("DataScaperX 🕸️")
st.markdown("---")

def flipkart():
    if URL:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # Find title
        title_element = soup.find('span', class_='VU-ZEz')
        title = title_element.get_text().strip() if title_element else "Title not found"

        # Find price
        price_element = soup.find('div', class_='Nx9bqj CxhGGd')
        price = price_element.get_text().strip() if price_element else "Price not found"

        st.metric(label="Title", value=title)
        st.metric(label="Price", value=price)

        # Create a Timestamp for your output to track when data was collected
        today = datetime.date.today()
        time = datetime.datetime.now()
        st.write(f"As of {time}")

        header = ['Title', 'Price', 'Date']
        data = [title, price, today]
        # %%
        import pandas as pd

        df = pd.read_csv(r'FlipkartWebScraperDataset.csv')

        st.markdown("---")

        with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        def check_price():
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Connection": "close",
                "Upgrade-Insecure-Requests": "1"
            }

            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")

            # Find title
            title_element = soup.find('span', class_='VU-ZEz')
            title = title_element.get_text().strip() if title_element else "Title not found"

            # Find price
            price_element = soup.find('div', class_='Nx9bqj CxhGGd')
            price = price_element.get_text().strip() if price_element else "Price not found"
            today = datetime.date.today()
            header = ['Title', 'Price', 'Date']
            data = [title, price, today]
            with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(data)

        def send_mail1(title, price, URL):
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login('srishtijaitly2002@gmail.com', 'esylrglmynyfwyqc')

            subject = f"The Product {title} you want is now {price}! Now is your chance to buy!"
            body = (f"The Product {title} you want is now {price}! Now is your chance to buy! "
                    f"Dear User, This is the moment we have been waiting for. Now is your chance to pick up the product of your dreams. Don't miss it! Link here: {URL}")

            # Create MIMEText object with UTF-8 encoding
            msg = MIMEMultipart()
            msg['From'] = 'srishtijaitly2002@gmail.com'
            msg['To'] = 'sjaitly0218@gmail.com'
            msg['Subject'] = subject
            msg.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))

            # Send email
            server.sendmail('srishtijaitly2002@gmail.com', 'sjaitly0218@gmail.com', msg.as_string())
            server.quit()

        i = 0
        while (i <= 5):
            check_price()
            i += 1
            send_mail1(title, price, URL)

            st.toast("Email Send!!", icon='🎉')
            t.sleep(0.1)

        st.write("Recent values: ")
        st.write(df.tail(5))
    else:
        st.warning("Enter Flipkart Link")

def gfg():
    if URL:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        title_element = soup.find('h1', class_='entry-title')
        title = title_element.get_text().strip() if title_element else "Title not found"

        # Find price
        content_element = soup.find('div', class_='page_content')
        content = content_element.get_text() if content_element else "Price not found"

        st.metric(label= "Title" , value=title)
        st.write(content)
    else:
        st.warning("Enter Link")



website = st.selectbox("Select Website:", ["Flipkart" , "GeeksForGeeks"] )
URL = st.text_input("URL")

if website == "Flipkart":
    flipkart()
elif website == "GeeksForGeeks":
    gfg()
