from django.urls import path
from .views import ClothesView, ClothesDetailView, ClothesRecommendationView, CSRFTokenView, ClothesCleanUpView

app_name = 'clothes'

urlpatterns = [
    # 옷 목록 조회, 추가
    path('', ClothesView.as_view()),
    # 특정 옷 조회, 수정, 삭제
    path('<int:pk>/', ClothesDetailView.as_view()),
    # 옷 랜덤 추천
    path('reco/<int:gender>/', ClothesRecommendationView.as_view()),
    # 옷 DB 초기화
    path('clean-up/', ClothesCleanUpView.as_view()),
    # csrf-token
    path('csrf/', CSRFTokenView.as_view())
]
