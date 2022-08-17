from django.http import JsonResponse, Http404
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User,AnnounceModel,ScheduleModel,ComplainModel,VotingModel,notesModel,Voters,CampaignModel,Responsemodel
from .serializers import  campaignSerializer,UserSerializer,AnnounceSerializer,ScheduleSerializer,ResponseSerializer,ComplainSerializer,VoteSerializer,notesSerializer,CandidatesSerializer


class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Announcements(generics.ListCreateAPIView):
    queryset = AnnounceModel.objects.all()
    serializer_class = AnnounceSerializer

class Announcement(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnnounceModel.objects.all()
    serializer_class = AnnounceSerializer

class Complains(generics.ListCreateAPIView):
    queryset = ComplainModel.objects.all()
    serializer_class = ComplainSerializer

class Complain(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComplainModel.objects.all()
    serializer_class = ComplainSerializer

class Schedules(generics.ListCreateAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer

class Schedule(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer

class Candidates(APIView):
    def get(self, request):
        candidate = User.objects.filter(user_role='Candidate')
        serializer = CandidatesSerializer(candidate, many=True)
        return Response(serializer.data)

class Response(generics.ListCreateAPIView):
    queryset = Responsemodel.objects.all()
    serializer_class = ResponseSerializer

class Voters(APIView):
    def get(self, request):
        candidate = User.objects.filter(user_role='Voter')
        serializer = CandidatesSerializer(candidate, many=True)
        return Response(serializer.data)

class Committes(APIView):
    def get(self, request):
        candidate = User.objects.filter(user_role='Committee')
        serializer = CandidatesSerializer(candidate, many=True)
        return Response(serializer.data)


class Votes(generics.ListCreateAPIView):
    queryset = VotingModel.objects.all()
    serializer_class = VoteSerializer

class Votes (generics.ListCreateAPIView):
    queryset = Responsemodel.objects.all ()
    serializer_class = ResponseSerializer

class Vote(generics.RetrieveUpdateDestroyAPIView):
    queryset = VotingModel.objects.all()
    serializer_class = VoteSerializer

class notes(generics.ListCreateAPIView):
    queryset = notesModel.objects.all()
    serializer_class = notesSerializer

class Detailnotes(generics.RetrieveUpdateDestroyAPIView):
    queryset = notesModel.objects.all()
    serializer_class = notesSerializer


class campaigns(generics.ListCreateAPIView):
    queryset = CampaignModel.objects.all()
    serializer_class = campaignSerializer

class voting(APIView):
    def get(self, request):
        snippets = VotingModel.objects.all()
        serializer = VoteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        #data = JSONParser ().parse (request)
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def  changeStatus(name,isVote):
    cand= VotingModel.objects.all ()
    username="workuasasa@vote"
    votr_sta = Voters.objects.get (username=username)
    i=0
    print(name)
    for item in cand:
        print (name ,item.username, i)
        if item.username==name and i==0:
            print ("cand1")
            if votr_sta.cand1 == False:
                Voters.objects.filter (username=username).update (stat=True,cand1=True)
                isVote = True
                print ("cand1")

        elif item.username == name and i == 1:
            print ("cand2")
            if votr_sta.cand2 == False:
                Voters.objects.filter (username=username).update (stat=True, cand2=True)
                isVote = True
                print ("cand2")

        elif item.username == name and i == 2:
            print ("cand3")
            if votr_sta.cand3 == False:
                Voters.objects.filter (username=username).update (stat=True, cand3=True)
                isVote = True
                print ("cand3")

        elif item.username == name and i == 3:
            print ("cand4")
            if votr_sta.cand4 == False:
                Voters.objects.filter (username=username).update (stat=True, cand4=True)
                isVote = True
                print ("cand4")

        elif item.username == name and i == 4:
            print ("cand5")
            if votr_sta.cand5 == False:
                Voters.objects.filter (username=username).update (stat=True, cand5=True)
                isVote = True
                print ("cand5")

        elif item.username == name and i == 5:
            print ("cand6")
            if votr_sta.cand6 == False:
                Voters.objects.filter (username=username).update (stat=True, cand6=True)
                isVote = True
                print ("cand6")
        i=i+1
        if isVote:
            return True
    return False

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, username):
        try:
            return VotingModel.objects.get(username=username)
        except VotingModel.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        snippet = self.get_object(username)
        serializer = VoteSerializer(snippet)
        return Response(serializer.data)
                
    def put(self, request, username, format=None):
        query = self.get_object(username)
        pro = query.protocol + float (request.data.get ('protocol'))
        pre = query.presentation_skill + float (request.data.get ('presentation_skill'))
        conf = query.confidence + float (request.data.get ('confidence'))
        stra = query.strategic_plane + float (request.data.get ('strategic_plane'))
        ans = query.answering + float (request.data.get ('answering'))
        tm = query.Time_management + float (request.data.get ('Time_management'))
        total = tm + ans + stra + conf + pre + pro
        total_100 = query.Total_40 + total
        print(pro,pre, conf, stra, ans, tm, total,total_100)
        serializer = VoteSerializer (query, data=request.data)
        candidate=request.data.get('username')
        if serializer.is_valid():
            if changeStatus (candidate, False):
                VotingModel.objects.filter (username=candidate).update (protocol=pro, presentation_skill=pre,
                                                                        confidence=conf, strategic_plane=stra,
                                                                        answering=ans, Time_management=tm,
                                                                        Total_60=total,
                                                                        Total_100=total_100)
                print("voted ss")
            else:
                return Response (serializer.data)

           # serializer.save()
           # return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profile(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

