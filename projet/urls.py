
from django.contrib import admin

from django.urls import  path, include
from rest_framework.routers import DefaultRouter

from tikets import views

router = DefaultRouter()
router.register('guests', views.viewset_guest)

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

     path('rest/fvbmovi/<int:pk>/', views.FBmov_pk),


    path('rest/getpo/', views.CBV_LIST.as_view()),

    path('rest/getpo/<int:pk>/', views.CBV_pk.as_view()),
    
    path('rest/mixins/', views.mixins_list.as_view()),

    path('rest/mixins/<int:pk>/', views.mixins_pk.as_view()),

    path('rest/generic/', views.generic_list.as_view()),

    path('rest/generic/<int:pk>/', views.generic_pk.as_view()),

    path('rest/viewset/', include(router.urls) )

]
