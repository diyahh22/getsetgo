from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=30, null=True, blank=True)


class ClubTable(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    clubname = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField( max_length=30, null=True, blank=True)
    clubower = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
     

class Services(models.Model):
    CLUBNAME = models.ForeignKey(ClubTable,on_delete=models.CASCADE, null=True, blank=True)
    servicename = models.CharField(max_length=30, null=True, blank=True)



class EventOrgainser(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=30, null=True, blank=True)
    address=models.CharField(max_length=30, null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)
    email=models.CharField(max_length=30, null=True, blank=True)


class Event(models.Model):
    EVENTORGANISER = models.ForeignKey(EventOrgainser, on_delete=models.CASCADE)
    Event=models.CharField(max_length=30, null=True, blank=True)
    place=models.CharField(max_length=30, null=True, blank=True)
     
      
class Report(models.Model):
    CLUBNAME = models.ForeignKey(ClubTable,on_delete=models.CASCADE, null=True, blank=True)
    Event=models.CharField(max_length=30, null=True, blank=True)
    winners=models.CharField(max_length=30, null=True, blank=True)
    income=models.IntegerField(null=True, blank=True)
    



