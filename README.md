**Cold Email Generator using Large Language Model (LLM) Chain 🚀**
=================================================================


https://github.com/user-attachments/assets/1a18d5cf-f14c-4a29-bb47-301678add095


**Repository Overview**
------------------------

This repository contains a Streamlit app that generates cold emails based on job descriptions using a Large Language Model (LLM) chain. The app extracts job information from job descriptions and generates emails using the extracted information.

**What's Inside**
----------------

* `llm_chains.py`: Manages LLM chains for extracting job information and generating emails.
* `portfolio.py`: Handles a portfolio database using ChromaDB.
* `email_template`: Provides a template for generating cold emails.
* `utils.py`: Offers utility functions for text cleaning and preprocessing.

**How it Works**
----------------

1. The user inputs a job description URL into the Streamlit app.
2. The app uses the LLM chain to extract job information from the job description.
3. The extracted information is used to generate a cold email using the email template.
4. The app queries the portfolio database to retrieve relevant links based on skills.
5. The generated email is displayed to the user.

**Key Functions**
----------------

* `extract_jobs`: Extracts job information from a job post and returns it in JSON format.
* `write_email`: Generates an email from a job description and relevant corporate links.
* `create_streamlit_app`: Creates a Streamlit app that takes a URL as input, extracts job information, and generates an email.
* `load_portfolio`: Loads the portfolio dataset into ChromaDB.
* `query_links`: Queries the ChromaDB dataset to retrieve links based on skills.
* `clean_text`: Cleans and preprocesses text data by removing HTML tags, URLs, special characters, and extra whitespace.

**Dependencies**
----------------

* `langchain_groq`
* `langchain_core.prompts`
* `langchain_core.output_parsers`
* `langchain_core.exceptions`
* `prompts`
* `os`
* `streamlit`
* `langchain_community.document_loaders`
* `pandas`
* `chromadb`


**Notes**
--------

* Environment variables (GROQ_API_KEY) are used to configure the ChatGroq instance.
* The `extract_jobs` method raises an `OutputParserException` if the content is too big to parse.
* The `write_email` method uses an email template from the `prompts` module.
* The portfolio dataset is stored in a CSV file and loaded into ChromaDB using the `load_portfolio` method.
