from django import forms
from datetime import datetime
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    # upload_time = forms.DateTimeField(default = datetime.now)
