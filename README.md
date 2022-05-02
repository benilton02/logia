# logia
logia


## Inside container
python manage.py makemigrations logia
python manage.py migrate logia
python manage.py migrate --run-syncdb 

## Inside container
apply an specific fixture (example):
python manage.py loaddata logia/fixture/pharmacies_model.json

## Inside container
apply all fixtures:
python manage.py loaddata logia/fixture/*