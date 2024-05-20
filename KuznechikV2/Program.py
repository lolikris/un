import os
import main
def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        print(f"Файл '{file_path}' не существует.")

def list_files():
    print("Список файлов в текущем каталоге:")
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    return files

Crypt = 'encrypt' if input('Введите 1 для encrypt или 2 для decrypt: ') == '1' else 'decrypt'
file = input('Введите Имя файла с расширением(.pem Исключение; файл должен быть в папке с программой): ')
main.kuznechik(file,Crypt)
if Crypt == 'decrypt': file = file + '.pem'
delete_file(file)