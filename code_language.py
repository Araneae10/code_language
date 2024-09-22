import random
import string

a= list(string.ascii_lowercase)

st = input('enter the message:')

words = st.split(" ")

Coding = input('enter 1 for encoding and 0 for decoding:')
Coding = True if (Coding=='1') else False
print(Coding)
if(Coding):
    nwords = []
    for word in words:
        if(len(word)>=5):
            r1 = random.choice(a)
            # r2 = random.choice(a)
            stnew = r1 + word[1:] + word[0] + r1
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    newwords = " ".join(nwords)
    print(newwords)
    with open('myfile.txt','w') as a:
        a.write(newwords)
    print('the decoded message has been saved.')

else:
    nwords = []
    for word in words:
        if len(word)>=5:
            stnew= word[1:-1]
            stnew= stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

with open('myfile.txt','r')as e:
    to_decode = e.read()
asked = input("enter Yes to decode and No to exit:")
asked = True if (asked == 'Yes') else False
print(asked)
if(asked):

    decode_word = [ ]
    for word in to_decode.split(" "):
        if len(word) >=5:
            stnew = word[1:-1]
            stnew = stnew[-1] + stnew[:-1]
            decode_word.append(stnew)
        else:
            decode_word.append(word[::-1])
    to_decode = " ".join(decode_word)
    print(to_decode)
else:
    print('the program is completed...')
