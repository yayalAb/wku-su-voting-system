"""voting_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include('announcement.urls')),
    path('Home/', include('Home.urls')),
    path('accounts/',include('Account.urls')),
    path('admin/', admin.site.urls),
    path('apis/v1/',include('Apis.urls')),
    path('user/', include('manage_user.urls')),
    path('vote/', include('vote.urls')),
    path('complain/', include('complain.urls')),
    path('voting_day/', include('schedule_voting_day.urls')),
    path('campaign/', include('campaign.urls')),
    path('Exam/',include('Exam.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

