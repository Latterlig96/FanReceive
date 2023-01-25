web: gunicorn --bind 127.0.0.1:8000 --workers=1 --threads=15 fanreceive.wsgi:application

celery_worker: celery worker -A fanreceive.settings.celery.app --loglevel=INFO

celery_beat: celery beat -A fanreceive.settings.celery.app --loglevel=INFO
