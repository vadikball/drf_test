from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from cars import views

router = routers.DefaultRouter()
router.register(r'colors', views.ColorViewSet, 'colors')
router.register(r'brands', views.BrandViewSet, 'brands')
router.register(r'car_models', views.CarModelViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'ordered_color', views.OrderedColorViewSet)
router.register(r'ordered_brand', views.OrderedBrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi', get_schema_view(
            title="DRF Test Project",
            description="API for Cars",
            version="1.0.0"
        ), name='openapi-schema'),
]