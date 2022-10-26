from . import views
from rest_framework import routers
from django.urls import include,path

router = routers.DefaultRouetr()
router.register(r'posts',views.PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]