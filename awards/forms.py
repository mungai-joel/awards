from django import forms
from .models import Profile,Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','user_project_id']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']



class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')