from django.urls import path
from .views import ListUser,DetailUser,profile,campaigns,Response,Voters,Committes,Announcements,Announcement,Complains,Complain,Schedules,SnippetDetail,Schedule,Votes,Vote,notes ,Detailnotes,Candidates,voting

urlpatterns = [
    path('',ListUser.as_view()),
    path('<int:pk>/', DetailUser.as_view()),

    path('Announcements', Announcements.as_view()),
    path('Announcement/<int:pk>/', Announcement.as_view()),

    path ('Complains', Complains.as_view ()),
    path ('Complain/<int:pk>/', Complain.as_view ()),
    path ('Response', Response.as_view ()),

    path ('Schedules', Schedules.as_view ()),
    path ('Schedule/<int:pk>/', Schedule.as_view ()),
    
    path ('Votes', Votes.as_view ()),
    path ('Vote/<int:pk>/', Vote.as_view ()),

    path ('notes', notes.as_view ()),
    path ('notes/<int:pk>/', Detailnotes.as_view ()),

    path ('Candidates', Candidates.as_view ()),
    path ('Committes', Committes.as_view ()),
    path ('Voters', Voters.as_view ()),

    path ('voting', voting.as_view()),
    path ('snip/<str:username>/', SnippetDetail.as_view()),
    path ('profile/<str:username>/', profile.as_view()),

    path ('campaigns', campaigns.as_view ()),
]