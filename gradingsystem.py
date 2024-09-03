def main():
    user_marks = float(input("Enter your mark: "))
    grade = compute_mark(user_marks)
    print(grade)

def compute_mark(user_marks):
    if user_marks <0 or user_marks >100:
        return "Invalid Grade"
    elif user_marks  >= 90 and user_marks <= 100:
        return "Grade A"
    elif user_marks  <90 and user_marks >= 80:
        return "Grade B"
    elif user_marks  <80 and user_marks >=70:
        return "Grade C"
    elif user_marks <70 and user_marks >=60:
        return "Grade D"
    else:
         return "Grade E"
    
if __name__ == "__main__":
    main()
    