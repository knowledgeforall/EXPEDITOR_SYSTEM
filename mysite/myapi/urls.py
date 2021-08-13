# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'produce_orders', views.produce_ordersViewSet)
router.register(r'vertical_farm_1', views.vertical_farm_1ViewSet)
router.register(r'vertical_farm_2', views.vertical_farm_2ViewSet)
router.register(r'vertical_farm_3', views.vertical_farm_3ViewSet)
router.register(r'vertical_farm_4', views.vertical_farm_4ViewSet)
router.register(r'vertical_farm_5', views.vertical_farm_5ViewSet)
router.register(r'vertical_farm_6', views.vertical_farm_6ViewSet)
router.register(r'vertical_farm_7', views.vertical_farm_7ViewSet)
router.register(r'vertical_farm_8', views.vertical_farm_8ViewSet)
router.register(r'vertical_farm_9', views.vertical_farm_9ViewSet)
router.register(r'vertical_farm_10', views.vertical_farm_10ViewSet)
router.register(r'rest1', views.rest1ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
]