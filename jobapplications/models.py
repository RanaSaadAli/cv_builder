from django.db import models
from skills.models import Skill

# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('got_reply', 'Got Reply'),
        ('rejected', 'Rejected'),
        ('no_reply', 'No Reply')
    ]           

    job_description = models.TextField()
    company_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    date_applied = models.DateField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.company_name} - {self.job_description[:50]}"

class TailoredCV(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    tailored_cv = models.TextField()
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tailored_cv[:100]} - {self.is_submitted}"



class ReferralMessage(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    referral_msg = models.TextField()
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.referral_msg[:50]} - {self.is_used}"