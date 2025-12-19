from django.urls import path,include

from rest_framework import routers
from users.views import UserViewset
import users.views as views

router=routers.DefaultRouter()

router.register(r'users',UserViewset)
urlpatterns = [
    path('',include(router.urls))
    # path('hello',views.home)
]
