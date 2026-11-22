#taking input
st=input("enter your message:")
words=st.split(" ")
coding= input("1 for coding or 0 for decoding:")
coding= True if(coding=="1") else False

#coding Section
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="asd"
            r2="jkl"
            stnew= r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

#decoding section
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew= word[3:-3]
            stnew= stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    