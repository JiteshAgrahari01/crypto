# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cSdTbWQEi5GpRdnUJfQPWtsiyIMb7xQr
"""

#Ceaser

def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if(char.isupper()):
      result += chr((ord(char) + s - 65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result
def decrypt(result,s):
  result1 = ""
  for i in range(len(text)):
    char = result[i] 
    if(char.isupper()):
      result1 += chr((ord(char) - s - 65) % 26 + 65)
    else:
      result1 += chr((ord(char) - s - 97) % 26 + 97)
  return result1
text = input("Enter Text: ")
s = int(input("Enter Key: "))
print("Cipher: " + encrypt(text,s))
ct=encrypt(text,s)
print("Decrypt: " + decrypt(ct,s))


#Vignere
def key_matching(PT,key):
 key = list(key)
 if len(key) == len(PT):
   return key
 else:
   for i in range(len(PT) - len(key)):
     key.append(key[i % len(key)])
   return ("" . join(key))
def encrypt(PT,key):
 en_text = []
 for i in range(len(PT)):
   x = (ord(PT[i]) +ord(key[i])) % 26
   x += ord('A')
   en_text.append(chr(x))
 return("" . join(en_text))

def decrypt(CT,key):
 en_text = []
 for i in range(len(CT)):
   x = (ord(CT[i]) - ord(key[i])+26) % 26
   x += ord('A')
   en_text.append(chr(x))
 return("" . join(en_text))
plain_text = input("Enter Plain Text:  ")
key_value = input("Enter Key:  ")
key = key_matching(plain_text, key_value) 
print("Cipher Text:  " + encrypt(plain_text,key))
Cipher_text = encrypt(plain_text,key)
print("Decryption Text:  " + decrypt(Cipher_text,key))


#AFFINE CIPHER

def encrypt_words():
    plain_text=input('Enter the plain text to be encrypted:')
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    cipher_text=''
    for i in plain_text:
        if i.isupper():
            x=ord(i)-65
            enc_val=(a*x+b)%26
            cipher_text+=' '+chr(enc_val+65)
        else:
            x=ord(i)-97
            enc_val=(a*x+b)%26
            cipher_text+=' '+chr(enc_val+97)
    print(cipher_text)

def decrypt_words():
    cipher_text=input('Enter the cipher text to be decrypted:')
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    c=0
    for i in range(1,27):
        if (a*i)%26==1:
            c=i
    plain_text=''
    for i in cipher_text:
        if i.isupper():
            y=ord(i)-65
            enc_val=(c*(y-b))%26
            plain_text+=' '+chr(enc_val+65)
        else:
            y=ord(i)-97
            enc_val=(c*(y-b))%26
            plain_text+=' '+chr(enc_val+97)
    print(plain_text)
    
encrypt_words()          
decrypt_words()
