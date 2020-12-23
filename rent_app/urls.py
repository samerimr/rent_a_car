from django.urls import path     
from . import views

urlpatterns = [
            path('', views.root),
            # path('register', views.register),   
            # path('welcome/<int:id>',views.welcome),
            # path('login',views.login),
            # path('logout', views.car), 
            # path('about+_us',views.about_us),
            # path('add_car/<int:id>', views.add_car),
            # path('rent/<int:user_id>/<int:car_id>',views.likecar),
            # path('remove_from_rent/<int:user_id>/<int:care_id>',views.unrentcar),
            # path('View_car/<int:user_id>/<int:car_id>',views.info),
            # path('update_car/<int:user_id>/<int:car_id>',views.update),
            # # path('delete/<int:user_id>/<int:car_id>',views.delete)
        ]   