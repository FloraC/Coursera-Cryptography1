import sys
from Crypto import Random
from Crypto.Cipher import AES

## 16-byte encryption IV is chosen at random
## and is prepended to the ciphertext
Block=16

## String XOR, different length
## return a string
def StrXOR(s1,s2):
    if len(s1) > len(s2):
        s1=s1[:len(s2)]
    else:
        s2=s2[:len(s1)]
    return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(s1,s2)])
    
## AES encryption using CBC mode
## key and pt are strings
def encrypto_CBC_AES(key, pt):
    ## define the IV
    IV = Random.new().read(Block)
    ## define the padding
    num_pad=Block-len(pt)%Block
    ## message to be encry
    for i in range(num_pad):
        pt+=chr(num_pad)
    ## Encrypto function
    fn_cipher=AES.new(key,AES.MODE_ECB)
    
    result=IV
    ## number of block
    num_block=len(pt)/Block

    ## start encrypto
    for n in range(num_block):
        cn=fn_cipher.encrypt(StrXOR(IV, pt[:Block]))
        IV=cn
        pt=pt[Block:]
        result=result+cn

    return result.encode('hex')

## AES decryption using CBC mode
## key and ct are strings
def decrypto_CBC_AES(key,ct):
    ## Decrypto function
    fn_cipher=AES.new(key, AES.MODE_ECB)
    ## Find IV
    IV=ct[:Block]
    ## ct to be decrypto
    ct=ct[Block:]

    result=''
    ## number of block
    num_block=len(ct)/Block

    ## start decrypto
    for n in range(num_block):
        pt=StrXOR(IV,fn_cipher.decrypt(ct[:Block]))
        IV=ct[:Block]
        ct=ct[Block:]
        result=result+pt

    ## remove the pad
    num_pad=ord(result[-1])

    return result[:(len(result)-num_pad)]

key='140b41b22a29beb4061bda66b6747e14'.decode('hex')    
ct1='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')    
ct2='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')
pt1='Basic CBC mode encryption needs padding.'
pt2='Our implementation uses rand. IV'
print decrypto_CBC_AES(key,ct1)    
print decrypto_CBC_AES(key,ct2)
ct3=encrypto_CBC_AES(key,pt1).decode('hex')
ct4=encrypto_CBC_AES(key,pt2).decode('hex')
print decrypto_CBC_AES(key,ct3)    
print decrypto_CBC_AES(key,ct4)       
