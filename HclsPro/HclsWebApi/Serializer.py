from rest_framework import serializers
from .models import AdminType, AdminLogin, Department, Employee, Doctor, Patient, Receptionist, Helper, CheckLogin

class AdminTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminType
        fields = '__all__'

class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLogin
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'

class HelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helper
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
            class Meta:
                model = Patient
                fields = '__all__'

class CheckLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckLogin
        fields = '__all__'