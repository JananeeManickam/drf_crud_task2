from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ToySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Toy

# Create your views here.
# POST api
class ToyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Response converts py obj into json.
            return Response({'data':serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        qs = Toy.objects.all()
        serializer = ToySerializer(qs, many=True)
        return Response({ 'data': serializer.data })
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Toy.objects.get(toy_name=pk)
        serializer = ToySerializer(instance=instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = Toy.objects.get(toy_name=pk)
        except Toy.DoesNotExist:
            return Response({'error': 'Toy not found'}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({'message': 'Object has been deleted.'})
        