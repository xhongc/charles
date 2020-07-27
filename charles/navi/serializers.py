from rest_framework import serializers

from charles.navi.models import Category, Nana


class ListNanaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nana
        fields = '__all__'


class ListNanaCategorySerializers(serializers.ModelSerializer):
    cates = ListNanaSerializers(many=True)

    class Meta:
        model = Category
        fields = '__all__'
