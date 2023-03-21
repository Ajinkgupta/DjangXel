# Djangxel - Photo Sharing Platform
=================================

Djangxel is a web-based photo-sharing platform built with Django, a high-level Python web framework. It allows users to create accounts, upload and share photos, follow and unfollow other users, and view profiles.

## Prerequisites
-------------

To run Djangxel on your local machine, you need to have the following software installed:

*   Python 3.6 or higher
*   pip
*   Django 4.1.7
*   asgiref 3.6.0
*   Pillow 9.4.0
*   pytz 2022.7.1
*   sqlparse 0.4.3
*   django-cors-headers 3.14.0
*   django-crispy-forms 2.0
*   djangorestframework 3.12.4
*   tzdata 2022.7

## Installation
------------

1.  Clone the repository to your local machine:
    
    ```git clone https://github.com/ajinkgupta/djangxel.git```
    
2.  Navigate to the project directory:
    
    ```cd djangxel```
    
3.  Install the required packages:
    
    ```pip install -r requirements.txt```
    
4.  Run the migrations:
    
    ```python manage.py migrate```
    
5.  Create a superuser account:
    
     ```python manage.py createsuperuser```
    
6.  Start the development server:
    
    ```python manage.py runserver```
    
7.  Open your web browser and go to [http://localhost:8000](http://localhost:8000/).



    

## Features
--------

*   User authentication (sign-up/sign-in).
*   Image upload.
*   Follow and unfollow other users.
*   Profile page.

## Usage

To use `Djangxel`, follow these steps:

1. Create an account or sign in if you already have one.
2. Upload photos to your account.
3. Follow other users to see their photos in your feed.
4. View your profile page to see your own photos and follower/following lists.





## Contributing

If you want to contribute to Djangxel, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Write tests for your code.
4. Implement your feature/bug fix.
5. Run the tests to make sure everything works.
6. Create a pull request to merge your changes into the main branch.

## Authors

- [Ajinkgupta](https://github.com/Ajinkgupta)

## Acknowledgements

DjangXel was inspired by other popular photo-sharing platforms, including Instagram and Flickr.


## License
-------

Djangxel is released under the MIT License. See [LICENSE](https://github.com/ajinkgupta/djangxel/blob/main/LICENSE) for more information.
