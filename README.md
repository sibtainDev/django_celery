# django_celery

### This project is related to django celery and celery_beat.
In this project i am creating two task first one is back_ground task and another one is periodic task
for background task input any value and the backeground task will save the output in a model and the periodic task just print statement
You can use your own logic for these task but i am giving you complete celery running project.


### Steps
- install all dependencies using pipenv install
- python manage.py migrate
- python manage.py runserver
## Now run celery worker and celery Beat using these commands
**1. celery -A project_name worker -l INFO**

**2. celery -A project_name beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler**

