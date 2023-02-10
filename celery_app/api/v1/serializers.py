from rest_framework import serializers

from celery_app.models import Calculation, PeriodicTaskCreation


class BackgroundFibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = "__all__"
        read_only_fields = ["output"]

class PeriodicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTaskCreation
        fields = "__all__"
