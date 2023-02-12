from gtts import gTTS  # type: ignore
from art import tprint  # type: ignore
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):

    # Проверяем, что по указанному пути есть файл
    # и файл имеет нужно расширение.
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+]Processing...')

        # Читаем DPF файл в обычную строку
        # С помощью mode='rb' открываем на чтение в двоичном режиме
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            # Пробегаемся по каждой странице и извлекаем текст из каждой.
            pages = [page.extract_text() for page in pdf.pages]

        # Склеиваем страницы.
        text = ''.join(pages)

        # Убираем переносы строк, так как они будут восприниматься как паузы.
        text = text.replace('\n', '')

        # Формируем аудио файл.
        my_audio = gTTS(text=text, lang=language, slow=False)

        # Получаем имя файла.
        file_name = Path(file_path).stem

        # Сохраняем аудио файл.
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully'

    else:
        return 'File does not exist! check the path!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose a language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
