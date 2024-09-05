# Prerequisites
#####
- Python3.10
- Django 5
- Remote MariaDB


docker build \
  --build-arg DB_NAME='superdjango' \
  --build-arg DB_USER='admin' \
  --build-arg DB_PASS='root' \
  --build-arg DB_HOST='192.168.56.28' \
  --build-arg DB_PORT=3306 \
  -t propfeed:latest .

pytest --cov --cov-report=xml

