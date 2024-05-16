from rest_framework import serializers
from .models import Toy
# serializers convert a py obj into json for convenience
class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'
        
        