from django.urls import path

from . import views

urlpatterns = [
    path('', views.PropertyList.as_view()),
    path('view/<int:pk>', views.PropertyView.as_view(), name='view'),
    path('new', views.PropertyCreate.as_view(), name='new'),
    # path('view/<int:pk>', views.PropertyView.as_view(), name='view'),
    path('edit/<int:pk>', views.PropertyUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.PropertyDelete.as_view(), name='delete'),
]