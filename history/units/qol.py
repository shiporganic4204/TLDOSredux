import os

def create_custom_files(source_folder, destination_folder):
    try:
        # Проверяем, существует ли исходная папка
        if not os.path.exists(source_folder):
            print(f"Ошибка: Исходная папка '{source_folder}' не существует.")
            return

        # Создаем целевую папку, если она не существует
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Получаем список файлов в исходной папке
        files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

        if not files:
            print("Ошибка: В исходной папке нет файлов для обработки.")
            return

        # Путь к шаблонному файлу
        template_path = os.path.join(destination_folder, "template.txt")

        # Проверяем, существует ли файл template
        if not os.path.exists(template_path):
            print(f"Ошибка: Шаблонный файл 'template.txt' отсутствует в папке '{destination_folder}'.")
            return

        # Читаем содержимое шаблонного файла
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        # Создаем новый файл для каждого файла в исходной папке
        for file in files:
            # Извлекаем первое слово из имени файла
            first_word = file.split()[0] if ' ' in file else file.split('.')[0]

            # Формируем новое имя для файла
            new_name = f"{first_word}_1936.txt"
            new_file_path = os.path.join(destination_folder, new_name)

            # Создаем новый файл с содержимым шаблона
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                new_file.write(template_content)

            print(f"Файл создан: {new_name}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    # Запрашиваем пути у пользователя
    source = input("Введите путь к исходной папке: ").strip()
    destination = input("Введите путь к целевой папке: ").strip()

    create_custom_files(source, destination)