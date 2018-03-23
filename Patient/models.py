from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
TREATMENT_CHOICES = [
    ('Tablet', 'Tablet'),
    ('Oint', 'Oint'),
    ('Syrup', 'Syrup'),
    ('Gel', 'Gel'),
    ('Cream', 'Cream'),
    ('Soap', 'Soap'),
    ('Injection', 'Injection'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class MainComplain(models.Model):
	Name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.Name


class Patient(models.Model):
    Name = models.CharField(max_length=100, blank=False, null=True)
    Age = models.CharField(max_length=100, blank=True, null=True)
    Gender = models.CharField(max_length=100,choices=GENDER_CHOICES, blank=True, null=True)
    Occupation = models.CharField(max_length=100, blank=True, null=True)
    Address = models.TextField(max_length=900, null=True, blank=True)
    Mobile = models.CharField(max_length=100, blank=False, null=True)
    Blood_Group = models.CharField(max_length=100, blank=True, null=True)
    Email_Id = models.CharField(max_length=100, blank=True, null=True)
    Diagnosis = models.CharField(max_length=100, blank=True, null=True)
    Chief_Complains = models.ManyToManyField(MainComplain, editable=True, blank=True)
    Past_History = models.CharField(max_length=100, blank=True, null=True)
    DRUG_Allergy = models.CharField(max_length=100, blank=True, null=True)
    Treatment = models.CharField(max_length=100,choices=TREATMENT_CHOICES, blank=True, null=True)
    Treatment_Desciption = models.CharField(max_length=100, blank=True, null=True)
    Investigation = models.CharField(max_length=100, blank=True, null=True)
    Temperature = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True)
    Blood_Pressure = models.CharField(max_length=100, blank=True, null=True)
    Pulse = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True)
    SPO2 = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True,verbose_name = "SPO2 (%)")
    Birth_date = models.DateField(auto_now_add=False, auto_now=False, null=True,blank=True)
    Reference_Doctor = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(auto_now_add=False, auto_now=False, null=True)

    def __str__(self):
    	return self.Name

class PatientFollowUpCase(models.Model):
	Patient = models.ForeignKey(Patient, editable=True,
                                    blank=True,
                                    null=True,
                                    on_delete=models.SET_NULL)
	Reference_Doctor = models.CharField(max_length=100, blank=True, null=True)
	Complain = models.TextField(max_length=300, null=True, blank=True)
	Treatment = models.CharField(max_length=100,choices=TREATMENT_CHOICES, blank=True, null=True)
	Treatment_Desciption = models.CharField(max_length=100, blank=True, null=True)
	Diagnosis = models.CharField(max_length=100, blank=True, null=True)
	Temperature = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True)
	Blood_Pressure = models.CharField(max_length=100, blank=True, null=True)
	Pulse = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True)
	SPO2 = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(999)],null=True,blank=True,verbose_name = "SPO2 (%)")
	Date = models.DateField(auto_now_add=False, auto_now=False, null=True)

	def __str__(self):
		return "Patient followup case"