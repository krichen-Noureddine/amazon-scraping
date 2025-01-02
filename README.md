# Amazon Scraping Project

A Python-based web scraping tool to fetch product details from Amazon. The goal of this project is to efficiently extract key product data such as prices, ratings, descriptions, and availability from Amazon product pages.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/krichen-Noureddine/amazon-scraping.git
    ```
2. Navigate to the project directory:
    ```bash
    cd amazonScraping
    ```
3. Set up a virtual environment:
    - For Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the scraper, you first need to add the product URLs that you want to scrape to the `links.txt` file. Each line in the `links.txt` file should contain one Amazon product URL.

For example, your `links.txt` file should look like this:

## Contributing

We welcome contributions from the community! If you'd like to contribute to the **Amazon Scraping Project**, please follow the guidelines in our [CONTRIBUTING.md](CONTRIBUTING.md) file.

Here’s a quick overview:
1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch for your changes.
4. Make and test your changes.
5. Push your branch and create a pull request.

For more details, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md).
