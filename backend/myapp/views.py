from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def ai_test(request):
    url = "http://127.0.0.1:1234/v1/chat/completions"

    data = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {"role": "user", "content": "Hello bhai!"}
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()
    ai_reply = result['choices'][0]['message']['content']

    return Response({"reply":ai_reply})

@api_view(['POST'])
def ai_chat(request):
    user_msg = request.data.get("message")

    url = "http://127.0.0.1:1234/v1/chat/completions"

    data = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {"role": "user", "content": user_msg}
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()
    print(result)
    if "choices"in result:
        ai_reply = result["choices"][0]["message"]["content"]
    else:
        ai_reply = "bhai response format alag agaya"

    return Response({"reply": ai_reply})

@api_view(['POST'])
def ai_summary(request):
    text = request.data.get("text")

    url = "http://127.0.0.1:1234/v1/chat/completions"

    data = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {"role": "user", "content": f"Summarize this: {text}"}
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    if "choices" in result:
        summary = result["choices"][0]["message"]["content"]
    else:
        summary = "Error in AI response"

    return Response({"summary": summary})

@api_view(['POST'])
def recommend_book(request):
    text = request.data.get("text")

    url = "http://127.0.0.1:1234/v1/chat/completions"

    data = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {"role": "user", "content": f"If I like this book: {text}, recommend similar books."}
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    if "choices" in result:
        reply = result["choices"][0]["message"]["content"]
    else:
        reply = "Error in recommendation"

    return Response({"recommendation": reply})

@api_view(['POST'])
def rag_query(request):
    question = request.data.get("question")

    books = Book.objects.all()

    context = ""

    keywords = question.lower().split()

    for book in books:
        desc = book.description.lower()

        for word in keywords:
            if word in desc:
                context += f"{book.title}: {book.description}\n"
                break

    if context == "":
        context = "No relevant books found."

    url = "http://127.0.0.1:1234/v1/chat/completions"

    data = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": [
            {
                "role": "user",
                "content": f"Use this data:\n{context}\n\nAnswer this question:\n{question}"
            }
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    if "choices" in result:
        answer = result["choices"][0]["message"]["content"]
    else:
        answer = "Error in RAG"

    return Response({"answer": answer})

@api_view(['DELETE'])
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return Response({"message": "Deleted successfully"})
    except Book.DoesNotExist:
        return Response({"error": "Book not found"})