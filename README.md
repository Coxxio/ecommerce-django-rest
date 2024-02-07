## Installation

Poetry provides a custom installer that will install `poetry` isolated
from the rest of your system.

### osx / linux / bashonwindows install instructions
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### windows powershell install instructions
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Clone the repository 
Clone with SSH
```bash
git clone git@gitlab.com:Coxxio/ecommerce-back-django.git
```
Or Clone with HTTPS
```bash
https://gitlab.com/Coxxio/ecommerce-back-django.git
```

### Install dependencies
```bash
cd ecommerce-back-django
```
```bash
poetry install
```

### Create the database

### Configure the .env file

### Getting started
```bash
poetry run manage.py makemigrations
```
```bash
poetry run manage.py migrate
```
```bash
poetry run manage.py createsuperuser
```
```bash
poetry run manage.py runserver
```
