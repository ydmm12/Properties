from rest_framework import serializers
from API.models import APIModel

class APISerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)
    area = serializers.DecimalField(min_value=0, max_value=100000, max_digits=5)
    email = serializers.EmailField(max_length=50)
    
    def create(self, data):
        instance = APIModel()
        instance.name = data.get('name')
        instance.address = data.get('address')
        instance.area = data.get('area')
        instance.email = data.get('email')
        instance.save()
        return instance