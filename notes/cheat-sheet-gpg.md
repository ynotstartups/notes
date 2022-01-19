# Cheat Sheet GPG

## How To Use GPG To Encrypt File

- Generate a GPG Keypair `gpg --gen-key`
- store the data you want to encrypt in a file in tmp e.g. `/tmp/foo.txt`
- encrypt `gpg --output ~/.foo.gpg --encrypt --recipient me@mydomain.com /tmp/.foo.txt`

## decrypt the file

`gpg -dq ~/.foo.gpg`

## How to export keys

`--armor` gives a ascii output, otherwise it is binary.

**Public Key**

`gpg --export --armor foo@bar.com > /path/to/public.key`

**Public Secret key**

`gpg --export-secret-keys --armor foo@bar.com > /path/to/private.key`

## My Public Key

Email: tiger huang yu hao AT google mail

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=ZOO8
-----END PGP PUBLIC KEY BLOCK-----
```
