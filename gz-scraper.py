import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

# Inizializza DataFrame
giallo_zafferano = pd.DataFrame(columns=["Nome", "Ingredienti", "Informazioni"])


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


def scraping_dolce(url):

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            informazioni = {}
            ingredienti = []

            # Estrai informazioni
            div_element = soup.find("div", class_="gz-list-featured-data")
            if div_element:
                ul_element = div_element.find("ul")
                if ul_element:
                    for li in ul_element.find_all("li"):
                        span_element = li.find("span", class_="gz-name-featured-data")
                        strong_element = li.find("strong")
                        if span_element and strong_element:
                            informazioni[span_element.text.strip()] = strong_element.text.strip()

            # Estrai ingredienti
            div_element2 = soup.find("div", class_="gz-ingredients gz-mBottom4x gz-outer")
            if div_element2:
                dl_element = div_element2.find("dl", class_="gz-list-ingredients")
                if dl_element:
                    for dd_element in dl_element.find_all("dd", class_="gz-ingredient"):
                        a_element = dd_element.find("a")
                        span_element = dd_element.find("span")
                        if a_element and span_element:
                            ingrediente = a_element.text.strip().replace("\n", "").replace("\t", "").replace("\r", "")
                            quantità = span_element.text.strip().replace("\n", "").replace("\t", "").replace("\r", "")
                            ingredienti.append(f"{ingrediente} ({quantità})")

            # Estrai nome della ricetta
            div_element3 = soup.find("div", class_="gz-title-content gz-innerdesktop")
            if div_element3:
                h_element = div_element3.find("h1", class_="gz-title-recipe gz-mBottom2x").text.strip()

            # Aggiungi alla DataFrame
            giallo_zafferano.loc[len(giallo_zafferano)] = [h_element, ", ".join(ingredienti), ", ".join([f"{k}: {v}" for k, v in informazioni.items()])]
    except requests.exceptions.SSLError as e:
        print(f"Errore SSL: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
# Funzione per ottenere i link delle ricette da una pagina principale


def scraping_pagina(url_main):
    urls = []
    response = requests.get(url_main)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        divs_element = soup.find_all("div", class_="gz-card-content")
        if divs_element:
            for div in divs_element:
                title = div.find("h2", class_="gz-title")
                if title:
                    a_element = title.find("a")
                    link = a_element.get("href")
                    if link:
                        urls.append(link)
    return urls

# Funzione per raccogliere tutti i link delle pagine di ricette
def scraping_serie():
    pagine = []
    for i in tqdm(range(1, 469), desc="Scaricando pagine"):  # Supponiamo che ci siano fino a 468 pagine
        url = f"https://www.giallozafferano.it/ricette-cat/pag-{i}/"
        pagine.extend(scraping_pagina(url))
    return pagine

# Raccogli i link delle pagine di ricette
pagine = scraping_serie()

# Scraping delle ricette
for pagina in tqdm(pagine, desc="Scaricando ricette"):
    scraping_dolce(pagina)

# Stampa e salvataggio del DataFrame
print(giallo_zafferano)
giallo_zafferano.to_csv('ricetta.csv', index=False, encoding='utf-8', sep=',')



















