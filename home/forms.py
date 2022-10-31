from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:      #inner class used for getting the same fields as Student model
        model=Student
        fields=('fullname','mobile','stud_code','address')
        labels={
            'fullname':'Full Name',
            'mobile':'Mobile Number',
            'stud_code':'Student ID',
            'address':'Address',
        }

def __init__(self,*args,**kwargs): 
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['stud_code'].required=False


