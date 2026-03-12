from django.db import models

# Create your models here.


class AdminType(models.Model):
    Id= models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Name} ({self.Id})"
    class Meta:
        db_table = 'AdminType'

class AdminLogin(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Password = models.CharField(max_length=128)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    AdminType = models.ForeignKey(AdminType, on_delete=models.CASCADE, db_column='AdminType')
    Status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Name} ({self.Id})"
    
    class Meta:
        db_table = 'AdminLogin'

class Department(models.Model):
    DeptNo = models.AutoField(primary_key=True)
    Dname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.DeptNo} {self.Dname}"
    
    class Meta:
        db_table = 'Department'

class Employee(models.Model):
    EmpID = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Password = models.CharField(max_length=128)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Salary = models.FloatField()
    Address = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)
    IsAdmin = models.BooleanField(default=False)
    IsLoggedIn = models.BooleanField(default=False)
    DeptNo = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='DeptNo')

    def __str__(self):
        return f"{self.EmpID} {self.Ename}"
    
    class Meta:
        db_table = 'Employee'

class Doctor(models.Model):
    DocID = models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.DocID} {self.Dname}"
    
    class Meta:
        db_table = 'Doctor'

class Receptionist(models.Model):
    RecID = models.IntegerField(primary_key=True)
    Rname = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.RecID} {self.Rname}"
    
    class Meta:
        db_table = 'Receptionist'

class Helper(models.Model):
    HelperID = models.IntegerField(primary_key=True)
    Hname = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.HelperID} {self.Hname}"
    
    class Meta:
        db_table = 'Helper'

class Patient(models.Model):
    PatientID = models.IntegerField(primary_key=True)
    Pname = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    ReceptionistID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='ReceptionistID', related_name='receptionist_patients')
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='DoctorID')
    HelperID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='HelperID', related_name='helper_patients')
    Prescription = models.CharField(max_length=250)
    EntryDateandTime = models.DateTimeField(auto_now_add=True)
    ExitDateandTime = models.DateTimeField(null=True, blank=True)
    IsAdmitted = models.BooleanField(default=False)
    Medication = models.CharField(max_length=250)
    Bill= models.CharField(max_length=500)

    class Meta:
        db_table = 'Patient'

class CheckLogin(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    phone= models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'CheckLogin'
