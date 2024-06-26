# DataScraperX 🕸️

DataScaperX is a versatile web scraping tool built with Python and Streamlit. It allows users to extract information from various websites such as Flipkart, GeeksForGeeks, and Coursera. Whether you want to track product prices, read articles, or explore course details, DataScaperX has got you covered!
## Features

- **Flipkart Scraper**: Monitor product prices on Flipkart by providing the product URL.
- **GeeksForGeeks Scraper**: Fetch content from GeeksForGeeks by providing the article URL.
- **Coursera Scrapper**:Explore course details on Coursera by providing the course URL.
- **Email Notifications**: Receive email notifications when there is a significant change in data.
- **Streamlit Interface**: User-friendly interface powered by Streamlit for easy interaction.

## How to Use

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/Srish0218/DataScaperX.git
   ```

2. Navigate to the project directory.
   ```bash
   cd DataScraperX
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```
5. Don't Forget to change header According to your own system from https://httpbin.org/get
6. Select the website you want to scrape (Flipkart or GeeksForGeeks) and provide the URL.
Scrape Data: Select the desired website from the dropdown, input the URL, and click 'Scrape' to extract data.

<details>
<summary> Instructions</summary>
For Flipkart, enter the URL of the product page only!

For GeeksForGeeks, enter the URL of the article page only, not the home page.

For Coursera, enter the URL of the course or professional certificate info page!

</details>

7. Monitor the data and receive email notifications if enabled.

## Requirements

- Python 3.7+
- Streamlit
- BeautifulSoup
- Requests
- Pandas

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)
- [Flipkart](https://www.flipkart.com/)
- [Coursera](https://www.coursera.org/)

