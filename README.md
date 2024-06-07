# giallo-zafferano-scraper-site
 The GialloZafferano Recipe Scraper is a Python-based project designed to scrape and collect recipe data from the GialloZafferano website. This project utilizes web scraping techniques and parallel processing to efficiently gather and store recipe information, including recipe names, ingredients, and other details.

# GialloZafferano Recipe Scraper

## Description

The GialloZafferano Recipe Scraper is a Python-based project designed to scrape and collect recipe data from the GialloZafferano website. This project utilizes web scraping techniques and parallel processing to efficiently gather and store recipe information, including recipe names, ingredients, and other details.

## Features

- **Efficient Web Scraping**: Utilizes `requests` and `BeautifulSoup` to scrape recipe data from multiple pages.
- **Parallel Processing**: Leverages `concurrent.futures.ThreadPoolExecutor` for concurrent scraping, significantly speeding up the data collection process.
- **Progress Tracking**: Uses `tqdm` to display progress bars for page downloading and recipe scraping.
- **Data Storage**: Collected data is stored in a Pandas DataFrame and can be exported to a CSV file.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`
- `tqdm`
- `concurrent.futures` (part of Python standard library)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/giallozafferano-recipe-scraper.git
    cd giallozafferano-recipe-scraper
    ```

2. **Create a virtual environment (optional but recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the scraper script:**
    ```sh
    python scraper.py
    ```

2. **Check the output:**
    - The scraped recipe data will be saved to `ricetta.csv` in the repository root directory.

## Project Structure


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- The project relies on the GialloZafferano website for recipe data.
- Thanks to the developers of `requests`, `BeautifulSoup`, `pandas`, and `tqdm` for their invaluable libraries.
