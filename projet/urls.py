
from django.contrib import admin

from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from tikets import views

router = DefaultRouter()
router.register('guests', views.viewset_guest),
router.register('movie', views.viewset_movie),
router.register('res', views.viewset_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('djangojsonresponsenomodel/', views.no_rest_no_model ),

    #2
    
    path('djangojsonresponsefrommodel/', views.no_rest_from_model ),

    #

    path('rest/fvb/', views.FBV_List),

    path('rest/fvbmovi/', views.FBV_ListMO),
    
    path('rest/res/', views.FBV_Listre),

    path('rest/movcl/<int:pk>', views.movcl_pk.as_view()),

    path('rest/movcl/', views.mov_clas.as_view()),

    path('rest/rescl/', views.res.as_view()),

    path('rest/rescl/<int:pk>/', views.rescl_pk.as_view()),

    path('rest/res/<int:pk>', views.FBre_pk),

    path('rest/fvbk/<int:pk>/', views.FBV_pk),

    #find movie

     path('findmov/', views.find_movie),

     #new reservation

     path('newres/', views.new_reservation),

     path('rest/fvbmovi/<int:pk>/', views.FBmov_pk),


    path('rest/getpo/', views.CBV_LIST.as_view()),

    path('rest/getpo/<int:pk>/', views.CBV_pk.as_view()),
    
    path('rest/mixins/', views.mixins_list.as_view()),

    path('rest/mixins/<int:pk>/', views.mixins_pk.as_view()),

    path('rest/generic/', views.generic_list.as_view()),

    path('rest/generic/<int:pk>/', views.generic_pk.as_view()),

    path('rest/viewset/', include(router.urls) ),

    path('api-auth/', include('rest_framework.urls')),

    #token

     path('api-token-auth/', obtain_auth_token),


]