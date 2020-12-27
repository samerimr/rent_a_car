from django.urls import path     
from . import views

urlpatterns = [
            path('', views.index),
            path('registration', views.registration),
            path('register', views.register), 
            path('success', views.success),    
            path('login',views.login),
            path('logout',views.logout),
            path('add_car',views.add_car),
            path('car_list',views.car_list),
            path('car_list/<car_id>',views.car_details),
            path('contact_us',views.contact_us),
            path('about_us',views.about_us),
            path('book/<car_id>',views.book),



            # path('logout', views.car), 
            # path('about+_us',views.about_us),
            # path('add_car/<int:id>', views.add_car),
            # path('rent/<int:user_id>/<int:car_id>',views.likecar),
            # path('remove_from_rent/<int:user_id>/<int:care_id>',views.unrentcar),
            # path('View_car/<int:user_id>/<int:car_id>',views.info),
            # path('update_car/<int:user_id>/<int:car_id>',views.update),
            # # path('delete/<int:user_id>/<int:car_id>',views.delete)
            # path('welcome/<int:id>',views.welcome),
        ]   