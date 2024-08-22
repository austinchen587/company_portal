# Use an official Python runtime as parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt . 

# Install any needed packages specified in requirement.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHOMUNBUFFERED 1

# Run app.py when the container launches
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
