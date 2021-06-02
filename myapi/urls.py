from django.db import router
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework import viewsets

from .serializers import EmployeeSerializer
from .models import Employee
from .views import DeleteTodoAPIView

router = routers.DefaultRouter()
router.register( r'employee', views.EmployeeViewSet )

app_name = 'myapi'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path( '', include( router.urls ) ),
    path( 'api-auth/', include( 'rest_framework.urls', namespace='rest_framework' ) ),
    path('delete/<int:pk>/', DeleteTodoAPIView.as_view(), name='delete' ),
    #path( 'getemployees_all/', views.getemployees, name='getemployees_all' ),
]




