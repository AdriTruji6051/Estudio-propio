from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        #Para indicar que solo queremos ciertos datos y no todos
        #fields = ('id', 'tittle', 'description', 'done')

        model = Tasks
        #Para indicar que queremos todos los datos dentro de nuestro modelo
        fields = '__all__'
