#views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.

from rest_framework import viewsets

from .serializers import produce_ordersSerializer
from .serializers import vertical_farm_1Serializer
from .serializers import vertical_farm_2Serializer
from .serializers import vertical_farm_3Serializer
from .serializers import vertical_farm_4Serializer
from .serializers import vertical_farm_5Serializer
from .serializers import vertical_farm_6Serializer
from .serializers import vertical_farm_7Serializer
from .serializers import vertical_farm_8Serializer
from .serializers import vertical_farm_9Serializer
from .serializers import vertical_farm_10Serializer
from .serializers import rest1Serializer

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


	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_1.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_2.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_3.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_4.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_5.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_6.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_7.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_8.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_9.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = vertical_farm_10.objects.all()
	return render(request, "index.html", {'query_results':query_results})

def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = produce_orders.objects.all()
	return render(request, "index.html", {'query_results':query_results})

def UI_Supermarket_Restaurant(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	query_results = rest1.objects.all()
	return render(request, "index.html", {'query_results':query_results})
	
class vertical_farm_1ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_1.objects.all().order_by('idVf1', 'Available_capacity')
    serializer_class = vertical_farm_1Serializer
	
class vertical_farm_2ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_2.objects.all().order_by('idVf2', 'Available_capacity')
    serializer_class = vertical_farm_2Serializer
	
class vertical_farm_3ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_3.objects.all().order_by('idVf3', 'Available_capacity')
    serializer_class = vertical_farm_3Serializer
	
class vertical_farm_4ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_4.objects.all().order_by('idVf4', 'Available_capacity')
    serializer_class = vertical_farm_4Serializer

class vertical_farm_5ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_5.objects.all().order_by('idVf5', 'Available_capacity')
    serializer_class = vertical_farm_5Serializer

class vertical_farm_6ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_6.objects.all().order_by('idVf6', 'Available_capacity')
    serializer_class = vertical_farm_6Serializer
	
class vertical_farm_7ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_7.objects.all().order_by('idVf7', 'Available_capacity')
    serializer_class = vertical_farm_7Serializer
	
class vertical_farm_8ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_8.objects.all().order_by('idVf8', 'Available_capacity')
    serializer_class = vertical_farm_8Serializer
	
class vertical_farm_9ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_9.objects.all().order_by('idVf9', 'Available_capacity')
    serializer_class = vertical_farm_9Serializer
	
class vertical_farm_10ViewSet(viewsets.ModelViewSet):
    queryset = vertical_farm_10.objects.all().order_by('idVf10', 'Available_capacity')
    serializer_class = vertical_farm_10Serializer
	
class produce_ordersViewSet(viewsets.ModelViewSet):
    queryset = produce_orders.objects.all().order_by('idOrder', 'Produce_type', 'Qty')
    serializer_class = produce_ordersSerializer

class rest1ViewSet(viewsets.ModelViewSet):
    queryset = rest1.objects.all().order_by('Nomenclature', 'Qty', 'Unit', 'Deliver', 'PLU', 'Price')
    serializer_class = produce_ordersSerializer
	
	
def index(request):
    return render("index.html", context_instance=RequestContext(request))
