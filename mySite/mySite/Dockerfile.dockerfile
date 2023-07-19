# Use an official Python runtime as the base image
FROM Python:3.11.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port on which your Django app will run
EXPOSE 8000

# Define the command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
