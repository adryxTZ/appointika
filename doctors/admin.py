from django.contrib import admin

from doctors.models import DoctorProfile


class DoctorProfiles(admin.ModelAdmin):
    list_display = ['id', "user", "specialization", 'experience', 'available_days']


#
#
admin.site.register(DoctorProfile, DoctorProfiles)
