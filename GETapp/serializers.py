from rest_framework import serializers
from GETapp.models import Model
  
  
class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Model
        fields=['student','classroom']