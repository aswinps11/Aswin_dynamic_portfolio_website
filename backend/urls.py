from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard),
    path('homecontent/', views.homecontent, name='homecontent'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
    path('contact/', views.contact, name='contact'),
    path('contacts/delete/<int:id>/', views.delete_contact_message, name='delete_contact'),
]