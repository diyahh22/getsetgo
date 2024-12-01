
from django.urls import path

from .views import *

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('admindash', Admin.as_view(), name='admindash'),
    path('notification', Notification.as_view(), name='notification'),
    path('service', Serviceclub.as_view(), name="service"),
    path('booking', Booking.as_view(), name='booking'),
    path('club', Club.as_view(), name='club'),
    path('feedback', Feedback.as_view(),name='feedback'),
    path('instruction', Instruction.as_view(),name='instruction'),
    path('report', Report.as_view(),name='report'),
    path('teamsheet', Teamsheet.as_view, name='teamsheet'),
    path('event', Event.as_view(), name='event'),
    path('clubview', Clubviewevent.as_view(), name='clubview'),
    path('eventdash', Eventdashevent.as_view(), name='eventdash'),
    path('eventview', Eventviewevent.as_view(), name='eventview'),
    path('feedbackevent', Feedbackevent.as_view(), name='feedbackevent'),
    path('sponsers', Sponserevent.as_view(), name='sponserevent'),
    path('user',User.as_view(),name="user"),
    path('manageclub',Manageclub.as_view(),name="manageclub"),
    path('viewreport',ViewReport.as_view(),name='viewreport'),
    path('notificationview',NotificationClub.as_view(),name='notificationview'),
    path('contact',Contactev.as_view(),name='contact'),
    path('instructionsev',InstructionView.as_view(),name='instructionsev'),
    path('teamsheetev',Teamsheetev.as_view(),name='teamsheetev'),
    
]
