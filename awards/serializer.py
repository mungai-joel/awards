from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_picture','prof_user','bio','all_projects')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','details','link','image','design','usability','content')