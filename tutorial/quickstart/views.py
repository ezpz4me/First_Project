from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import signupserializer
from .models import signup

# Create your views here.
class signupviews(APIView):
    def post(self, request):
        serializer= signupserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        return Response({'staus':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id= None):
        if id:
            item=signup.objects.get(id=id)
            serializer=signupserializer(item)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        items=signup.objects.all()
        serializer=signupserializer(items,many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)