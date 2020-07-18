## Test task: Scraping citrus.ua and API with Django Rest Framework

#### Implement:
  1. used Django Rest Framework
  2. models: ProductItem
  3. scraping with HTMLSession, BeautifulSoup
  4. Celery, Redis
  5. testing models, views, urls
  
#### Urls:
1. main page with one button  ```/```
2. list of all scraping items ```items/```
3. list of iPhones ```items/phone```
4. list of notebooks ```items/notebook```
```
{
    "all likes at 2020-07-16 to 2020-07-17": 5,
    "daily likes": {
        "2020-07-16": 2,
        "2020-07-17": 3
    }
}
```

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

