print("Programme for calculating percentage in Madhyamik")
print("Let's Start")

beng=int(input(print("Enter your number in Bengali (Like : 85,90 etc..): ")))
eng=int(input(print("Enter your number in English : ")))
math=int(input(print("Enter your number in Mathematics : ")))
L_Sc=int(input(print("Enter your number in Life Science : ")))
P_Sc=int(input(print("Enter your number in Physical Science : ")))
Hist=int(input(print("Enter your number in History : ")))
Geo=int(input(print("Enter your number in Geography : ")))

percentage=round(float((beng+eng+math+L_Sc+P_Sc+Hist+Geo)/7),2)

print("Your percentage in Madhyamik is :",percentage)