from django.urls import path

from .views import(
    home_view,
    contact_view,
    who_are_we_view,
    search_view,
    register_view,
    logout_view,
    account_view,
    TestingView,
    TestingTemplateView,
    LoginView,
    QuestionsCreateView,
    QuestionsList,
    QuestionsDetail,
    QuestionsUpdateView,
    QuestionsDeleteView,
    AccountCreateView,

)

app_name= 'information'
urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),   
    path('who_are_we/', who_are_we_view, name='whoarewe'),   
    path('search/', search_view, name='search'),   
    path('register/', register_view, name='register'),   
    path('login/form_view/', LoginView.as_view(), name='loginform'),   
    path('logout/', logout_view, name='logout'), 
    path('new_account/', AccountCreateView.as_view(), name='newaccount'),     
    path('create_account/', account_view, name='account'),   
    path('testing/', TestingView.as_view(), name='testing'),   
    path('templateview/', TestingTemplateView.as_view(), name='testingtemplateview'), 
    path('questions/', QuestionsList.as_view(), name='questionlist'),     
    path('questions/new_question/', QuestionsCreateView.as_view(), name='newquestion'),   
    path('questions/question_detail/<pk>/', QuestionsDetail.as_view(), name='questiondetails'),   
    path('questions/update_question/<pk>/', QuestionsUpdateView.as_view(), name='updatequestion'),   
    path('questions/delete_question/<pk>/', QuestionsDeleteView.as_view(), name='deletequestion'),   

]
