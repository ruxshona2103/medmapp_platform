from rest_framework import serializers
from .models import ServiceIntro, JourneyStep, JourneyStepItem
from core.models import Specialty

class ServiceIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceIntro
        fields = ("title", "subtitle", "button_text", "meta_title", "meta_description", "meta_keywords")

class JourneyStepItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneyStepItem
        fields = ("text", "order")

class JourneyStepSerializer(serializers.ModelSerializer):
    items = JourneyStepItemSerializer(many=True, read_only=True)
    class Meta:
        model = JourneyStep
        fields = ("order", "step_number", "title", "description", "icon_svg", "items")

# TZ: mutaxassisliklar qisqa ko‘rinishda
class SpecialtyBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ("id", "title", "description", "icon_svg", "order")
