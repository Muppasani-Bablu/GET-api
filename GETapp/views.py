from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Model
from .serializers import ModelSerializers
from rest_framework import status

 #Create your views here.
class userModelModelAPIView(APIView):
    def get(self, request):
      try:
         # Retrieve all objects from the database
         queryset = Model.objects.all()
        
         # Serialize queryset
         serializer = ModelSerializers(queryset, many=True)
        
        # Return serialized data in the response
         return Response(serializer.data)
      except Exception as e:
            # Return an error response if an exception occurs
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import generics
# from GETapp.models import Model
# from GETapp.serializers import ModelSerializers
# from GETapp.utils import api_response

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt


# @method_decorator(
#     csrf_exempt, name="dispatch"
# )  # for simplicity, use csrf_exempt; consider adding proper CSRF protection
# class userCreateView(generics.ListCreateAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializers

#     def get(self, request):
       
#       # created_student = userModel.objects.get(id=id)
#       # created_student_name = created_student.student_name
            
#       return api_response(200, 'Successfully created bablu2. Please check once', {"self": "created_id"})
