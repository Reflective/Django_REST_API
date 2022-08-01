# convert instances of models from python objects into serialized data
# that can be converted by Response
from rest_framework import serializers
from base.models import Name

# A good naming convention for serializers is: <ModelName>Serializer() 
class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'  #__all__ will take all fields within model
        
        