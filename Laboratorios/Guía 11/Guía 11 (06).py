import glob #lista los archivos del ordenador
lista_todos = glob.glob('*')
print('Lista de todos los archivos y carpetas en la carpeta actual:')
print(lista_todos)
lista_py = glob.glob('*.py')
print('Lista de todos los archivos .py en la carpeta actual:')
print(lista_py)
print('Numero total de archivos .py en la carpeta actual = ', len(lista_py))