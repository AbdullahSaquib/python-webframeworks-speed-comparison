## Run Flask App

    gunicorn flask_app.main:app --workers 32  --bind 0.0.0.0:8000


## Run Django App

1. WSGI

    cd django_app/ && gunicorn django_app.wsgi:application --workers 32 --bind 0.0.0.0:8000

2. ASGI

    cd django_app/ && gunicorn django_app.asgi:application -k uvicorn.workers.UvicornWorker --workers 32 --bind 0.0.0.0:8000


## Run Fastapi App

    gunicorn -k uvicorn.workers.UvicornWorker fastapi_app.main:app --workers 32 --bind 0.0.0.0:8000


## Run WRK

    python wrk.py

