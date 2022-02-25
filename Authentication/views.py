import email
from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect
from Authentication.models import user_detail,providerdetails
# Create your views here.


def check_user(request):
    if request.method =="GET":
        un = request.GET["user_n"]
        check = User.objects.filter(email=un)

        if len(check)==1:
            return HttpResponse("Exists")
        else :
            return HttpResponse ("Not Exists")
        print (check,len(check))
        print (un)
    return HttpResponse("Hello")

def login(request):
    if request.method == 'POST':
        print ("in sign in post")
        un =  request.POST["name"]
        pass1 =  request.POST["password"]
        user= authenticate(username=un,password=pass1)
        if user is not None:
            return redirect("ClientHome")
            return render(request,"Client/index.html")
            return HttpResponseRedirect('/')
        else:
            return render(request,"Authentication/login.html",{'context':"Error in username or password"})

    return render(request,"Authentication/login.html")

def register(request):

    if request.method == 'POST':
        print ("in post")
        firtname=request.POST['firtname']
        midlename=request.POST['midlename']

        midlename1=request.POST['midlename']

        lastname=request.POST['lastname']
        suffix=request.POST['suffix']
        email=request.POST['email']
        password=request.POST['password']
        snn_number=request.POST['snn_number']
        dob=request.POST['dob']
        phone_h=request.POST['phone_h']
        phone_w=request.POST['phone_w']
        phone_M=request.POST['phone_M']
        fax=request.POST['fax']
        mail_address=request.POST['mail_address']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        country=request.POST['country']
        
        p_detail=request.POST['provider']
        print (p_detail)
        if p_detail == "1":
            username=request.POST['user_A']
            password2=request.POST['password_A']
            security_num=request.POST['security_num_A']
            num=request.POST['num_A']
            note=request.POST['note_A']
            print (username)
            print (password2)
            print (security_num)
            print ("in 1")
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="Identity IQ",username=username,password2=password2,num=num,note=note)
            provider.save()
        
        elif p_detail=="2":
            print ("in 2")
            username=request.POST['user_B']
            password2=request.POST['password_B']
            security_num=request.POST['security_num_B']
            num=request.POST['num_B']
            note=request.POST['note_B']
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="Smart Credit",username=username,password2=password2,num=num,note=note)
            provider.save()
        elif p_detail=="3":
            print ("in 3")
            
            username=request.POST['user_C']
            password2=request.POST['password_C']
            security_num=request.POST['security_num_C']
            num=request.POST['num_C']
            note=request.POST['note_C']
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="MyFreeScoreNow",username=username,password2=password2,num=num,note=note)
            provider.save()
        elif p_detail=="4":
            username=request.POST['user_D']
            password2=request.POST['password_D']
            security_num=request.POST['security_num_D']
            num=request.POST['num_D']
            note=request.POST['note_D']
            print("in 4")
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="MyScoreIQ",username=username,password2=password2,num=num,note=note)
            provider.save()
        elif p_detail=="5":
            username=request.POST['user_E']
            password2=request.POST['password_E']
            security_num=request.POST['security_num_E']
            num=request.POST['num_E']
            note=request.POST['note_E']
            print("in 5")
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="PrivacyGuard",username=username,password2=password2,num=num,note=note)
            provider.save()
        elif p_detail=="6":
            username=request.POST['user_F']
            password2=request.POST['password_F']
            security_num=request.POST['security_num_F']
            num=request.POST['num_F']
            note=request.POST['note_F']
            print("in 6")
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="IdentityClub",username=username,password2=password2,num=num,note=note)
            provider.save()
        elif p_detail=="7":
            username=request.POST['user_G']
            password2=request.POST['password_G']
            security_num=request.POST['security_num_G']
            num=request.POST['num_G']
            note=request.POST['note_G']
            print("in 7")
            print (username)
            print (password2)
            print (security_num)
            
            # user created
            usr = User.objects.create_user(email,email,password)
            usr.first_name = firtname
            usr.last_name =lastname
            usr.save()
            # print (request.POST)
            
            #additional detail
            detail = user_detail(user=usr,midelname=midlename,suffix=suffix,last_snn=snn_number,dob=dob,phone_h=phone_h,phone_w=phone_w,phone_m=phone_M,fax=fax,mail_address=mail_address,city=city,state=state,zipcode=zip_code)
            detail.save()

            
            #provider detail
            provider = providerdetails(user=usr,p_detail="SampleReport",username=username,password2=password2,num=num,note=note)
            provider.save()





        
        # print (firtname)
        # print (country)

        # user = user_detail.objects.create(firstname=firtname,last_snn=snn_number,dob=dob)
        # user.save()
        # print (fname)


    return render(request,"Authentication/register.html")