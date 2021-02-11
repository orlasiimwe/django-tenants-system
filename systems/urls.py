from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.get_home, name= 'home'),
    path('visitors', views.get_visitors ,name='get_visitors'),
    path('visitors/add_visitors' ,views.add_visitors, name='add_visitors'),
    path('visitors/<int:pk>' ,views.visitor_details, name='visitor_details'),
    path('visitors/<int:pk>/update', views.update_visitor, name='update_visitor'),
    # path('search_result', views.search, name='search')
]
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]
