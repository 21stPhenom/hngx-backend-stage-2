from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Person
from api.serializers import PersonSerializer

# Create your views here.
class BasePersonView(APIView):
    serializer = PersonSerializer
    queryset = Person.objects.all

    def get_queryset(self):
        return self.queryset()
    
    def get(self, request, *args, **kwargs):
        # Get every Person object from the database
        persons = self.serializer(self.get_queryset(), many=True)
        return Response(persons.data, status=200)

    def post(self, request, *args, **kwargs):
        new_person = self.serializer(data=request.data) # Parse the data sent in the request

        # Create and return a new Person object only if there's no person with the same name
        if new_person.is_valid():
            if not Person.objects.filter(name=request.data['name']).exists():
                new_person.save()
                return Response(new_person.data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "message": f"Person with name `{request.data['name']}` already exists."},
                    status=status.HTTP_400_BAD_REQUEST)
            
        # Return errors if the data is invalid
        return Response(new_person.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadUpdateDeleteView(APIView):
    serializer = PersonSerializer

    def get(self, request, user_id=None, *args, **kwargs):
        # Read info aobut a person using id or name
        name = request.query_params.get('name')
        if name:
            person = get_object_or_404(Person, name=name)
        else:
            person = get_object_or_404(Person, pk=user_id)
        serialized_person = self.serializer(person)
        
        return Response(serialized_person.data, status=status.HTTP_200_OK)
        
    def put(self, request, user_id, *args, **kwargs):
        # Update info aobut a person using id or name
        name = request.query_params.get('name')
        if name:
            person = get_object_or_404(Person, name=name)
        else:
            person = get_object_or_404(Person, pk=user_id)
        update_data = self.serializer(person, data=request.data)

        # Update and return an existing Person object only if there's no person with the new name.
        if update_data.is_valid():
            if not Person.objects.filter(name=request.data['name'] or request.query_params['name']).exists():
                update_data.save()
                return Response(update_data.data, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": f"Person with name `{request.data['name']}` already exists."},
                    status=status.HTTP_400_BAD_REQUEST)
        
        # Return errors if the data is invalid
        return Response(update_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):
        # Read info aobut a person using id or name
        name = request.query_params.get('name')
        if name:
            person = get_object_or_404(Person, name=name)
        else:
            person = get_object_or_404(Person, pk=user_id)
        person.delete()
        return Response({
            "message": f"Person with id {user_id} has been deleted"
        }, status=status.HTTP_204_NO_CONTENT)

base_view = BasePersonView.as_view()
rud_view = ReadUpdateDeleteView.as_view()
