from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet,ProductsViewSet

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductsViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]