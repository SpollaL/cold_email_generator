"""Main module to run streamlit app"""
import sys
import streamlit as st
import streamlit.web.cli as stcli
import traceback
from langchain_community.document_loaders import WebBaseLoader
from cold_email_generator.chains import Chain
from cold_email_generator.portfolio import PortFolio
from cold_email_generator.utils import clean_text


def create_streamlit_app(llm: "Chain", portfolio: "PortFolio") -> None:
    """Function to create streamlit app

    Args:
        llm (Chain): LLM CHain
        portfolio (PortFolio): Portfolio DB
    """
    st.title("Cold Mail Generator")
    url_input = st.text_input("Enter a URL:")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get("skills", [])
                links = portfolio.query_links(skills)
                email = llm.write_email(job, links)
                st.code(email, language="markdown")
        except Exception as e:
            # Get the detailed traceback
            tb_str = traceback.format_exc()
            
            # Display error message with traceback
            st.error(f"An error occurred: {e}")
            st.text_area("Traceback Details", tb_str, height=300)


def app():
    chain = Chain()
    portfolio_ = PortFolio()
    st.set_page_config(
        layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio_)


if __name__ == '__main__':
    app()
