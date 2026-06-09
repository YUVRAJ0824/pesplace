from db_connection import connect_db

def add_student():
    conn = connect_db()
    cursor = conn.cursor()
    f_name=input("Enter First Name:")
    l_name=input("Enter Last Name:")
    gender=input("Enter Gender:")
    dob=input("Enter Date of Birth(YYY-MM-DD):")
    email=input("Enter Email:")
    phone=input("Enter Phone:")
    course=input("Enter Course:")
    department=input("Enter Department:")
    admission=input("Enter Admission Date(YYY-MM-DD):")
    address=input("Enter Address:")
    
    query ="""
    insert into student
    (f_name, l_name, gender, dob, email, phone, course, department, admission, address)
    values(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
    """
    
    values = (
        f_name, 
        l_name,
        gender,
        dob,
        email,
        phone,
        course,
        department,
        admission,
        address
    )
    
    cursor.execute(query, values)
    conn.commit()
    
    print("Student added sucessfully!") 
    cursor.close()
    conn.close()   
    
while True:
    print("\nStudent Management System")
    print("1.Add Student")
    print("2. Exit")
    
    choice = input("Enter your choice:")
    
    if choice =='1':
        add_student()
    elif choice =='2':
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please try again.")