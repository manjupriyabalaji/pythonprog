vow=("a","e","i","o","u")
cons=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
letter=str(input())
if(letter in vow):
 print("vowel")
elif(letter in cons):
 print("constant")
else:
 print("invalid")
