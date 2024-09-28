from django.urls import path
from .views import ItemCreateView, ItemDetailView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='create_item'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
