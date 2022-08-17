from rest_framework import serializers

from .models import User,AnnounceModel,Responsemodel,ComplainModel,ScheduleModel,VotingModel,notesModel,CampaignModel


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       fields = "__all__"
       model = User

class AnnounceSerializer (serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = AnnounceModel


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ComplainModel

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ScheduleModel

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','username', 'protocol', 'presentation_skill', 'confidence', 'strategic_plane', 'answering', 'Time_management']
        model = VotingModel


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'user_fname','user_lname']
        model = User


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','username', 'certifcate', 'written_exam', 'oral_interview', 'Str_and_opra_plane']
        model = VotingModel


class notesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = notesModel

class campaignSerializer(serializers.ModelSerializer):
   class Meta:
       fields = "__all__"
       model = CampaignModel

class ResponseSerializer (serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Responsemodel



