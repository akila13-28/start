from django.urls import path
from . import views
urlpatterns =[
    path('',views.card,name='card'),
    path('doreamon',views.host,name='doreamon'),
    path('choice/',views.choice,name='choice'),
    path('optimisation/',views.optimisation,name='optimisation'),
    path('empowerment/',views.empowerment,name='empowerment'),
    path('persuasion/',views.persuasion,name='persuasion'),
    path('interaction/',views.interaction,name='interaction'),
    path('socialconversation/',views.social_conversation,name='socialconversation'),
    
    
    
]