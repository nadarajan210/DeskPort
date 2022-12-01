from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import departments,tickets,fields,knowledgebases,roless,staffss,nuserss,dashinput
# Create your views here.
def index(request):
    return render(request , "index.html")

def dashboard(request):
    D = dashinput()
    D.dusers = len(nuserss.objects.all())
    D.dstaffs  = len(staffss.objects.all())
    D.ddepartments = len(departments.objects.all())
    D.dknws = len(knowledgebases.objects.all())
    D.dsatisfied = len(nuserss.objects.all())
    D.dtickets = len(tickets.objects.all())
    op = 0
    close = 0
    atickets = tickets.objects.all()
    for aticket in atickets:
        if aticket.status:
            close += 1
        else:
            op += 1 
    D.dotickets = op
    D.dctickets = close           

    tkets = tickets.objects.all()
    return render(request,'dashboard.html',{'tickets':tkets , 'D':D})  

def AllTickets(request):
    tkets = tickets.objects.all()
    return render(request,'AllTickets.html', {'tickets':tkets})

def open1(request):
    tkets = tickets.objects.all()
    return render(request,'open.html',{'tickets':tkets})

def close(request):
    tkets = tickets.objects.all()
    return render(request,'closedt.html',{'tickets':tkets})    

def addtickets(request):
    depts = departments.objects.all()
    return render(request,'addtickets.html' , {'depts':depts})

def department(request):
    depts = departments.objects.all()

    return render(request,'department.html', {'depts':depts}) 


def customfield(request):
    cfields = fields.objects.all()
    return render(request,"custom field.html",{'fields':cfields})    

def knowledgebase(request):
    knws = knowledgebases.objects.all()
    return render(request,"knowledgebase.html" ,{'knws':knws})    

def staffs(request):
    nstaff = staffss.objects.all()
    return render(request,"staffs.html" , {'staffs':nstaff})  

def  users(request):
    vusers = nuserss.objects.all()
    return render(request,"users.html" ,{'vusers':vusers})     

def roles(request):
    vroles = roless.objects.all()
    return render(request,"roles.html" , {'vroles':vroles})   

def nknowledgebase(request):
    depts = departments.objects.all()
    return render(request,"newknowledgebase.html" , {'depts':depts}) 

def nstaffs(request):
    depts = departments.objects.all()
    vroles = roless.objects.all()
    return render(request,"newstaffs.html" , {'depts':depts  , 'roles':vroles})  

def nusers(request):
    return render(request,"newUsers.html")   

def nroles(request):
    return render(request,"newroles.html")

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        dept_num = request.POST['dept_num']
        dept = departments(title=title , desc=desc , dept_num=dept_num)
        dept.save()
        return redirect('department')
    else:
        return render(request, "department.html")        

def editdept(request,id):
    edept = departments.objects.get(id=id)
    return render(request, "editdept.html",{'edept':edept})


def updatedept(request,id):
    if request.method == 'POST':
        udept = departments.objects.get(id=id)
        udept.delete()
        udept = departments(title=request.POST['title'],desc=request.POST['desc'], dept_num=request.POST['dept_num'])
        udept.save()
        return redirect('department')
    else:
        udept = departments.objects.get(id=id)
        return render(request , "editdept.html",{'edept':udept})  

def  deletedept(request,id):
    ddept = departments.objects.get(id=id)
    ddept.delete()
    return redirect('department') 

def newticket(request,username):
    if request.method == 'POST':
        problemtitle = request.POST['problemtitle']
        priority = request.POST['priority']
        dept = request.POST['department']
        msg = request.POST['msg']
        website = request.POST['website']
        products = request.POST['products']
        file = request.POST['file']
        Idnum = request.POST['Idnum']
        ticket = tickets(problemtitle=problemtitle , priority=priority , dept=dept , msg=msg ,website=website , products=products , file=file , Idnum=Idnum , username=username)
        ticket.save()
        return redirect('AllTickets')

    else:
        return redirect('addtickets')  


def rticket(request,id):
    reticket = tickets.objects.get(id=id)
    return render(request,"rticket.html",{'reticket':reticket})

def updatetic(request,id):
    if request.method == 'POST':
        rply = tickets.objects.get(id=id)     
        rply.reply = request.POST['reply']
        rply.save()
        return redirect('AllTickets')
    else:
        return redirect('rticket') 

def closeticket(request,id):
    closetic = tickets.objects.get(id=id)
    closetic.status = True
    closetic.save()
    return redirect('AllTickets')   

def reopentic(request,id):
    reoticket = tickets.objects.get(id=id)
    reoticket.status = False
    reoticket.save()
    return render(request , "reopentic.html" , {'reoticket':reoticket})

def nfield(request):
    if request.method == 'POST':
        field_name = request.POST['field_name']
        field_type = request.POST['field_type']
        placeholder = request.POST['placeholder']
        field_length = request.POST['field_length']
        field_required = request.POST['field_required']
        field_status = request.POST['field_status'] 
        field = fields(field_name=field_name , field_type=field_type , placeholder=placeholder , field_length=field_length , field_required=field_required , field_status=field_status)  
        field.save()
        return redirect('customfield')
    else:
        return redirect('customfield')

def editfield(request,id):
    efield = fields.objects.get(id=id)
    return render(request,"editfield.html",{'efield':efield})

def updatefield(request,id):
    if request.method == 'POST':
        ufield = fields.objects.get(id=id)
        ufield.delete()
        field_name = request.POST['field_name']
        field_type = request.POST['field_type']
        placeholder = request.POST['placeholder']
        field_length = request.POST['field_length']
        field_required = request.POST['field_required']
        field_status = request.POST['field_status'] 
        ufield = fields(field_name=field_name , field_type=field_type , placeholder=placeholder , field_length=field_length , field_required=field_required , field_status=field_status)  
        ufield.save()
        return redirect('customfield')
    else:
        efield = fields.objects.get(id=id)
        return render(request,"editfield.html",{'efield':efield})


def delfield(request,id):
    dfield = fields.objects.get(id=id)
    dfield.delete()
    return redirect('customfield') 
 
 
def addknw(request,username):
    if request.method == 'POST':
        dept = request.POST['dept']
        title = request.POST['title']  
        desc = request.POST['desc']  
        status = request.POST['status']
        know = knowledgebases(dept=dept , title=title , desc=desc , status=status , username=username)
        know.save()
        return redirect('knowledgebase')
    else:
        return redirect('knowledgebase') 

def editknw(request,id):
    eknw = knowledgebases.objects.get(id=id)
    depts = departments.objects.all() 
    return render(request,"editknw.html" , {'eknw':eknw , 'depts':depts})           


def updateknw(request,id,username):
    if request.method == 'POST':
        uknw = knowledgebases.objects.get(id=id)
        uknw.delete()
        dept = request.POST['dept']
        title = request.POST['title']  
        desc = request.POST['desc']  
        status = request.POST['status']
        uknw = knowledgebases(dept=dept , title=title , desc=desc , status=status , username=username)
        uknw.save()
        return redirect('knowledgebase')
    else:
        eknw = knowledgebases.objects.get(id=id)
        depts = departments.objects.all() 
        return render(request,"editknw.html" , {'eknw':eknw , 'depts':depts}) 

def deleteknw(request,id):
    dknw = knowledgebases.objects.get(id=id)
    dknw.delete()
    return redirect('knowledgebase')  

def addrole(request):
    if request.method == 'POST':
        role = roless(title=request.POST['title'])  
        role.save() 
        return redirect('roles')
    else:
        return redirect('nroles')        

def editrole(request,id):
    erole = roless.objects.get(id=id)
    return render(request , "editrole.html",{'erole':erole})

def updaterole(request,id):
    if request.method == 'POST':
        urole = roless.objects.get(id=id)
        urole.delete()  
        urole = roless(title=request.POST['title'])  
        urole.save() 
        return redirect('roles')
    else:
        erole = roless.objects.get(id=id)
        return render(request , "editrole.html",{'erole':erole})

def deleterole(request,id):
    drole = roless.objects.get(id=id)
    drole.delete()
    return redirect('roles')

def addstaff(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dept = request.POST['dept']
        role = request.POST['role']
        status = request.POST['status']
        password = request.POST['password']
        staff = staffss(name=name , email=email , dept=dept , role=role , status=status , password=password)
        staff.save()
        return redirect('staffs')
    else:
        return redirect('nstaffs')

def  editstaff(request,id):
    estaff = staffss.objects.get(id=id)
    depts = departments.objects.all()
    vroles = roless.objects.all()
    return render(request,"editstaff.html",{'estaff':estaff , 'depts':depts  , 'roles':vroles  })

def upddatestaff(request,id):
    if request.method == 'POST':
        ustaff = staffss.objects.get(id=id)
        ustaff.delete()
        name = request.POST['name']
        email = request.POST['email']
        dept = request.POST['dept']
        role = request.POST['role']
        status = request.POST['status']
        password = request.POST['password']
        ustaff = staffss(name=name , email=email , dept=dept , role=role , status=status , password=password)
        ustaff.save()
        return redirect('staffs')
    else:
        estaff = staffss.objects.get(id=id)
        depts = departments.objects.all()
        vroles = roless.objects.all()
        return render(request,"editstaff.html",{'estaff':estaff , 'depts':depts  , 'roles':vroles  })

def adduser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['psw']
        status = request.POST['status']
        nuser = nuserss(name=name , email=email , status=status , password1=password1)
        nuser.save()
        return redirect('users')
    else:
        return redirect('nusers')    

def edituser(request,id):
    enuser = nuserss.objects.get(id=id)
    return render(request,"editnuser.html",  {'enuser':enuser})

def updateuser(request,id):
    if request.method == 'POST':
        unuser = nuserss.objects.get(id=id)
        unuser.delete()
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['psw']
        status = request.POST['status']
        unuser = nuserss(name=name , email=email , status=status , password1=password1)
        unuser.save()
        return redirect('users')
    else:
        enuser = nuserss.objects.get(id=id)
        return render(request,"editnuser.html",  {'enuser':enuser})

def deletenuser(request,id):
    dnuser = nuserss.objects.get(id=id)
    dnuser.delete()
    return redirect('users')

