# Grab official image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
RUN mkdir /src
RUN mkdir /src/requirements
WORKDIR /src

# Install Python dependencies
COPY ./requirements/base.txt /src/requirements/base.txt
COPY ./requirements/development.txt /src/requirements/development.txt
RUN pip install -r /src/requirements/development.txt

# Copy project
COPY . /src

# Expose port
EXPOSE 8000
