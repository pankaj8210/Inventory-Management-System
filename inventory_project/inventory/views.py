from rest_framework import status, generics
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        item = cache.get(f'item_{item_id}')
        if not item:
            item = self.get_object()
            cache.set(f'item_{item_id}', item)
        return Response(ItemSerializer(item).data)
