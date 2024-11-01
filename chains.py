"""Module to store the llm chains"""
import os
from typing import List
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from prompts import email_template, extraction_template


class Chain:
    """Class containing the project Chains
    """

    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-70b-versatile"
        )

    def extract_jobs(self, cleaned_text: str) -> List[str]:
        """Chain to extract job info from a job post"""
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except Exception as e:
            raise OutputParserException(
                "Content too big. Unable to parse jobs") from e
        return res if isinstance(res, list) else [res]

    def write_email(self, job: str, links: List[str]) -> str:
        """Chain to write email from job description and relevant corporate links"""
        prompt_email = PromptTemplate.from_template(
            email_template
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke(
            input={"job_description": str(job), "link_list": links})
        return res.content
