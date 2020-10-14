from django.shortcuts import render,redirect,HttpResponse
from myapp.models import Finalresults,Students,Aptitude,Technical,Listquestions,quizattempt
from django.contrib import messages
from random import sample
import datetime
import xlwt

def home(request):
    return render(request,'master.html')

def login(request):
    return render(request,'userlogin.html')

def userloginview(request):
    return render(request,'userlogin.html')

def signup(request):
    return render(request,'signuppage.html')

def aboutus(request):
    return render(request,'aboutus.html')

def forgot(request):
    return render(request,'forgot.html')

def userregister(request):
    name=request.POST['fname']
    username=request.POST['username']
    password=request.POST['password']
    phoneno=request.POST['iphone']
    gender=request.POST['gender']
    college=request.POST['college']
    branch=request.POST['branch']
    year=request.POST['year']
    div=request.POST['div']
    if Students.objects.filter(email_id=username).exists():
        messages.add_message(request,messages.ERROR,"Username Already Exist Login")
        return redirect('home')
    else:    
        Students(name=name,email_id=username,password=password,phone_no=phoneno,gender=gender,college=college,branch=branch,year=year,div=div,role='student').save()
        messages.add_message(request,messages.ERROR,"You Register Succesfully Login Now!")
        return redirect('userloginview')
    
def userauthentication(request):
    
    username=request.POST['username']
    password=request.POST['password'] 
    if Students.objects.filter(email_id=username).exists():
        a= Students.objects.get(email_id=username)
        if password==a.password:
            request.session['email']=a.email_id
            request.session['name']=a.name
            request.session['role']=a.role
            request.session['college']=a.college
            request.session['branch']=a.branch
            request.session['year']=a.year
            request.session['logged_in']=True
            
            if request.session['email']=="admin":
                return redirect('home')
            else:
                return redirect('userhome')
        else:
            messages.add_message(request,messages.ERROR,"Invalid Username or Password")
            return redirect('userloginview')
    else:
        messages.add_message(request,messages.ERROR,"Username Does Not Exist Need To Register First")
        return redirect('home')
            
    
def logoutuser(request):
    del request.session['name']
    del request.session['role']
    del request.session['college']
    del request.session['branch']
    del request.session['year']
    del request.session['email']
    request.session['logged_in']=False 
    messages.add_message(request,messages.ERROR,"Logout Successfully")
    return redirect('home') 
        
def forgotpass(request):
    username=request.POST['username']
    phoneno=request.POST['phone']  
    if Students.objects.filter(email_id=username).exists():
        a= Students.objects.get(email_id=username)
        if phoneno==a.phone_no:
            request.session['usernameid']=a.email_id
            return redirect("changepassview")
        else:
            messages.add_message(request,messages.ERROR,"Phone Number Didn't Match")
            return redirect("forgot")
    else:
        messages.add_message(request,messages.ERROR,"Username Does Not Exist Need To Register First")
        return redirect('home')
    
def changepassview(request):
    return render(request,"changepass.html")   

def changepass(request):
    s=Students.objects.get(email_id=request.session["usernameid"])
    s.password=request.POST['password']
    s.save()
    
    messages.add_message(request,messages.ERROR,"Password Change Succesfully! Login Now")
    return redirect("home") 

def userhome(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session['quizstart']==True:
            return redirect(quizquestions)
        else:
            user=Students.objects.get(email_id=request.session["email"])
            a=datetime.datetime.now() 
            request.session['strtime']=str(a)
            request.session['result'] = False
            return render(request,'userhome.html',{"user":user})

def userprofile(request):
    if(not request.session['logged_in']):
        return redirect(userloginview)
    else:
        user=Students.objects.get(email_id=request.session["email"])
        return render(request,"userprofile.html",{"user":user})  



def passstudentsview(request): 
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(home)
    else:
        return render(request,'passstudents.html')

def passstudentslist(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(home)
    else:
        return render(request,'passstudentslist.html')

def passstudents(request):  
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(home)
    else: 
        a=request.GET["college"]
        request.session['coll']=a
        coll=Finalresults.objects.filter(college=str(a))
        return render(request,'passstudentslist.html',{"coll":coll})

def result(request):
    if(not request.session['logged_in']):
        return redirect(userloginview)
    else:
        c=datetime.datetime.now() 
        request.session['endtime']=str(c)
        a=int(request.session['aptimarks'])
        total=(a)*2
        request.session['total']=total    
        Listquestions.objects.all().delete() 
        request.session['quizstart']=False
        request.session['result'] = True
        q=quizattempt()
        q.Name=request.session['name']
        q.Email=request.session['email']
        q.save()
        if total > 60:
            d=Students.objects.get(email_id=request.session["email"])
            a=Finalresults()
            a.sid=d.id
            a.name=d.name
            a.email=d.email_id
            a.year=d.year
            a.college=d.college
            a.branch=d.branch
            a.div=d.div
            a.strtime=request.session['strtime']
            a.endtime=request.session['endtime']
            a.marks=request.session['total'] 
            a.save()
            return render(request,'result.html')
        else:
            return render(request,'result.html')



def quizquestions(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if quizattempt.objects.filter(Name=request.session['name']).exists():
            messages.add_message(request,messages.ERROR,"Already Submitted Ur Test")
            return redirect('home')
        else:
            apti=Aptitude.objects.all()
            countapti=Aptitude.objects.all().count() 
            tech=Technical.objects.all()
            counttech=Technical.objects.all().count()
            if request.session['quizstart']!=True:
                print("hello")
                aptilist=sample(list(apti),countapti) 
                techlist=sample(list(tech),counttech)   
                request.session['quizstart']=True
                for i in aptilist:
                    q=Listquestions()
                    q.qid=i.id
                    q.Question=i.Question
                    q.optionA=i.optionA
                    q.optionB=i.optionB
                    q.optionC=i.optionC
                    q.optionD=i.optionD
                    q.correct=i.correct
                    q.qtype='apti'
                    q.save()
                for i in techlist:
                    q=Listquestions()
                    q.qid=i.id
                    q.Question=i.Question
                    q.optionA=i.optionA
                    q.optionB=i.optionB
                    q.optionC=i.optionC
                    q.optionD=i.optionD
                    q.correct=i.correct
                    q.qtype='tech'
                    q.save()  
                aptilist1=Listquestions.objects.filter(qtype="apti")
                techlist1=Listquestions.objects.filter(qtype="tech")      
                return render(request,'quizquestions.html',{"aptilist1":aptilist1,"techlist1":techlist1})    
            else:
                aptilist1=Listquestions.objects.filter(qtype="apti")
                techlist1=Listquestions.objects.filter(qtype="tech")
                return render(request,'quizquestions.html',{"aptilist1":aptilist1,"techlist1":techlist1})

def quizresult(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    else:
        if request.session.get('result'):
            del request.session['result']
            messages.add_message(request,messages.ERROR,"You Already Submited your Test")
            return redirect("home")
        else:
            print("hi")
            marks=0
            data = request.POST.items()
            
            for key,value in data:   
                print(key,value)     
                try:
                    question = Listquestions.objects.get(id=int(key))
                except:
                    pass
                else:
                    if(question.correct == value):
                        marks +=1
                
            request.session['aptimarks']=marks
            return redirect('result')
    
    

def download(request):
    if(not request.session['logged_in']):
        messages.add_message(request,messages.ERROR,"Need To Login First")
        return redirect(userloginview)
    elif("admin" not in request.session['role']):
        messages.add_message(request,messages.ERROR,"You Dont have Permission Access This Page")
        return redirect(home)
    else:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="QuizPassstudents.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Name','Email Address','Branch','Year','Div','Marks', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Finalresults.objects.filter(college=request.session['coll']).values_list('name', 'email', 'branch', 'year','div','marks')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response   