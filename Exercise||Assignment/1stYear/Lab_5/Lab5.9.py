hei = int(input("Height : "))

if hei >= 1 :
    for i in range(0,hei):
        h=hei-i-1
        d=2*i+1
        print("#"*h+"."*d+"#"*h)

else :
    print("Error")