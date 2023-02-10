from django_celery.celery import app
from celery_app.models import Calculation

from celery import shared_task

def fib(n):
    """Calculate the Nth fibonacci number"""
    if n < 0:
        raise ValueError('Negative numbers are not supported')
    elif n == 0:
        return 0
    elif n <= 2:
        return 1

    return fib(n - 2) + fib(n - 1)


@app.task(bind=True)
def fibonacci_task(self, calculation_id):
    """Perform a calculation & update the status"""
    calculation = Calculation.objects.get(id=calculation_id)

    try:
        calculation.output = fib(calculation.input)
        print("Calculation completed")
    except Exception as e:
        print(e)

    calculation.save()

@shared_task()
def periodic_task():
    """
    This task will be schedule user will set the time
    and that time an email can be send or a notification can be send
     """

    print("create schedule task by setting time from user")