from rest_framework import generics,viewsets,mixins

from .models import Women
from .serializers import WomenSerializer


class WomenAPIViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

