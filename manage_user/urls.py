


from django.contrib import admin
from django.urls import path
from .views import showUser, insertUser, editUser, updateUser, deletUser, Voters, Committees, ShowUnaprovedUser, \
    aprovale, RejectUser, Candidates, profile, CandidatesForEvaluation, CandidatesForVote, key_check

urlpatterns = [
    path('',showUser,name="showUser"),
    path('edit/<int:id>', editUser, name="editUser"),
    path('insert/',insertUser, name="insertUser"),
    path('update/<int:id>',updateUser, name="updateUser"),
    path('delete/<int:id>',deletUser, name="deletUser"),
    path('aprove/',ShowUnaprovedUser, name="aprove"),
    path('aprove/<int:id>',aprovale, name="aprovale"),
    path('Reject/<int:id>',RejectUser, name="Reject"),
    path('Candidates',Candidates, name="Candidates"),
    path('Voters',Voters, name="Voters"),
    path('Committees',Committees, name="Committees"),
    path('CandidatesForVote/',CandidatesForVote, name="CandidatesForVote"),
    path('CandidatesForEvaluation/',CandidatesForEvaluation, name="CandidatesForEvaluation"),
    path('profile/',profile, name="profile"),
    path('key_check',key_check,name='key_check'),
]

