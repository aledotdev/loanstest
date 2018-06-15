# Loans Test

## How to setup

Runs with python 3

```
python -m venv .env
source .env/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Run tests

`python manage.py test`

### Run webapp

`python manage.py runserver`


## Loans urls

##### Request Loan View

`http://localhost:8000/loans/`

##### Loans List View
Needs to be logged as admin user (`http://localhost:8000/admin/`)

`http://localhost:8000/loans/list/`
