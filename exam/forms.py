from django import forms
from .models import Script

class AnsForm(forms.ModelForm):

	class Meta:
		model=Script
		exclude=['title', 'userid', 'send_otl_script',
			'send_result', 'number_scored']
