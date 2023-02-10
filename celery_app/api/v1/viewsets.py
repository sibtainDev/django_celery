from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from celery_app.api.v1.serializers import BackgroundFibSerializer, PeriodicTaskSerializer
from celery_app.models import Calculation, PeriodicTaskCreation
from celery_app.tasks import fibonacci_task


# celery background task and celery periodic task with celery beat

class BackgroundFibonacciTask(ModelViewSet):
    serializer_class = BackgroundFibSerializer
    permission_classes = [AllowAny]
    queryset = Calculation.objects.all()

    def create(self, request, *args, **kwargs):
        input = request.data.get("input")
        obj = Calculation.objects.create(input=input)
        fibonacci_task.delay(obj.id)
        return Response({"message": "FibonacciTask has been completed"}, status=status.HTTP_201_CREATED)


class PeriodicTaskViewSet(ModelViewSet):
    serializer_class = PeriodicTaskSerializer
    permission_classes = [AllowAny]
    queryset = PeriodicTaskCreation.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        clock = ClockedSchedule.objects.create(clocked_time=obj.task_date_time)
        PeriodicTask.objects.create(name=obj.task_name, clocked=clock, task='celery_app.tasks.periodic_task', one_off=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
