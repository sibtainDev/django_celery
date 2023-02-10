from rest_framework import routers

from celery_app.api.v1.viewsets import BackgroundFibonacciTask, PeriodicTaskViewSet

router = routers.SimpleRouter()

router.register("background_task", BackgroundFibonacciTask, basename='background_task')
router.register("periodic_task", PeriodicTaskViewSet, basename='periodic_task')

urlpatterns = router.urls
