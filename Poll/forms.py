from django.forms import ModelForm
from .models import db


class Form_Poll(ModelForm):
    class Meta:
        model = db
        fields = ['poll_que', 'poll_option1',
                  'poll_option2', 'poll_option3', 'poll_option4']
