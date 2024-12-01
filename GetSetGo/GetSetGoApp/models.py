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
     

class ServicesTable(models.Model):
    CLUBNAME = models.ForeignKey(ClubTable,on_delete=models.CASCADE, null=True, blank=True)
    servicename = models.CharField(max_length=30, null=True, blank=True)



class EventOrgainserTable(models.Model):
    LOGIN_ID=models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=30, null=True, blank=True)
    address=models.CharField(max_length=30, null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)
    email=models.CharField(max_length=30, null=True, blank=True)


class EventTable(models.Model):
    EVENTORGANISER = models.ForeignKey(EventOrgainserTable, on_delete=models.CASCADE)
    Event=models.CharField(max_length=30, null=True, blank=True)
    place=models.CharField(max_length=30, null=True, blank=True)
     
      
class ReportTable(models.Model):
    CLUBNAME = models.ForeignKey(ClubTable,on_delete=models.CASCADE, null=True, blank=True)
    Event=models.CharField(max_length=30, null=True, blank=True)
    winners=models.CharField(max_length=30, null=True, blank=True)
    income=models.IntegerField(null=True, blank=True)


class SchoolsTable(models.Model):
    Schoolname=models.CharField(max_length=30, null=True,blank=True)
    Address=models.CharField(max_length=30, null=True, blank=True)
    Phone=models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=30, null=True, blank=True)


class CollegeTable(models.Model):
    Collegename=models.CharField(max_length=30, null=True,blank=True)
    Address=models.CharField(max_length=30, null=True, blank=True)
    Phone=models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=30, null=True, blank=True)
 

class NotificationTable(models.Model):
    Notification=models.CharField(max_length=100, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True, null=True,blank=True)


class InstructionsTable(models.Model):
     Instruction=models.CharField(max_length=100, null=True,blank=True)
     created_at=models.DateTimeField(auto_now_add=True, null=True,blank=True)
     updated_at=models.DateTimeField(auto_now=True, null=True, blank=True)


class TeamsheetTable(models.Model):
      eventname=models.CharField(max_length=30, null=True,blank=True)
      teammembers=models.IntegerField(null=True,blank=True)
      discription=models.CharField(max_length=100, null=True,blank=True)
      rules=models.CharField(max_length=100, null=True, blank=True)
       

class UserTable(models.Model):
     name=models.CharField(max_length=30, null=True,blank=True)
     gender=models.CharField(max_length=30, null=True, blank=True)
     age=models.IntegerField(null=True,blank=True)
     Address=models.CharField(max_length=30, null=True, blank=True)
     Phone=models.IntegerField(null=True, blank=True)
     Email=models.CharField(max_length=30, null=True, blank=True)
 


class  MembersTable(models.Model):
       TEAMSHEET=models.ForeignKey(TeamsheetTable,on_delete=models.CASCADE, null=True, blank=True)
       USER=models.ForeignKey(UserTable,on_delete=models.CASCADE, null=True, blank=True)


class SponsorsTable(models.Model):
      Event = models.ForeignKey(ClubTable, on_delete=models.CASCADE,null=True, blank=True)
      sponsors=models.CharField(max_length=30, null=True, blank=True)




       

    





     
    



