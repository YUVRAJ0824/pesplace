from db_connection import connect_db

def add_employee():
    try:
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
    except Exception as e:
        print(f"Error adding employee: {e}")

# Update employee details
def update_employee():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        emp_id = input("Enter Employee ID to update:")
        phone_no = input("Enter new Phone Number:")
        roll_given = input("Enter new Roll:")
        
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
    except Exception as e:
        print(f"Error updating employee")
# Delete employee record
def delete_employee():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        emp_id = input("Enter Employee ID to delete:")
        query = "DELETE FROM EMPLOYEES WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))
        conn.commit()
        
        print("Employee deleted successfully!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error deleting employee ")
    
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        update_employee()
    elif choice == '3':
        delete_employee()
    elif choice == '4':
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
