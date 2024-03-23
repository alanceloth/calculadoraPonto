# Use the official Python image as a base image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Allow installing as root
ENV POETRY_VIRTUALENVS_CREATE=false

# Copy only the dependencies definition file to optimize caching
COPY poetry.lock pyproject.toml ./
COPY .python-version ./

# Install dependencies
RUN /root/.poetry/bin/poetry install --no-dev

# Copy all files from the current directory into the container at /app
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app when the container starts
CMD ["/root/.poetry/bin/poetry", "run", "streamlit", "run", "frontend.py"]
