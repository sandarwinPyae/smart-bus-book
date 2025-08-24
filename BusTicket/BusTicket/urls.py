"""
URL configuration for BusTicket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path

from django.urls import path,re_path,include
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about-us/',views.about_us,name='about_us'),
    path('search/',views.search_routes, name='search_routes'),
    path('select-trip/<int:schedule_id>/', views.seat_selection, name='select_trip'),
    path('select-seats/<int:schedule_id>/submit/', views.submit_seats, name='submit_seats'),
    # payment and booking by LLS
    # URL to handle the payment form submission
    # path('process-payment/<int:schedule_id>/',views.process_payment,name='process_payment'),
    # URL pattern for the booking confirmation page
    # path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),

    # path('bookings/',views.bookings,name='bookings'),
    path('profile_page/',views.profile_page,name='profile_page'),
    # path('seebookings/<int:booking_id>/',views.seebookings,name='seebookings'),
    re_path(r'^seebookings/(?P<booking_id>\d+)?/?$', views.seebookings, name='seebookings'),

    # payment and booking process by sdwp
    path('process-payment/<int:user_id>/', views.process_payment, name='process_payment'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('feedback/',views.feedback,name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),


    # sdwp
    path('register/',views.user_registration,name='register'),
    path('accounts/login/',views.user_login,name='login'),
    path('login-home/',views.logined_user_home,name='logined_user'),
    path('accounts/logout/', views.logout_view, name="logout"),

    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('send_password_reset_email/', views.send_password_reset_email, name='send_password_reset_email'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('contactus/',views.contact_us, name='contact_us'),

    # admin url call
    path('admindashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admindashboard/user_home/',views.user_home,name='user_home'),
    path('admindashboard/user_home/<int:user_id>/delete/', views.soft_delete_user, name='soft_delete_user'),
    path('admindashboard/operator_home/',views.operator_home,name='operator_home'),
    path('admindashboard/operator_home/add_new_operator/',views.add_operator,name='operator_add'),
    path('admindashboard/operator_home/<int:operator_id>/update/',views.update_operator,name='operator_update'),
    path('admindashboard/operator_home/<int:operator_id>/delete/',views.delete_operator,name='operator_delete'),
    path('admindashboard/route_home/',views.route_home,name='route_home'),
    path('admindashboard/route_home/add_new_route/',views.add_route,name='route_add'),
    path('admindashboard/route_home/<int:route_id>/update/',views.update_route,name='route_update'),
    path('admindashboard/route_home/<int:route_id>/delete/',views.delete_route,name='route_delete'),
    path('admindashboard/bus_home/',views.bus_home,name='bus_home'),
    path('admindashboard/bus_home/add_new_bus/',views.add_bus,name='bus_add'),
    path('admindashboard/bus_home/<int:bus_id>/update/',views.update_bus,name='bus_update'),
    path('admindashboard/bus_home/<int:bus_id>/delete/',views.delete_bus,name='bus_delete'),
    path('admindashboard/schedule_home/',views.schedule_home,name='schedule_home'),
    path('admindashboard/schedule_home/add_new_schedule/',views.add_schedule,name='schedule_add'),
    path('admindashboard/schedule_home/<int:schedule_id>/update/',views.update_schedule,name='schedule_update'),
    path('admindashboard/schedule_home/<int:schedule_id>/delete/',views.delete_schedule,name='schedule_delete'),

    path('admindashboard/bookings/', views.booking_list, name='booking_list'),
    # path('admindashboard/bookings/create/', views.booking_create, name='booking_create'),
    path('admindashboard/history/', views.history_list, name="history"),
    path('admindashboard/feedback/', views.feedback_list,name='feedback_list'),
    path('admindashboard/feedback_detail/<int:feedback_id>/',views.feedback_detail,name='feedback_detail'),
    path('admindashboard/q_a/',views.question_answer_list,name='question_answer_list'),
    path('admindashboard/q_a/add/',views.add_qa,name='qa_add'),
    path('admindashboard/q_a/<int:qa_id>/update/',views.update_qa,name='qa_update'),
    path('admindashboard/q_a/<int:qa_id>/delete/',views.delete_qa,name='qa_delete'),
]
