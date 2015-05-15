##Crypotograpy Problem Set 1
## Question 7

## define a function to decode 26 lower characters and space into
## 8-bit ascii written in hex
def cs2achex(ori_text):
    coded_text=0x0
    for letter in ori_text:
        if letter == " ":
            coded_text=coded_text*0x100+0x20
        if letter == "a":
            coded_text=coded_text*0x100+0x61
        if letter == "b":
            coded_text=coded_text*0x100+0x62
        if letter == "c":
            coded_text=coded_text*0x100+0x63
        if letter == "d":
            coded_text=coded_text*0x100+0x64
        if letter == "e":
            coded_text=coded_text*0x100+0x65
        if letter == "f":
            coded_text=coded_text*0x100+0x66
        if letter == "g":
            coded_text=coded_text*0x100+0x67
        if letter == "h":
            coded_text=coded_text*0x100+0x68
        if letter == "i":
            coded_text=coded_text*0x100+0x69
        if letter == "j":
            coded_text=coded_text*0x100+0x6a
        if letter == "k":
            coded_text=coded_text*0x100+0x6b
        if letter == "l":
            coded_text=coded_text*0x100+0x6c
        if letter == "m":
            coded_text=coded_text*0x100+0x6d
        if letter == "n":
            coded_text=coded_text*0x100+0x6e
        if letter == "o":
            coded_text=coded_text*0x100+0x6f
        if letter == "p":
            coded_text=coded_text*0x100+0x70
        if letter == "q":
            coded_text=coded_text*0x100+0x71
        if letter == "r":
            coded_text=coded_text*0x100+0x72
        if letter == "s":
            coded_text=coded_text*0x100+0x73
        if letter == "t":
            coded_text=coded_text*0x100+0x74
        if letter == "u":
            coded_text=coded_text*0x100+0x75
        if letter == "v":
            coded_text=coded_text*0x100+0x76
        if letter == "w":
            coded_text=coded_text*0x100+0x77
        if letter == "x":
            coded_text=coded_text*0x100+0x78
        if letter == "y":
            coded_text=coded_text*0x100+0x79
        if letter == "z":
            coded_text=coded_text*0x100+0x7a
    return coded_text

## plain text 1
pt1 = "attack at dawn"
## ascii for text 1
acpt1 = cs2achex(pt1)

## plain text 2
pt2 = "attack at dusk"
## ascii for text 2
acpt2 = cs2achex(pt2)

## given the k xor acpt1, solve for k xor acpt2
ct1 = 0x6c73d5240a948c86981bc294814d

## also k xor acpt1 xor axpt1 = k
k=ct1 ^ acpt1
print(["k="+hex(k)])

## ct2 = k^acpt2
ct2 = k ^ acpt2
            
print(["ct2="+hex(ct2)])
