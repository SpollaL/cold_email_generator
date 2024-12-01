FROM python:3.12-slim
WORKDIR /app
COPY ./dist/cold_email_generator-0.1.0-py3-none-any.whl /app/
RUN pip install --no-cache-dir /app/cold_email_generator-0.1.0-py3-none-any.whl
RUN mkdir -p /home/app/.cache && \
    groupadd app && \
    useradd -g app -d /home/app app && \
    chown -R app:app /home/app
CMD [ "cold-email" ]