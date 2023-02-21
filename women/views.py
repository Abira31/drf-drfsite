from rest_framework import generics

from .models import Women
from .serializers import WomenSerializerList,WomenSerializer


class WomenAPIList(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializerList


class WomenAPICreate(generics.CreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
