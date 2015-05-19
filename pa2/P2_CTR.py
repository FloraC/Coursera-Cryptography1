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

## String for IV+n, n indicate the number of the block
def IV_new(IV,n):
    IV_num=int('0x'+IV.encode('hex'),0)+n
    IV_hex=hex(IV_num)[2:]
    if IV_hex[-1]=='L':
        IV_hex=IV_hex[:-1]
    result=IV_hex.decode('hex')
    return result
    
## AES encryption using CTR mode
## key and pt are strings
def encrypto_CTR_AES(key, pt):
    ## define the IV
    IV = Random.new().read(Block)
    ## define the number of blocks
    num_block=int(len(pt)/Block)
    ## Encrypto function
    fn_cipher=AES.new(key,AES.MODE_ECB)
    
    result=IV

    ## start encrypto
    for n in range(num_block+1):
        # calculate IV for encrypt
        IV_encry=IV_new(IV,n)
            
        cn=StrXOR(fn_cipher.encrypt(IV_encry), pt[:Block])
        pt=pt[Block:]
        result=result+cn

    return result.encode('hex')

## AES decryption using CBC mode
## key and ct are strings
def decrypto_CTR_AES(key,ct):
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
    for n in range(num_block+1):
        # calculate IV for decrypt
        IV_decry=IV_new(IV,n)
        pt=StrXOR(fn_cipher.encrypt(IV_decry),ct[:Block])
        ct=ct[Block:]
        result=result+pt

    return result

key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')    
ct1='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex')    
ct2='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex') 
pt1='CTR mode lets you build a stream cipher from a block cipher.'
pt2='Always avoid the two time pad!'
print decrypto_CTR_AES(key,ct1)    
print decrypto_CTR_AES(key,ct2)
ct3=encrypto_CTR_AES(key,pt1).decode('hex')
ct4=encrypto_CTR_AES(key,pt2).decode('hex')
print decrypto_CTR_AES(key,ct3)    
print decrypto_CTR_AES(key,ct4)  
        
