from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    path('expenses/<int:pk>/download_balance_sheet/', ExpenseViewSet.as_view({'get': 'download_balance_sheet'})),
]
