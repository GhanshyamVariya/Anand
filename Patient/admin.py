from django.contrib import admin
from Patient.models import Patient,PatientFollowUpCase,MainComplain
from django.forms import Textarea
from django.db import models


# Register your models here.
# class PatientInline(admin.StackedInline):
# 	formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows': 2,})}
#     }
# 	fieldsets = [
# 			('',
# 	         dict(fields=[
# 				(
# 				'Date',
# 				'Temperature',
# 				'Blood_Pressure',
# 				'Pulse',
# 				'SPO2',
# 	         	'Complain',
# 				'Treatment',
# 				'Treatment_Desciption',
# 				'Diagnosis',
# 				'Reference_Doctor',),
# 	         ],
# 	         )),
# 		]
# 	model = PatientFollowUpCase
# 	extra = 1
	
# 	def get_max_num(self, request, obj=None, **kwargs):
# 		max_num = 1
# 		return max_num	

class PatientHistoryInline(admin.TabularInline):
	model = PatientFollowUpCase
	extra = 1
	readonly_fields = (
				'Date',
				'Temperature',
				'Blood_Pressure',
				'Pulse',
				'SPO2',
	         	'Complain',
				'Treatment',
				'Treatment_Desciption',
				'Diagnosis',
				'Reference_Doctor',
		)

	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 50})}
	}

	def has_delete_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		else:
			return False

	def has_add_permission(self, request, obj=None):
		return False

class MainComplainAdmin(admin.ModelAdmin):
	fieldssets = [
		('Name',),
	]

	list_display = ('Name',)


class PatientAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})}
    }
	fieldsets = [
        ('Basic Info',
         dict(fields=[
             ('Name', 'Age','Birth_date', 'Gender','Blood_Group','Occupation',),
             ('Email_Id', 'Mobile','Address', ),
         ],
         )),
        ('Body Info',
         dict(fields=[
             ('Temperature','Blood_Pressure','Pulse','SPO2','DRUG_Allergy',),
         ],
         )),
        ('Complains Info',
         dict(fields=[
             ('Chief_Complains','Past_History','Treatment','Treatment_Desciption','Investigation','Reference_Doctor',),
         ],
         )),
        ('Important Date',
         dict(fields=[
             ('Date'),
         ],
         )),
    ]
	list_display = ('Name','Gender','Mobile','Date',)

	search_fields = ('Name','Mobile','Birth_date',)

	inlines = [PatientHistoryInline,]

	def save_model(self, request, obj, form, change):
		PatientFollowUpCase.objects.create(
			Patient = obj,
			Reference_Doctor = obj.Reference_Doctor,
			Complain = obj.Complain,
			Treatment = obj.Treatment,
			Treatment_Desciption = obj.Treatment_Desciption,
			Diagnosis = obj.Diagnosis,
			Temperature = obj.Temperature,
			Blood_Pressure = obj.Blood_Pressure,
			Pulse = obj.Pulse,
			SPO2 = obj.SPO2,
			Date = obj.Date,
		)
		obj.save()

admin.site.register(Patient,PatientAdmin)
admin.site.register(MainComplain,MainComplainAdmin)