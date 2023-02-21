from rest_framework import serializers

from .models import Women,Category

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class WomenSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['url','pk','title','content','cat','user']
class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = '__all__'


