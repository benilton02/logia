docker-compose up --build -d &&
docker exec logia_web_1 python manage.py migrate &&
docker exec logia_web_1 python manage.py loaddata logia/fixture/* &&
docker-compose up --build
