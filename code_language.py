import random
import string

st = input('enter the message:')

words = st.split(" ")

Coding = input('enter 1 for encoding and 0 for decoding:')
Coding = True if (Coding=='1') else False
print(Coding)
if(Coding):
    nwords = []
    for word in words:
        r1 = random.choice(string.ascii_lowercase)
        r2 = str(random.randint(0,9))
        stnew = r1 + word[1:] + r2 + word[0] + r1
        nwords.append(stnew)
        
    newwords = " ".join(nwords)
    print(newwords)
    with open('myfile.txt','w') as a:
        a.write(newwords)
    print('the decoded message has been saved.')

else:
    nwords = []
    for word in words:
        stnew = word[1:-1]
        stnew = stnew[-1] + stnew[:-1]
        stnew = stnew[:-1]
        nwords.append(stnew)
        
    print(" ".join(nwords))

with open('myfile.txt','r')as e:
    to_decode = e.read()
asked = input("enter Yes to decode and No to exit:")
asked = True if (asked == 'yes') else False
print(asked)
if(asked):

    decode_word = [ ]
    for word in to_decode.split(" "):
        # if len(word) >=5:
        stnew = word[1:-1]
        stnew = stnew[-1] + stnew[:-1]
        stnew = stnew[:-1]
        decode_word.append(stnew)
        
    to_decode = " ".join(decode_word)
    print(to_decode)
    with open('myfile.txt', 'a')as k:
        a.write == decode_word
else:
    print('the coding is completed...')
