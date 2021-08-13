# serializers.py

from rest_framework import serializers

from .models import produce_orders
from .models import vertical_farm_1
from .models import vertical_farm_2
from .models import vertical_farm_3
from .models import vertical_farm_4
from .models import vertical_farm_5
from .models import vertical_farm_6
from .models import vertical_farm_7
from .models import vertical_farm_8
from .models import vertical_farm_9
from .models import vertical_farm_10
from .models import rest1

class vertical_farm_1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_1
        fields = ('idVf1', 'Available_capacity')
		
class vertical_farm_2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_2
        fields = ('idVf2', 'Available_capacity')
		
class vertical_farm_3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_3
        fields = ('idVf3', 'Available_capacity')
		
class vertical_farm_4Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_4
        fields = ('idVf4', 'Available_capacity')
		
class vertical_farm_5Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_5
        fields = ('idVf5', 'Available_capacity')
		
class vertical_farm_6Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_6
        fields = ('idVf6', 'Available_capacity')
		
class vertical_farm_7Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_7
        fields = ('idVf7', 'Available_capacity')
		
class vertical_farm_8Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_8
        fields = ('idVf8', 'Available_capacity')
		
class vertical_farm_9Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_9
        fields = ('idVf9', 'Available_capacity')
		
class vertical_farm_10Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vertical_farm_10
        fields = ('idVf10', 'Available_capacity')
		
class produce_ordersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = produce_orders
        fields = ('idOrder', 'Produce_type', 'Qty')

class rest1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rest1
        fields = ('Nomenclature', 'Qty', 'Unit', 'Deliver', 'PLU', 'Price')