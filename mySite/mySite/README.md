# MySite

MySite is a Django web application that allows users to create and publish blog posts.

## Setup and Usage

### Using venv

1. Clone the repository:

```shell
git clone https://github.com/your-username/mySite.git

2. Navigate to the project directory:

cd mySite

3. Create a virtual environment and activate it:

python -m venv myvenv

source myvenv/bin/activate

4. Install the dependencies:

pip install -r requirements.txt

5. Apply the database migrations:

python manage.py migrate

6. Create a superuser for accessing the admin panel:

python manage.py createsuperuser

7. Run the development server:

python manage.py runserver

8. Access the application in your browser at http://localhost:8000.


Using Docker

1. Clone the repository:

git clone https://github.com/your-username/mySite.git

2. Navigate to the project directory:

cd mySite

3. Build the Docker image:

docker build -t mysite .

4. Run a Docker container:

docker run -p 8000:8000 mysite

5. Access the application in your browser at http://localhost:8000.


Dependencies

Python 3.x
Django 3.x
Other dependencies are listed in the requirements.txt file.


Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
