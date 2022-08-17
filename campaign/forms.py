from django import forms
from .models import CampaignModel,campaign_video,evaluation_video,fileUploading


class CampaignForms (forms.ModelForm):
    class Meta:
        model = CampaignModel
        fields = '__all__'
class campaign_videoForm (forms.ModelForm):
    class Meta:
        model = campaign_video
        fields = ['username','video_dis','video_file']

class evaluation_videoFrom (forms.ModelForm):
    class Meta:
        model = evaluation_video
        fields = ['username','video_dis','video_file']


class fileUploadingForms (forms.ModelForm):
    class Meta:
        model = fileUploading
        fields = ['username','file_dis','certificate_file']
