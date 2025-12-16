from django.db import models

class Prescription(models.Model):
    provider_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    followup_date = models.CharField(max_length=100)
    followup_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'prescriptions'
    
    def __str__(self):
        return f"{self.patient_name} - {self.medicine_name}"