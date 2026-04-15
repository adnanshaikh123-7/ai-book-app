from django.urls import path
from .views import get_books, add_book, ai_test, ai_chat,ai_summary
from .views import recommend_book
from .views import rag_query
from .views import delete_book

urlpatterns = [
    path('books/', get_books),
    path('books/add/', add_book),
    path('ai/',ai_test),
    path('chat/',ai_chat),
    path('ai-summary/',ai_summary),
    path('recommend/', recommend_book),
    path('rag/', rag_query),
    path('books/delete/<int:id>/', delete_book),
]