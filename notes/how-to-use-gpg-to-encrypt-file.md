# How To Use GPG To Encrypt File

- Generate a GPG Keypair `gpg --gen-key`
- store the data you want to encrypt in a file in tmp e.g. `/tmp/foo.txt`
- encrypt `gpg --output ~/.foo.gpg --encrypt --recipient me@mydomain.com /tmp/.foo.txt`

## decrypt the file 

`gpg -dq ~/.foo.gpg`
