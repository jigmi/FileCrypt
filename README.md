
![security - rsa encryption flaw v2 (1)](https://user-images.githubusercontent.com/87882680/150626195-f853b377-72ac-45c7-a477-8f7ff225a196.jpg)
 [![jigmi - PyCryptRAT-MultiClientEncryptedRAT](https://img.shields.io/static/v1?label=jigmi&message=FileCrypt&color=black&logo=github)](https://github.com/jigmi/FileCrypt "Go to GitHub repo")
 [![stars - PyCryptRAT-MultiClientEncryptedRAT](https://img.shields.io/github/stars/jigmi/FileCrypt?style=social)](https://github.com/jigmi/FileCrypt)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](https://opensource.org/licenses/MIT) [![Python 3.9.9](https://img.shields.io/badge/python-3.9.9-black.svg)](https://www.python.org/downloads/release/python-399/)
# File encryption program using Python 
FileCrypt is a program that encrypts the selected file with AES 256 bit encryption using a 32 byte password that the user inputs, the password is then passed into a password based key derivative function (PBKDF2) which allows a user to enter a password which will be converted into the key for encryption.

 ![Screenshot 2022-01-22 194027](https://user-images.githubusercontent.com/87882680/150631330-4872211f-2b64-474e-a60e-ff9bbe7ba7a0.png)


![Screenshot 2022-01-23 221228](https://user-images.githubusercontent.com/87882680/150675690-5e192e75-dac5-4f8d-8573-31733645d3df.png)

# Key Modules
Tkinter for GUI

pycryptodomex for AES encryption 

# Dependancies
- Pycryptodomex
```python
pip install pycryptodomex
```
# How to encrypt and decrypt
1. Run the application and select any file that you want to be encrypted.
2. Enter your password to be used for encryption and subsequent decryption, the password can be of any length, letter and symbol. 
3. Click Encryption, the file that you selected will have its encrypted version created in the same directory, with .enc to signify its encryped status, the original file will have been deleted automatically. 
4. Select the encrypted file, then enter the password used for encryption to decrypt the file, if the password is correct, the decrypted file will have been created. If the password is incorrect, the file will remain decrypted till the correct password is given.
