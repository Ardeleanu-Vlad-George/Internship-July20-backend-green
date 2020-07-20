from django.forms import ModelForm
from clubs.models import Club

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ['owner', 'name', 'description']