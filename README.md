# FARMER BACKEND APPLICATION using DJANGO & REST

Django app to register and authenticate user using REST API framework.

## How to use:
-  open the folder in vs code or any software of your choice.
-  open postman
- `pip install -r requirements.txt`
- `python manage.py runserver`

On the running server:

## URLs to target:

- to register a user
  - localhost:8000/api/addUser/
     => Add key and value :-
        * Username
        * Email
        * Password
(A user is registered)
        
- to login a user
  - localhost:8000/api/login/
       => Add key and value :-
        * Username
        * Password
        
        
- to upload a file
  - localhost:8000/api/upload/
       => Add key and value :-
        * add file location to files
        
- to translate the file
  - open translate.py
       => Run using `python3 translate.py
       * choose the target language source
       * file will be converted from the detected language to target language
        
- to logout a user
  - localhost:8000/api/logout/
  
- to view all data
  - localhost:8000/api/admin/
       => login using the user
       
## API Call examples:

- `curl -X POST http://localhost:8000/api/addUser/ -d "email=test@test.com&password=abcd123&username=test"`
- `curl -X POST http://localhost:8000/api/login/ -d "email=test@test.com&password=abcd123"`
- `curl -X POST http://localhost:8000/api/logout/ -d "token=b75f9fc8-f598-4d4c-8698-d98ee808c1f3"`

## Note: token is generated using uuid package.

## Useful commands:

- `python manage.py createsuperuser`
- `python manage.py makemigrations`
- `python manage.py migrate`
