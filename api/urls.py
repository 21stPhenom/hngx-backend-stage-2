from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('', views.base_view, name='list-create'),
    path('<int:user_id>', views.rud_view, name='read-update-delete'),
]