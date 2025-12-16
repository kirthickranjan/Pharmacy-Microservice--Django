from rest_framework import serializers
from .models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    prescriptionId = serializers.IntegerField(source='id', read_only=True)
    providerName = serializers.CharField(source='provider_name')
    patientName = serializers.CharField(source='patient_name')
    medicineName = serializers.CharField(source='medicine_name')
    followupDate = serializers.CharField(source='followup_date')
    followupNotes = serializers.CharField(source='followup_notes', required=False, allow_blank=True)
    
    class Meta:
        model = Prescription
        fields = ['prescriptionId', 'providerName', 'patientName', 'medicineName', 
                 'dosage', 'followupDate', 'followupNotes']