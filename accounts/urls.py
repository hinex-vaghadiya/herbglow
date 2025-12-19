from django.urls import path,include

from rest_framework import routers
from accounts.views import UserViewset
import accounts.views as views

router=routers.DefaultRouter()

router.register(r'accounts',UserViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('hello',views.home)
]
