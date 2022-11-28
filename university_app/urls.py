from rest_framework import routers
from django.urls import path,include
from .viewsets import *
from .views import *
"""
for viewsets
router=routers.DefaultRouter()
router.register(r'Students',studentViewset) #r to take only anti-sla student\5 dont take it as \n
router.register(r'Groups',groupViewset)
router.register(r'Address',addressViewset)

urlpatterns=[
    path('',include(router.urls))
]
"""
#for views
urlpatterns = [
    path(r'all/',get_all_students),
    path(r'add/',add_student),
    path(r'delete/',delete_student),
]
