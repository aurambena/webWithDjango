from django.urls import path

from .views import(
    home_view,
    contact_view,
    who_are_we_view,
    search_view,
    register_view,
    login_view,
    logout_view,
    account_view,
)

app_name= 'information'
urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),   
    path('who_are_we/', who_are_we_view, name='whoarewe'),   
    path('search/', search_view, name='search'),   
    path('register/', register_view, name='register'),   
    path('login/', login_view, name='login'),   
    path('logout/', logout_view, name='logout'),   
    path('create_account/', account_view, name='account'),   


]
