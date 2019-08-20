from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# 라우터를 생성하고 뷰셋을 등록한다.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URL을 라우터가 자동으로 인식한다.
urlpatterns = [
    path('', include(router.urls)),
]