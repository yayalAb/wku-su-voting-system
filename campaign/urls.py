from django.urls import path,include
from .views import Campaign, Campaigns, campaignUpload, EvaluationUpload, Evaluation_videos, campaign_videos, \
    DocumentUpload, certificates, approvale_need_evaluation, approve_evaluation, approvale_need_campaign, \
    approve_campaign, delete_campaign, delete_Evaluation, approvale_need_certificates, approve_certificates,delete_certificates

urlpatterns = [
    path('',Campaign,name="Campaign"),
    path('Campaigns/',Campaigns,name="Campaigns"),
    path('campaignUpload/',campaignUpload,name="campaignUpload"),
    path('campaign_videos/',campaign_videos,name="campaign_videos"),
    path('approvale_need_campaign/',approvale_need_campaign,name="approvale_need_campaign"),
    path('approve_campaign/<int:id>',approve_campaign,name="approve_campaign"),
    path('delete_campaign/<int:id>',delete_campaign,name="delete_campaign"),

    path ('EvaluationUpload/', EvaluationUpload, name="EvaluationUpload"),
    path ('Evaluation_videos/', Evaluation_videos, name="Evaluation_videos"),
    path('approvale_need_evaluation/',approvale_need_evaluation,name="approvale_need_evaluation"),
    path('approve_evaluation/<int:id>',approve_evaluation,name="approve_evaluation"),
    path('delete_Evaluation/<int:id>',delete_Evaluation,name="delete_Evaluation"),

    path ('Upload/', DocumentUpload, name="DocumentUpload"),
    path ('certificates/', certificates, name="certificates"),
    path ('approvale_need_certificates/', approvale_need_certificates, name="approvale_need_certificates"),
    path ('approve_certificates/<int:id>', approve_certificates, name="approve_certificates"),
    path ('delete_certificates/<int:id>', delete_certificates, name="delete_certificates"),
]#