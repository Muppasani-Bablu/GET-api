# from django.urls import path
# from .views import userModelCreateView

# urlpatterns = [
#     path('userModel/', userModelCreateView.as_view(), name='userModel-list-create'),
# ]

from django.urls import path
from .views import userModelModelAPIView

urlpatterns = [
    path('userModel/', userModelModelAPIView.as_view(), name='Model-model-api'),
]
