# DataScraperX 🕸️

DataScraperX is a web scraping tool built with Streamlit, capable of monitoring product prices on Flipkart and content on GeeksForGeeks.

## Features

- **Flipkart Scraper**: Monitor product prices on Flipkart by providing the product URL.
- **GeeksForGeeks Scraper**: Fetch content from GeeksForGeeks by providing the article URL.
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

---

Feel free to customize this template according to your project's specifics and add any additional sections or information you find relevant.