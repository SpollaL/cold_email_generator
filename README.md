# Cold Email Generation Tool
=====================================

## Overview
------------

This repository contains a set of tools and scripts for generating cold emails based on a given URL. The tool uses a language model (LLM) to extract job information from the webpage content and a portfolio database to query relevant links. The extracted job information and links are then used to generate a cold email.

## Components
-------------

### 1. LLM Chain Module

This module defines a `Chain` class that utilizes the LangChain library to create two chains for natural language processing tasks:

* **Job Extraction Chain**: Extracts job postings from a given text and returns the extracted information in JSON format.
* **Email Writing Chain**: Generates an email based on a job description and a list of corporate links.

### 2. Streamlit App for Cold Email Generation

This script creates a Streamlit app that generates cold emails based on a given URL. The app uses a language model (LLM) to extract job information from the webpage content and a portfolio database to query relevant links.

### 3. Portfolio Database Handler Module

This module provides a class `PortFolio` to manage a portfolio database. It uses `pandas` to read a CSV file and `chromadb` to store and query the data.

### 4. Text Cleaning Function

This function removes unwanted elements from a given text, including HTML tags, URLs, special characters, and multiple spaces.

## Usage
-----

### 1. Initialize the Portfolio Database

Create an instance of the `PortFolio` class and load the portfolio data into the ChromaDB collection:
```python
portfolio = PortFolio(filepath="path/to/portfolio.csv")
portfolio.load_portfolio()
```

### 2. Query Relevant Links

Query the ChromaDB collection to retrieve links based on provided skills:
```python
links = portfolio.query_links(["Python", "Machine Learning"])
print(links)
```

### 3. Generate a Cold Email

Use the Streamlit app to generate a cold email based on a given URL:
```bash
streamlit run app.py
```

## Example Use Case
-----------------

The task is to write a cold email as Mohan, a business development executive at AtliQ, an AI and software consulting company. The email should describe AtliQ's capabilities in fulfilling the client's needs, and include relevant examples from a provided list of links to showcase the company's portfolio.

## Requirements
------------

* Python 3.8+
* LangChain library
* Streamlit library
* pandas library
* chromadb library

## Contributing
------------

Contributions are welcome! Please submit a pull request with your changes and a brief description of what you've added or fixed.
