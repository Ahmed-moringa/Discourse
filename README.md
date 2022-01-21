# Discourse

## Author

[Ahmed Mohamed](https://github.com/Ahmed-moringa)

# Description
A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## User Story
1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3. As a user, I would like to view the most recent posts
4. As a user, I would like to an email alert when a new post is made by joining a subscription.
5. As a user, I would like to see random quotes on the site
6. As a writer, I would like to sign in to the blog.
7. As a writer, I would also like to create a blog from the application.
8. As a writer, I would like to delete comments that I find insulting or degrading.
9. As a writer, I would like to update or delete blogs I have created.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Ahmed-moringa/Discourse.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Pitch_me
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/discourse'
  ```
4. Running the application
  ```bash
  python3 manage.py server
  ```
5. Testing the application
  ```bash
  python3 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## License
* *MIT License:*
* Copyright (c) 2022 **Ahmed Mohamed**