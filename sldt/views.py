from django.shortcuts import render,redirect
from .models import Bill
from django.contrib import messages
from django.contrib.auth.models import User, auth


from django.http import HttpResponse

def home(request):
    return render(request,'home.htm')

def update(request):
    if request.user.is_authenticated:
        return render(request,'update.html')
    else:
        messages.info(request,'Please login')
        return redirect('login')

def add(request):
    if request.user.is_authenticated:
        return render(request,'add.html')
    else:
        messages.info(request,'Please login')
        return redirect('login')

def stat(request):
    if request.user.is_authenticated:
        return render(request,'stat.html')
    else:
        messages.info(request,'Please login')
        return redirect('login')
    
def st(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('date') and request.POST.get('paid'):
            s1=request.POST.get('name')
            s2=request.POST.get('date')
            Bill.objects.filter(name=s1).filter(date=s2).update(paid=request.POST.get('paid'))
            
            messages.info(request,'Paid amount updated')
            return redirect('add')
                
        else:
            messages.info(request,'plase check the name and date in stat')
            return redirect('stat')
def sta(request):
    if request.method=='POST':
        if request.POST.get('date') and request.POST.get('date1'):
            s1=request.POST.get('date')
            s2=request.POST.get('date1')
            a= Bill.objects.filter(date__gte=s1, date__lte=s2)
            
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('contact')
                
            else:
                return render(request,'sta.html',{'a':a})

def Login(request):
    return render(request,'login.html')

def updates(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('date'):
            s1=request.POST.get('name')
            s2=request.POST.get('date')
            b=str(s2)
            a= Bill.objects.filter(name=s1).filter(date=s2)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('contact')
                
            else:
                return render(request,'dis1.html',{'a':a,'b':b})

def bill(request):
    return render(request,'bill.htm')

def data(request):
    return render(request,'Contact.htm')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('Login')

    else:
        return redirect('Login')



def logout(request):
    auth.logout(request)
    return redirect('/')     
      
def dis(request):
    return render(request,'dis.html')

def services(request):
    return render(request,'Services.htm')
    
def cont(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('date'):
            s1=request.POST.get('name')
            s2=request.POST.get('date')
            b=str(s2)
            a= Bill.objects.filter(name=s1).filter(date=s2)
            if not a:
                messages.info(request,'Data Not Available')
                return redirect('contact')
                
            else:
                return render(request,'dis.html',{'a':a,'b':b})
    

def bll(request):
    if request.method =='POST':
        if request.POST.get('name') and request.POST.get('date'):
            b=Bill()
            b.name=request.POST.get('name')
            b.date=request.POST.get('date')
            b.t1=request.POST.get('t1')
            b.t2=request.POST.get('t2')
            b.t3=request.POST.get('t3')
            b.t4=request.POST.get('t4')
            b.t5=request.POST.get('t5')
            b.t6=request.POST.get('t6')
            b.t7=request.POST.get('t7')
            b.t8=request.POST.get('t8')
            b.t9=request.POST.get('t9')
            b.t10=request.POST.get('t10')
            b.t11=request.POST.get('t11')
            b.t12=request.POST.get('t12')
            b.t13=request.POST.get('t13')
            b.t14=request.POST.get('t14')
            b.t15=request.POST.get('t15')
            b.t16=request.POST.get('t16')
            b.t17=request.POST.get('t17')
            b.t18=request.POST.get('t18')
            b.t19=request.POST.get('t19')
            b.t20=request.POST.get('t20')
            b.t21=request.POST.get('t21')
            b.t22=request.POST.get('t22')
            b.t23=request.POST.get('t23')
            b.t24=request.POST.get('t24')
            b.t25=request.POST.get('t25')
            b.t26=request.POST.get('t26')
            b.t27=request.POST.get('t27')
            b.t28=request.POST.get('t28')
            b.t29=request.POST.get('t29')
            b.t30=request.POST.get('t30')
            b.t31=request.POST.get('t31')
            b.t32=request.POST.get('t32')
            b.t33=request.POST.get('t33')
            b.t34=request.POST.get('t34')
            b.t35=request.POST.get('t35')
            b.t36=request.POST.get('t36')
            b.t37=request.POST.get('t37')
            b.t38=request.POST.get('t38')
            b.t39=request.POST.get('t39')
            b.t40=request.POST.get('t40')
            b.t41=request.POST.get('t41')
            b.t42=request.POST.get('t42')
            b.t43=request.POST.get('t43')
            b.t44=request.POST.get('t44')
            b.t45=request.POST.get('t45')
            b.t46=request.POST.get('t46')
            b.t47=request.POST.get('t47')
            b.t48=request.POST.get('t48')
            b.t49=request.POST.get('t49')
            b.t50=request.POST.get('t50')
            b.t51=request.POST.get('t51')
            b.t52=request.POST.get('t52')
            b.t53=request.POST.get('t53')
            b.t54=request.POST.get('t54')
            b.t55=request.POST.get('t55')
            b.t56=request.POST.get('t56')
            b.t57=request.POST.get('t57')
            b.t58=request.POST.get('t58')
            b.t59=request.POST.get('t59')
            b.t60=request.POST.get('t60')
            b.t61=request.POST.get('t61')
            b.t62=request.POST.get('t62')
            b.t63=request.POST.get('t63')
            b.t64=request.POST.get('t64')
            b.t65=request.POST.get('t65')
            b.t66=request.POST.get('t66')
            b.t67=request.POST.get('t67')
            b.t68=request.POST.get('t68')
            b.t69=request.POST.get('t69')
            b.t70=request.POST.get('t70')
            b.t71=request.POST.get('t71')
            b.t72=request.POST.get('t72')
            b.t73=request.POST.get('t73')
            b.t74=request.POST.get('t74')
            b.t75=request.POST.get('t75')
            b.t76=request.POST.get('t76')
            b.total=request.POST.get('total')
            b.paid=0
            b.save()
            messages.info(request,'Data added')
            return redirect('contact')
        else:
            return redirect('bill') 

def bll1(request):
    if request.method =='POST':
        if request.POST.get('name') and request.POST.get('date'):
            s1=request.POST.get('name')
            s2=request.POST.get('date')
            Bill.objects.filter(name=s1).filter(date=s2).update(
            date=request.POST.get('date'),
            t1=request.POST.get('t1'),
            t2=request.POST.get('t2'),
            t3=request.POST.get('t3'),
            t4=request.POST.get('t4'),
            t5=request.POST.get('t5'),
            t6=request.POST.get('t6'),
            t7=request.POST.get('t7'),
            t8=request.POST.get('t8'),
            t9=request.POST.get('t9'),
            t10=request.POST.get('t10'),
            t11=request.POST.get('t11'),
            t12=request.POST.get('t12'),
            t13=request.POST.get('t13'),
            t14=request.POST.get('t14'),
            t15=request.POST.get('t15'),
            t16=request.POST.get('t16'),
            t17=request.POST.get('t17'),
            t18=request.POST.get('t18'),
            t19=request.POST.get('t19'),
            t20=request.POST.get('t20'),
            t21=request.POST.get('t21'),
            t22=request.POST.get('t22'),
            t23=request.POST.get('t23'),
            t24=request.POST.get('t24'),
            t25=request.POST.get('t25'),
            t26=request.POST.get('t26'),
            t27=request.POST.get('t27'),
            t28=request.POST.get('t28'),
            t29=request.POST.get('t29'),
            t30=request.POST.get('t30'),
            t31=request.POST.get('t31'),
            t32=request.POST.get('t32'),
            t33=request.POST.get('t33'),
            t34=request.POST.get('t34'),
            t35=request.POST.get('t35'),
            t36=request.POST.get('t36'),
            t37=request.POST.get('t37'),
            t38=request.POST.get('t38'),
            t39=request.POST.get('t39'),
            t40=request.POST.get('t40'),
            t41=request.POST.get('t41'),
            t42=request.POST.get('t42'),
            t43=request.POST.get('t43'),
            t44=request.POST.get('t44'),
            t45=request.POST.get('t45'),
            t46=request.POST.get('t46'),
            t47=request.POST.get('t47'),
            t48=request.POST.get('t48'),
            t49=request.POST.get('t49'),
            t50=request.POST.get('t50'),
            t51=request.POST.get('t51'),
            t52=request.POST.get('t52'),
            t53=request.POST.get('t53'),
            t54=request.POST.get('t54'),
            t55=request.POST.get('t55'),
            t56=request.POST.get('t56'),
            t57=request.POST.get('t57'),
            t58=request.POST.get('t58'),
            t59=request.POST.get('t59'),
            t60=request.POST.get('t60'),
            t61=request.POST.get('t61'),
            t62=request.POST.get('t62'),
            t63=request.POST.get('t63'),
            t64=request.POST.get('t64'),
            t65=request.POST.get('t65'),
            t66=request.POST.get('t66'),
            t67=request.POST.get('t67'),
            t68=request.POST.get('t68'),
            t69=request.POST.get('t69'),
            t70=request.POST.get('t70'),
            t71=request.POST.get('t71'),
            t72=request.POST.get('t72'),
            t73=request.POST.get('t73'),
            t74=request.POST.get('t74'),
            t75=request.POST.get('t75'),
            t76=request.POST.get('t76'),
            total=request.POST.get('total'))
            
            messages.info(request,'Data updated')
            return redirect('contact')
        else:
            return redirect('bill')   