marks = float(input("enter marks : "))
if(marks >= 90):
    print(f"You got A grade")
elif((marks >= 80) and (marks <= 89)):
    print(f"You got B1 grade")
elif((marks >= 70) and (marks <= 79)):
    print(f"You got B2 grade")
else:
    print("You have FAILED this course. Kindly contact course coordinator.")
