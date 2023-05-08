VEMS (Virtual Event Management System) is a web application that allows users to manage events. It was developed using Flask and SQLAlchemy, and includes features such as event creation, editing, and deletion, venue management, user authentication, and more.

![image](https://user-images.githubusercontent.com/97791913/236888809-6945966e-2570-46e7-8dcf-a464bd2208ea.png)
![image](https://user-images.githubusercontent.com/97791913/236888858-ed914485-19f7-4455-b665-84d848f1708e.png)
![image](https://user-images.githubusercontent.com/97791913/236888926-e3ef8fce-72c7-4300-85ae-e77f32fd4ad2.png)
![image](https://user-images.githubusercontent.com/97791913/236888965-f887c927-101e-42b3-a9c9-6371114bdc76.png)
![image](https://user-images.githubusercontent.com/97791913/236889007-c2445636-43a9-4b50-b38d-ee3dd8d71fbb.png)
![image](https://user-images.githubusercontent.com/97791913/236889035-137b308e-0645-485f-bad3-896ed557d298.png)


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
