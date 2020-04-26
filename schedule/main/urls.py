from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.schedule,name='schedule'),
    path('new',views.new,name='new'),
    path('edit',views.edit,name='edit'),
]

