FROM python:3.10

# Set the working directory in the container.
WORKDIR /moose

# Copy the requirements file to the working directory.
COPY requirements.txt /moose/

# Install the required packages.
RUN pip3 install -r requirements.txt

# Copy the rest of the application code to the working directory.
COPY . /moose/

# Run database migrations.
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Expose the port on which the Django app runs.
EXPOSE 8000

# Run the Django application using the development server.
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
