import sys
import string

## plain text 1
pt1 = "attack at dawn"
## ascii for text 1
acpt1 = "".join([hex(ord(x)) for x in pt1])
acpt1 = "0x"+"".join([x for x in string.split(acpt1,"0x")])

## plain text 2
pt2 = "attack at dusk"
## ascii for text 2
acpt2 = "".join([hex(ord(x)) for x in pt2])
acpt2 = "0x"+"".join([x for x in string.split(acpt2,"0x")])

## given the k xor acpt1, solve for k xor acpt2
ct1 = 0x6c73d5240a948c86981bc294814d

## also k xor acpt1 xor axpt1 = k
k=ct1 ^ int(acpt1,0)

##ct2 = k^acpt2
ct2 = k ^ int(acpt2,0)
print("k=",hex(k))        
print("ct2=",hex(ct2))

## Or, k xor acpt1 xor acpt1 xor acpt2 = k xor acpt2
ct2_m2= ct1 ^ int(acpt1,0) ^ int(acpt2,0)
print("ct2=ct1^pt1^pt2",hex(ct2_m2))
