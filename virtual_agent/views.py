from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from llama_cpp import Llama  # Импортируем LLama C++ Python
import os

# Путь к локальной GGUF-модели
LOCAL_MODEL_PATH = "E:\\LM\\models\\hermes\\nous-hermes-13b.ggmlv3.q2_K.bin"
assert os.path.exists(LOCAL_MODEL_PATH), f"Файл модели не найден: {LOCAL_MODEL_PATH}"

# Загружаем модель GGUF через llama-cpp-python
llm = Llama(model_path = r"E:\LM\models\hermes\nous-hermes-13b.ggmlv3.q2_K.bin", n_ctx=256, n_threads=4)

 # Настройте потоки в зависимости от CPU


def chat_interface(request):
    """Отображение HTML-страницы с чатом."""
    return render(request, "chat_interface.html")


@api_view(['POST'])
def chat_with_ai(request):
    """Генерация ответа с использованием `Hermes-3-Llama-3.2-3B-GGUF`."""

    user_input = request.data.get('question', '')

    if not user_input:
        return Response({"answer": "Пожалуйста, задайте ваш вопрос."}, status=400)

    try:
        # Генерация ответа с использованием llama-cpp-python
        output = llm(f"Q: {user_input}\nA:", max_tokens=200, temperature=0.7, top_p=0.9)

        # Получаем текст ответа
        answer = output["choices"][0]["text"].strip()

        return Response({"answer": answer})

    except Exception as e:
        return Response({"answer": f"Произошла ошибка: {str(e)}"}, status=500)
