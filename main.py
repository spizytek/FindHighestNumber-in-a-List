# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
idx =0

for n in range(0, len(student_scores)):

    if((n+1) < len(student_scores)):
        if(student_scores[n] > student_scores[n+1] ):
            idx = student_scores[n]
        else:
            if(student_scores[n+1] > idx):
                idx = student_scores[n+1]
print(f"The highest score in the class is: {idx}")
#Write your code below this row 👇

