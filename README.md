# proboston-test
Test project for Proboston interview

## Local Installation

The very first step is to clone this repo. 

```
git clone https://github.com/josewails/proboston-test.git
```


Once cloned, there are two ways to run the project locally. 

### Using Docker 

With docker and docker-compose installed follow the following the steps:


+ Run `docker-compose up` to run the project. 
+ Head over to [https://localhost:8000](https://localhost:8000) to add new records.
+ Run `docker-compose exec web python manage.py createsuperuser` to create a superuser to test admin. 



### The normal way. 

+ Run `python manage.py migrate` to create the db. 
+ RUN `python manage.py runserver` to run the server. 
+ Head over to [https://localhost:8000](https://localhost:8000) to add new records.
+ RUN `python manage.py createsuperuser` to create a superuser to test the admin. 
