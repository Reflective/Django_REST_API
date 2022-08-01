# Response will render serialized python data as a json
from rest_framework.response import Response

# Decorators are necessary for function based views
from rest_framework.decorators import api_view
from base.models import Name
from .serializers import NameSerializer


# process serialized data using Response
@api_view(["GET"])
def getData(request):
    items = Name.objects.all()
    #  many=True allows for serializer to process multiple items
    serializer = NameSerializer(items, many=True)
    # Response will return model data as json data
    return Response(NameSerializer.data)

# returns validated serialized data from POST
@api_view(["POST"]) 
def addItem(request):
    serializer = NameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() #adds new db entry
    return Response(serializer.data)
