import hashlib

arquivo_alvo = input("Qual o nome do arquivo que se encontra neste diretório? Escreva o nome completo + extensão")
path = r'C:\Users\daida\Desktop\PythonNetwork\Hash_Integrity\exemplo.txt'

with open(path, 'rb') as opened_file:
    content = opened_file.read()
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()

    md5.update(content)
    sha1.update(content)
    sha224.update(content)
    sha256.update(content)
    sha384.update(content)
    sha512.update(content)

    print('Result')
    print()
    print('{}: {}'.format(md5.name,md5.hexdigest()))