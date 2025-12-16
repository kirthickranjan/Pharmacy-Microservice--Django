from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                self.permission_denied(
                    self.request,
                    message="Only admin can manage stocks"
                )
        return super().get_permissions()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin → All orders
        if user.is_staff:
            return Order.objects.all()

        # User → Own orders only
        return Order.objects.filter(user_email=user.email)

    def perform_create(self, serializer):
        serializer.save(user_email=self.request.user.email)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                self.permission_denied(
                    self.request,
                    message="Only admin can manage orders"
                )
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def my_orders(self, request):
        orders = Order.objects.filter(user_email=request.user.email)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    return Response({
        'status': 'healthy',
        'service': 'Stock Service',
        'port': 8082
    })
