# Project: Permissions & Postgresql

## Author: Osama Maher

## Setup

- activate virtual enviroment with `source .venv/bin/activate`
- then run `docker-compose up --build`
- open a split terminal and run this command `docker-compose run web python manage.py migrate`
- create super user with this command `docker-compose run web python manage.py createsuperuser`

## How do you run tests

- `docker-compose run web python manage.py test`
## pull request 
[my pull request](https://github.com/osamadado123/drf-api-permissions-postgres/pull/1)
