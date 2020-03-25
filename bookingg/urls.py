from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:id>/', views.MakeReservationView.as_view(), name='booking'),
    path('add/', views.CreateRoomView.as_view(), name='add_room'),
    path('<int:id>/', views.RoomDetailsView.as_view(), name='room_details'),
    path('update/<int:id>/', views.UpdateRoomView.as_view(), name='room_update'),
    path('list/', views.AllRoomsView.as_view(), name='rooms_list'),
    path('delete/<int:id>', views.DeleteRoomView.as_view(), name='delete_room'),
    path('deleted/', views.DeletedRoomView.as_view(), name='deleted_room'),
    path('search/', views.SearchRoomView.as_view(), name='search_room'),
]