from rest_framework import serializers

from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    class Meta:
        model = Women
        fields = ['pk','title','content','cat']