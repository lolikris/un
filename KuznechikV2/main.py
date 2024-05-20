import uuid
import gostcrypto.gostcipher as gostcrypto
import os
def kuznechik(file: str, function: str = "encrypt", ):
    encrypted_file = f'{file}.pem'
    dop = str(uuid.uuid4().int)[:6]
    init_vect = bytearray([
        0x12, 0x34, 0x56, 0x78, 0x90, 0xab, 0xce, 0xf0,
    ])
    if function == 'encrypt':
        encrypt_file(file, encrypted_file, init_vect)
        return True
    elif function == 'decrypt':
        decrypt_file(encrypted_file, f"{dop}__{file}", init_vect)
        return True
    else:
        print("Unknown function, encrypt or decrypt")


def encrypt_file(input_file, output_file, init_vect):
    key = os.urandom(32)
    cipher_obj = gostcrypto.gost_34_13_2015.new('kuznechik', key, gostcrypto.gost_34_13_2015.MODE_CTR,
                                                init_vect=init_vect)

    buffer_size = 512

    with open(input_file, 'rb') as plain_file, open(output_file, 'wb') as cipher_file:
        buffer = plain_file.read(buffer_size)
        cipher_file.write(key)
        while len(buffer) > 0:
            cipher_data = cipher_obj.encrypt(buffer)
            cipher_file.write(cipher_data)
            buffer = plain_file.read(buffer_size)


def decrypt_file(input_file, output_file, init_vect):
    buffer_size = 512
    with open(input_file, 'rb') as cipher_file, open(output_file, 'wb') as plain_file:
        key = cipher_file.read(32)
        buffer = cipher_file.read(buffer_size)
        cipher_obj = gostcrypto.gost_34_13_2015.new('kuznechik', key, gostcrypto.gost_34_13_2015.MODE_CTR,
                                                    init_vect=init_vect)
        while len(buffer) > 0:
            plain_data = cipher_obj.decrypt(buffer)
            plain_file.write(plain_data)
            buffer = cipher_file.read(buffer_size)

