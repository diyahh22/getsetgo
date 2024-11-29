from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request, 'Login.html')
    
class Signup(View):
    def get(self,request):
        return render(request, 'Signup.html' )
    

class Admin(View):
    def get(self,request):
        return render(request, 'admin/admindash.html')
    
class Notification(View):
    def get(self,request):
        return render(request, 'admin/sent_notification.html')   
    
class Service(View):
    def get(self,request):
        return render(request, 'admin/verifyclubs_service.html')    
    
class Activities(View):
    def get(self,request):
        return render(request, 'admin/viewActivities.html')   

class User(View):
    def get(self,request):
        return render(request, 'admin/viewUser.html')    

class Club(View):
    def get(self,request):
        return render(request, 'Club/clubDash.html')    
    
class Booking(View):
    def get(self,request):
        return render(request, 'Club/Booking.html')     
    
class Feedback(View):
    def get(self,request):
        return render(request, 'Club/feedbackView.html') 

class Instruction(View):
    def get(self,request):
        return render(request, 'Club/instructions_view.html')  

class Report(View):
    def get(self,request):
        return render(request, 'Club/report_view.html') 

class Serviceclub(View):
    def get(self,request):
        return render(request, 'Club/servicesView.html')        
    
class Teamsheet(View):
    def get(self,request):
        return render(request, 'Club/vieTeamSheet.html')        

class Event(View):
    def get(self,request):
        return render(request, 'Club/ViewEvents.html')   

class Clubviewevent(View):
    def get(self,request):
        return render(request, 'Events/Clubsview.html')   

class Eventdashevent(View):
    def get(self,request):
        return render(request, 'Events/EventDash.html')  

class Eventviewevent(View):
    def get(self,request):
        return render(request, 'Events/Events_view.html')   

class Feedbackevent(View):
    def get(self,request):
        return render(request, 'Events/feedback.html')   
        
class Sponserevent(View):
    def get(self,request):
        return render(request, 'Events/Sponsers_view.html')   





        
        
    

    
    
    