from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Prescription
from .serializers import PrescriptionSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def prescription_list(request):

    # View all prescriptions (Admin & User)
    if request.method == 'GET':
        prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create prescription (Admin only)
    elif request.method == 'POST':
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin can add prescriptions'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Prescription inserted successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def prescription_detail(request, pk):

    try:
        prescription = Prescription.objects.get(pk=pk)
    except Prescription.DoesNotExist:
        return Response(
            {'error': 'Prescription not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    # View prescription (Admin & User)
    if request.method == 'GET':
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update prescription (Admin only)
    elif request.method == 'PUT':
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin can update prescriptions'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Prescription updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete prescription (Admin only)
    elif request.method == 'DELETE':
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin can delete prescriptions'},
                status=status.HTTP_403_FORBIDDEN
            )

        prescription.delete()
        return Response(
            {'message': 'Prescription deleted successfully'},
            status=status.HTTP_200_OK
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    return Response({
        'status': 'healthy',
        'service': 'Prescription Service',
        'port': 8081
    })
