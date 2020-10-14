
from django.urls import path
from .views import passstudentslist,download,quizresult,quizquestions,result,passstudents,passstudentsview,userprofile,userhome,changepass,changepassview,forgotpass,logoutuser,userauthentication,userregister,home,login,userloginview,signup,aboutus,forgot

urlpatterns = [
    path('',home,name='home'),
    path('login/',login),
    path('userloginview/',userloginview,name='userloginview'),
    path('userregister/',userregister,name='userregister'),
    path('signuppage/',signup),
    path('aboutus/',aboutus),
    path('forgot/',forgot,name='forgot'),
    path('userauthentication/',userauthentication),
    path('logoutuser/',logoutuser),
    path('forgotpass/',forgotpass,name='forgotpass'),
    path('changepassview/',changepassview,name='changepassview'),
    path('changepass/',changepass),
    path('userhome/',userhome,name='userhome'),
    path('userprofile/',userprofile),

    path('result/',result,name="result"),
    path('passstudentsview/',passstudentsview,name='passstudents'),
    path('passstudents/',passstudents,name='pass'),
    path('quizquestions/',quizquestions,name='quizquestions'),
    path('quizresult/',quizresult),
    path('passstudentslist/',passstudentslist),
    path('download/',download)

]
