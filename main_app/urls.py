from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.listsCreate.as_view(), name='lists_create'),
    path('delete/<int:lists_id>', views.delete, name='delete'),
]