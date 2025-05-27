from PIL import Image

# 1. Открываем изображение
image = Image.open("input_image.jpg")  # замените на своё изображение

# 2. Поворот на 45 градусов с расширением границ
rotated = image.rotate(45, expand=True)

# 3. Уменьшение до 300×300 пикселей
resized = rotated.resize((300, 300))

# 4. Обрезаем верхние 110 пикселей
width, height = resized.size
if height > 110:
    cropped = resized.crop((0, 110, width, height))
else:
    raise ValueError("Изображение слишком маленькое для обрезки на 110 пикселей по высоте.")

# 5. Сохраняем результат
cropped.save("output_image.jpg")

print("Готово: изображение сохранено как 'output_image.jpg'")
