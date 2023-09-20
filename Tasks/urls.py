from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    # Create new or get list of all tasks 
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    # Read,Update,Delete particular tasks by their id.
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # To generate JWT access_token + refresh_token using login creds 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # To refresh the expired access token by passing the previous refresh_token
    path('tasks/sort/', views.TaskSortListView.as_view(), name='task-sort-list'),
    # You can sort tasks by specifying a query parameter ex: ?sort_by=due_date or ?sort_by=title.
    path('tasks/filter/', views.TaskFilterListView.as_view(), name='task-filter-list'),
    # You can filter tasks based on status and due_date ex: ?status=in_progress or ?due_date=due_date.
]