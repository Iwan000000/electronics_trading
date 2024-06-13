from django.urls import path

from network.apps import NetworkConfig
from network.views import UnitCreateAPIView, UnitListAPIView, UnitUpdateAPIView, UnitRetrieveAPIView, UnitDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('units/create/', UnitCreateAPIView.as_view(), name='unit-create'),
    path('units/', UnitListAPIView.as_view(), name='unit-list'),
    path('units/<int:pk>/', UnitRetrieveAPIView.as_view(), name='unit-get'),
    path('units/update/<int:pk>/', UnitUpdateAPIView.as_view(), name='unit-update'),
    path('units/delete/<int:pk>/', UnitDestroyAPIView.as_view(), name='unit-delete')
]
