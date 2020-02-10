from rest_framework import routers
from my_api import views 
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
#router.register(r'operations',views.operations)
