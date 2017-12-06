from rest_framework import serializers
from models import Employeeteam, Employeename

class EmployeeteamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeeteam
        fields = ('__all__')
class EmployeenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeename
        fields = ('__all__')
