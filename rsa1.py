
p=int(input("Enter a 1st prime no.:-"))
q=int(input("Enter a 2nd prime no.:-"))
n=p*q
pi_n = (p-1)*(q-1)
print("pi_n",pi_n)
d=int(input("enter a private key:-"))
e=0
for i in range(1,pi_n):
 if (d*i)%pi_n==1:
  e=i
 break
m=int(input("Enter a message:-"))
ciphertxt = (m**e)%n
plaintxt = (ciphertxt**d)%n
print("Public key(e,n)",(e,n))
print("Private key(d,n)",(d,n))
print("Message:-",m)
print("ciphertext:-",ciphertxt)
print("plaintext:-",plaintxt)
