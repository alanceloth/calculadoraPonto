FROM python:3.11.5-slim
RUN pip install poetry
COPY . /src
WORKDIR /src
RUN poetry install --no-dev
EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
