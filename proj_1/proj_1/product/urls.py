from django.urls import path
from .views import *
from .models import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'products', BaseProductView, basename=BaseProduct)

urlpatterns = []

urlpatterns += router.urls