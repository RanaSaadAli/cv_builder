from django.contrib import admin
from .models import JobApplication, TailoredCV, ReferralMessage

# Register your models here.
admin.site.register(JobApplication)
admin.site.register(TailoredCV)
admin.site.register(ReferralMessage)
