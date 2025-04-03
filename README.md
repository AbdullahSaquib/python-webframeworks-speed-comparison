## AWS EC2 Instance Setup


    sudo dnf update -y
    sudo dnf install git -y
    git clone https://github.com/AbdullahSaquib/python-webframeworks-speed-comparison.git
    cd python-webframeworks-speed-comparison
    sudo dnf install python3.11 -y
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


## Run Flask App

    gunicorn flask_app.main:app --workers 342  --bind 0.0.0.0:8000


## Run Django App

1. WSGI

    cd django_app/ && gunicorn django_app.wsgi:application --workers 4 --bind 0.0.0.0:8000

2. ASGI

    cd django_app/ && gunicorn django_app.asgi:application -k uvicorn.workers.UvicornWorker --workers 4 --bind 0.0.0.0:8000


## Run Fastapi App

    gunicorn -k uvicorn.workers.UvicornWorker fastapi_app.main:app --workers 4 --bind 0.0.0.0:8000


## Run WRK

    cd 
    git clone https://github.com/wg/wrk.git
    cd wrk
    sudo dnf groupinstall "Development Tools" -y
    make
    sudo cp wrk /usr/local/bin
    cd  
    cd python-webframeworks-speed-comparison
    python wrk.py

