"""
Sports News Scraper

This script scrapes sports news headlines from the Indian Express website.
It retrieves titles, subtitles, and links for multiple articles and saves them to a CSV file.

Features:
- Headless browser operation
- Error handling and logging
- Command-line arguments for customization
- Multiple page scraping
- Rate limiting to prevent overloading the server

Usage:
python sports_news_scraper.py [--pages PAGE_COUNT] [--output OUTPUT_FILE]

Dependencies:
- selenium
- pandas
- requests
- argparse
- logging
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
from datetime import datetime
import os
import sys
import argparse
import logging
import time
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver(driver_path):
    """Set up and return a configured Chrome WebDriver."""
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_page(driver, url):
    """Scrape a single page for news articles."""
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    
    titles, subtitles, links = [], [], []
    
    try:
        # Scrape the first (featured) article
        first_article = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="articles first"]')))
        titles.append(first_article.find_element(By.XPATH, './/h2').text)
        subtitles.append(first_article.find_element(By.XPATH, './/p').text)
        links.append(first_article.find_element(By.XPATH, './/h2/a').get_attribute("href"))
        
        # Scrape the rest of the articles
        containers = driver.find_elements(By.XPATH, '//div[@class="articles "]')
        for container in containers:
            titles.append(container.find_element(By.XPATH, './/h2').text)
            subtitles.append(container.find_element(By.XPATH, './/p').text)
            links.append(container.find_element(By.XPATH, './/h2/a').get_attribute("href"))
    
    except (TimeoutException, NoSuchElementException) as e:
        logging.error(f"Error scraping page {url}: {str(e)}")
    
    return titles, subtitles, links

def main(pages, output_file):
    website = 'https://indianexpress.com/section/sports/'
    driver_path = '/Users/jijovaliyaveettil/Downloads/chromedriver_mac_arm64'
    
    driver = setup_driver(driver_path)
    
    all_titles, all_subtitles, all_links = [], [], []
    
    for page in range(1, pages + 1):
        url = f"{website}/page/{page}/" if page > 1 else website
        logging.info(f"Scraping page {page}")
        
        titles, subtitles, links = scrape_page(driver, url)
        all_titles.extend(titles)
        all_subtitles.extend(subtitles)
        all_links.extend(links)
        
        # Rate limiting
        time.sleep(2)
    
    driver.quit()
    
    # Create DataFrame and save to CSV
    df_headlines = pd.DataFrame({
        'titles': all_titles,
        'subtitles': all_subtitles,
        'links': all_links
    })
    
    df_headlines.to_csv(output_file, index=False)
    logging.info(f"Data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape sports news from Indian Express")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--output", type=str, default=f"sports-headline_{datetime.now().strftime('%m%d%Y')}.csv",
                        help="Output file name")
    
    args = parser.parse_args()
    
    main(args.pages, args.output)
