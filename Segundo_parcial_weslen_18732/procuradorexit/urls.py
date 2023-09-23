from .views import ProcuradorListView, ProcuradorDetailView, ProcuradorCreateView, ProcuradorUpdateView, ProcuradorDeleteView, home_view
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('procurador/', ProcuradorListView.as_view(), name='procurador_list'),
    path('procurador/<int:pk>/', ProcuradorDetailView.as_view(), name='procurador_detail'),
    path('procurador/create/', ProcuradorCreateView.as_view(), name='procurador_create'),
    path('procurador/<int:pk>/update/', ProcuradorUpdateView.as_view(), name='procurador_update'),
    path('procurador/<int:pk>/delete/', ProcuradorDeleteView.as_view(), name='procurador_delete'),
    
    #register
    path('login/', LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='paislist'), name='logout'),
    
    path('api/', include('procuradorexit.apiurls')),
    
    path('',home_view, name='base'),
]