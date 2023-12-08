import os
from uuid import uuid4

def generate_filename(instance, filename):
    """Генерирует уникальное имя файла."""
    ext = filename.split('.')[-1]  # получаем расширение файла
    filename = f"{instance.name}_{uuid4().hex}.{ext}"  # создаем уникальное имя
    return os.path.join('photos', filename)  # возвращаем путь для сохранения
