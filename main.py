#!/usr/bin/env python
import gnupg
from getpass import getpass

pass_phrase = getpass("Enter Passphrase: ")

gpg = gnupg.GPG()


# generate key
input_data = gpg.gen_key_input(
    key_type='RSA',
    key_length=2048,
    name_email='surajbudha@yahoo.co.in',
    passphrase=pass_phrase,
    name_real='Suraj Budha Thoki',
    expire_date='5y',
    key_usage='sign,encrypt,auth',
    #algorithm='rsa4096'
)
key = gpg.gen_key(input_data)
print(key)

# create ascii-readable versions of pub / private keys
ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
ascii_armored_private_keys = gpg.export_keys(
    keyids=key.fingerprint,
    secret=True,
    passphrase=pass_phrase,
)

# export
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)