from django.db import models

# Create your models here.
class departments(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    dept_num = models.IntegerField()
    tickets = models.IntegerField(default = 0)


class  tickets(models.Model):
    problemtitle = models.CharField(max_length=300)
    priority = models.CharField(max_length=100)
    dept = models.CharField(max_length=200)
    msg = models.TextField()
    website = models.TextField()
    products = models.CharField(max_length=200)
    file = models.FileField()
    Idnum = models.CharField(max_length=100)
    username = models.CharField(max_length=300)
    reply = models.TextField()
    status =  models.BooleanField(default=False)

class fields(models.Model):
    field_name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=100)
    placeholder = models.CharField(max_length=200)
    field_length = models.IntegerField(default=0)
    field_required = models.BooleanField(default=False)
    field_status = models.BooleanField(default=False)

class knowledgebases(models.Model):
    dept = models.CharField(max_length=200)
    title = models.CharField(max_length=300)    
    desc = models.TextField()
    status = models.BooleanField(default=False)
    username = models.CharField(max_length=300)

class roless(models.Model):
    title = models.CharField(max_length=200)

class staffss(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dept = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    password = models.CharField(max_length=200)

class nuserss(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    status = models.BooleanField(default=False)
    password1 = models.CharField(max_length=200)  

class dashinput(models.Model):
    dusers = models.IntegerField()
    dstaffs = models.IntegerField()
    ddepartments = models.IntegerField()
    dknws = models.IntegerField()
    dsatisfied = models.IntegerField()
    dtickets = models.IntegerField()
    dotickets = models.IntegerField()
    dctickets = models.IntegerField()      


  