from rest_framework import fields,serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        exclude=['id']
        # fields='__all__'

