from django import forms
from .models import Request,Applicant

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields=(
            'unit_name',
            'member_1','inst_1',
            'member_2','inst_2',
            'member_3','inst_3',
            'member_4','inst_4',
            'member_5','inst_5',
            'recruit_inst1',
            'recruit_inst2',
            'recruit_inst3',
            'recruit_inst4',
            'recruit_inst5',
            'music',
            'comment',
            )

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields='__all__'