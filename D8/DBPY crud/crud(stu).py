from db_connection import connect_db

def add_student():
    conn = connect_db()
    cursor = conn.cursor()
    f_name=input("Enter First Name:")
    l_name=input("Enter Last Name:")
    gender=input("Enter Gender:")
    dob=input("Enter Date of Birth(YYYY-MM-DD):")
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

def update_student():
    conn = connect_db()
    cursor = conn.cursor()
    
    stu_id = input("Enter Student ID to update:")
    phone = input("Enter new Phone Number:")
    course = input("Enter new Course:")
    department = input("Enter new Department:")
    
    query = """
    UPDATE student 
    SET phone = %s, course = %s, department = %s 
    WHERE stu_id = %s
    """
    
    cursor.execute(query, (phone, course, department, stu_id))
    conn.commit()
    
    print("Student updated successfully!")
    cursor.close()
    conn.close()

def delete_student():
    conn = connect_db()
    cursor = conn.cursor()
    
    stu_id = input("Enter Student ID to delete:")
    
    query = "DELETE FROM student WHERE stu_id = %s"
    cursor.execute(query, (stu_id,))
    conn.commit()
    
    print("Student deleted successfully!")
    cursor.close()
    conn.close()
    
while True:
    print("\nStudent Management System")
    print("1.Add Student")
    print("2.Update Student")
    print("3.Delete Student")
    print("4. Exit")
    
    choice = input("Enter your choice:")
    
    if choice =='1':
        add_student()
    elif choice =='2':
        update_student()
    elif choice =='3':
        delete_student()
    elif choice =='4':
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please try again.")