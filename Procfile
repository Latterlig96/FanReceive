web: gunicorn --bind 127.0.0.1:8000 --workers=1 --threads=15 fanreceive.wsgi:application

celery: celery -A fanreceive worker --loglevel=INFO

celery-beat: celery -A fanreceive beat --loglevel=INFO
