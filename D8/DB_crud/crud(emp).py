from db_connection import connect_db

def add_employee():
    conn = connect_db()
    cursor = conn.cursor()
    first_name=input("Enter First Name:")
    last_name=input("Enter Last Name:")
    gender=input("Enter Gender (male/female/others):")
    dob=input("Enter Date of Birth(YYYY-MM-DD):")
    age=input("Enter Age:")
    email=input("Enter Email:")
    phone_no=input("Enter Phone Number:")
    roll_given=input("Enter Roll/Position:")
    dept=input("Enter Department:")
    join_timeline=input("Enter Join Date(YYYY-MM-DD):")
    address=input("Enter Address:")
    
    query ="""
    INSERT INTO EMPLOYEES
    (first_name, last_name, gender, DOB, age, email, phone_no, roll_given, dept, join_timeline, address)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    values = (
        first_name, 
        last_name,
        gender,
        dob,
        age,
        email,
        phone_no,
        roll_given,
        dept,
        join_timeline,
        address
    )
    
    cursor.execute(query, values)
    conn.commit()
    
    print("Employee added successfully!") 
    cursor.close()
    conn.close()

def view_all_employees():
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT * FROM EMPLOYEES"
    cursor.execute(query)
    employees = cursor.fetchall()
    
    if employees:
        print("\n--- All Employees ---")
        for emp in employees:
            print(emp)
    else:
        print("No employees found!")
    
    cursor.close()
    conn.close()

def update_employee():
    conn = connect_db()
    cursor = conn.cursor()
    
    emp_id = input("Enter Employee ID to update:")
    phone_no = input("Enter new Phone Number:")
    roll_given = input("Enter new Roll/Position:")
    
    query = """
    UPDATE EMPLOYEES 
    SET phone_no = %s, roll_given = %s 
    WHERE emp_id = %s
    """
    
    cursor.execute(query, (phone_no, roll_given, emp_id))
    conn.commit()
    
    print("Employee updated successfully!")
    cursor.close()
    conn.close()

def delete_employee():
    conn = connect_db()
    cursor = conn.cursor()
    
    emp_id = input("Enter Employee ID to delete:")
    
    query = "DELETE FROM EMPLOYEES WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    
    print("Employee deleted successfully!")
    cursor.close()
    conn.close()
    
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_all_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please try again.")
