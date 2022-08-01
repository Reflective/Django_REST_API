# Response will render serialized python data as a json
from rest_framework.response import Response
# Allows for decorators on function based views
from rest_framework.decorators import api_view


@api_view(['GET']) 
def getData(request):
    person = {'name':'Brandon', 'age':32}    
    return Response(person)  # Response will return dictionary as json data

