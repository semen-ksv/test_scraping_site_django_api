## Test task: Simple REST API with Django Rest Framework

#### Implement:
  1. used Django Rest Framework
  2. models: SimpleUser inheritance AbstractUser, Post, Like
  2. JWT token authentication
  3. swagger documentations
  4. testing models, auth, views, urls
  
#### Urls:
1. user signup ```auth/users/```
2. user login (get JWT token) ```api/token/```
3. show all posts ```api/post/```
4. post creation ```api/post/create/```
5. post updating ```api/post/<post_slug>/update/```
6. post deleting ```api/post/<post_slug>/delete/```
7. post like ```api/post/<post_slug>/like/```
8. post unlike ```api/post/<post_slug>/unlike/```
9. analytics about how many likes was made for one day ```api/post/date_<YYYY-MM-DD>/```
10. like analytics for range of days ```api/post/date-from_<YYYY-MM-DD>-date-to_<YYYY-MM-DD>/```
```
{
    "all likes at 2020-07-16 to 2020-07-17": 5,
    "daily likes": {
        "2020-07-16": 2,
        "2020-07-17": 3
    }
}
```
11\. user activity show when user was login last time and when he made a last request ```user/```
```
{
    "id": 2,
    "username": "sem",
    "last_login": "2020-07-16T22:01:52.763687Z",
    "last_request": "2020-07-16T22:03:18.935197Z"
}
```
12\. Swagger page ```swagger/```


Passed tests


### Running project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
 or 
 ```
 env\Scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Migrate for creating all tables 

```
python manage.py migrate
```

Now you can run the project with this command

```
python manage.py runserver
```

