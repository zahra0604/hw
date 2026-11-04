from student.service import add_student,show_student,delete_student

def main():
    while True:
        print("1.add student")
        print("2.show student")
        print("3.delete student")
        print("4.exit")
        
        choice=input("choose:")
        if choice=="1":
            add_student()
        elif choice=="2":
            show_student()
        elif choice=="3":
            delete_student()
        elif choice=="4":
            print("good bye")
            break
        else:
            print("invalid choice")
            
if __name__=="__main__":
    main()