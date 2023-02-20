from rest_framework import viewsets,mixins,generics

from .models import Women
from .serializers import WomenSerializerList,WomenSerializer


class WomenListAPIView(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializerList

class WomenAPIViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


