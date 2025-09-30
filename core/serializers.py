from rest_framework import serializers
from .models import SiteSettings, Specialty, Statistic, WorkStep, ServiceCard


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = "__all__"


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"


class WorkStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStep
        fields = "__all__"


class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCard
        fields = "__all__"
