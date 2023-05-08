VEMS
VEMS (Venue Event Management System) is a web application that allows users to manage events at various venues. It was developed using Flask and SQLAlchemy, and includes features such as event creation, editing, and deletion, venue management, user authentication, and more.

Installation
To run VEMS on your local machine, you'll need to follow these steps:

Clone the repository: git clone https://github.com/JAMl3/vems.git
Install the required packages: pip install -r requirements.txt
Set up the database: python manage.py db init, python manage.py db migrate, python manage.py db upgrade
Start the server: python manage.py runserver
Usage
Once the server is running, you can access the VEMS application by navigating to http://localhost:5000 in your web browser. From there, you can create a new user account or log in to an existing one, and start managing events and venues.

Contributing
If you'd like to contribute to VEMS, feel free to fork the repository and submit a pull request. Be sure to follow the project's code style and guidelines, and include tests for any new functionality you add.

License
VEMS is licensed under the MIT License. See LICENSE for more information.
