#This code is a test to repeat the Nunmber Trick shown by Dr. Jacobs.
print("""************************************************
Welcome! In this program, I will show you that I can predict the number Isaac will write down!
************************************************""")
num_1 = int(input("Please provide a 4 digit number: "))
print(num_1)
#Isaac will add 20004 to whatever the number is
num_2 = int(input("Please provide another 4 digit number: "))
print(num_2)
#The following loop will add 10005 to the second number
num_3 = 0

while((num_2 + num_3) < 10005):

    num_3 += 1

print(f"Ok! I shall provide a digit too!")
#Num 3 + Num 2 now add 10005 which will allow us to add 20004 later when combined with the next steps

print(num_3)
num_4 = int(input("give me another 4 digit number! 4 digits between 1-8: "))
#Num 5 and Num 4 must add to 9999, the next loop is created
num_5 = 0
while((num_4 + num_5) < 9999):
    num_5 += 1

print(f"I see, I shall put one last number:")
print(num_5)

sum_num = num_1 + num_2 + num_3 + num_4 + num_5

print("Let's add them all together!")
answer = input(f"I have {sum_num} as my answer. Did Isaac write {sum_num} in the sticky note? Yes/No: ")
lc_answer = answer.lower()

yes = "yes"
no = "no"

#Final function to give answers - made a safe-code in case they do not respond aproprietly
if lc_answer == yes:
    print("Wow! Its like magic!")
elif lc_answer == no:
    print("I guess Isaac needs to work on his tricks!")
else:
    answer_2 = input("Please answer as 'yes' or 'no': ")
    lc_answer2 = answer_2.lower()
    if lc_answer2 == yes:
        print("Wow! Its like magic!")
    else:
        print("I guess Isaac needs to work on his tricks!")