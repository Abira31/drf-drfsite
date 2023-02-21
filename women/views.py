from rest_framework import generics
from rest_framework import permissions
from .models import Women
from .serializers import WomenSerializerList,WomenSerializer
from .permissions import IsAdminOrReadOnly,IsWonerOrReadOnly


class WomenAPIList(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializerList
    name = 'womens-list'


class WomenAPICreate(generics.CreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsWonerOrReadOnly,)
    name = 'women-detail'

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
