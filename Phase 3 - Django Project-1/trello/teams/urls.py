from django.urls import path
from .views import Team_List_view, Team_Detail_View, TeamCreateView, TeamDeleteView, TeamUpdateView
urlpatterns = [
    path('team_list/', Team_List_view.as_view(), name= 'team-list'),
    path('details_page/<int:pk>/', Team_Detail_View.as_view(), name = 'team-detail'),
    path("create/", TeamCreateView.as_view(), name="team-create"),
    path("update/<int:pk>/", TeamUpdateView.as_view(), name="team-update"),
    path("delete/<int:pk>/", TeamDeleteView.as_view(), name="team-delete"),
]
