# Create your views here.
from rest_framework import generics
from .models import FaceModel
from .serializers import FaceModelSerializer

class FaceModelListCreateView(generics.ListCreateAPIView):
    queryset = FaceModel.objects.all()
    serializer_class = FaceModelSerializer
