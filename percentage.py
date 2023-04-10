classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print(f"Percentage of classes attended: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("Sorry, you are not allowed to sit in the exam.")
