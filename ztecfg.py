from Crypto.Cipher import AES
from binascii import a2b_hex
KEY = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
def decrypt(text):
    cryptor = AES.new(KEY, AES.MODE_ECB)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return plain_text
cfg_file = open("db_user_cfg.xml", "rb")
dec_file = open("db_user_cfg.decode.xml", "w")
file_header = cfg_file.read(60)
while 1:
    trunk_info = cfg_file.read(12)
    trunk_data = cfg_file.read(65536)
    trunk_real_size = int.from_bytes(trunk_info[0:4], byteorder='big', signed=False)
    trunk_size = int.from_bytes(trunk_info[4:8], byteorder='big', signed=False)
    next_trunk = int.from_bytes(trunk_info[8:12], byteorder='big', signed=False)
    print(trunk_real_size, trunk_size, next_trunk)
    dec_file.write(decrypt(trunk_data.hex()).decode(encoding="utf-8"))
    if next_trunk==0:
        break
