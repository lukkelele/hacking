from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from os import urandom, read
import base64

mod = 256   # blocksize

# Generate a key with a length of 256*n bits
def generate_keys(n):
    key = RSA.generate(mod*n)
    privkey, pubkey = key.export_key(), key.publickey().export_key()
    return privkey, pubkey


def save_keys(privkey, pubkey, path="./"):
    for i in range(2):
        if i == 0:
            key = privkey
            keyname = 'private.pem'
        else:
            key = pubkey
            keyname = 'public.pem'
        file = open(keyname, 'wb')
        file.write(key)

privkey, pubkey = generate_keys(8)
save_keys(privkey, pubkey)
