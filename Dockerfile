FROM python:3.12-slim
WORKDIR /app
COPY ./dist/cold_email_generator-0.1.0-py3-none-any.whl /app/
RUN pip install --no-cache-dir /app/cold_email_generator-0.1.0-py3-none-any.whl
RUN groupadd app && useradd -g app app
USER app
CMD [ "cold-email" ]