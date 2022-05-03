docker-compose up --build -d &&
docker exec logia_api python manage.py migrate &&
docker exec logia_api python manage.py loaddata logia/fixture/* &&
docker-compose up --build
