
from django.contrib import admin
from django.urls import path

from tikets import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('djangojsonresponsenomodel/', views.no_rest_no_model ),

    #2
    
    path('djangojsonresponsefrommodel/', views.no_rest_from_model ),

    #

    path('rest/fvb/', views.FBV_List),

    path('rest/fvbk/<int:pk>/', views.FBV_pk)


]
