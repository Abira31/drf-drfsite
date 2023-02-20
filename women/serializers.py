from rest_framework import serializers

from .models import Women,Category

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class WomenSerializerList(serializers.ModelSerializer):
    cat = CatSerializer(read_only=True)
    class Meta:
        model = Women
        fields = ['pk','title','content','cat']
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['pk','title','content','cat']

