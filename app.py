employees = []
leave_requests = []
leave_balances = {}



def initialize_leave_balance(employee_id):
    leave_balances[employee_id] = {
        "total_leave": 20,
        "used_leave": 0,
        "remaining_leave": 20
    }


def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter employee department: ")

    employee = {
        "id": employee_id,
        "name": name,
        "department": department
    }

    employees.append(employee)
    initialize_leave_balance(employee_id)
    print(f"{employee_id} added successfully.")


def apply_leave():
    employee_id = input("Enter employee ID: ")
    reason = input("Enter leave reason (e.g., sick, vacation): ")
    leave_days = int(input("Enter number of leave days: "))

    employee_exists = any(emp["id"] == employee_id for emp in employees)

    if not employee_exists:
        print(f"Employee ID {employee_id} not found. Please add the employee first.")
        return

    balance = leave_balances[employee_id]

    if leave_days > balance["remaining_leave"]:
        print(
            f"Insufficient leave balance. "
            f"Remaining leave: {balance['remaining_leave']} days."
        )
        return

    status = "Approved"
    if leave_days > 5:
        status = "Pending Manager Approval"
    leave_request = {
        "employee_id": employee_id,
        "reason": reason,
        "leave_days": leave_days,
        "status": status
    }

    leave_requests.append(leave_request)
    if status == "Approved":
        balance["used_leave"] += leave_days
        balance["remaining_leave"] -= leave_days
    print(f"Leave request for {employee_id} submitted successfully.")

def view_employees():
    if not employees:
        print("No Employees found")
        return
    print("\nEmployees")
    print("-"*40)
    for employee in employees:
        print(
            f"ID : {employee['id']} | "
            f"Name : {employee['name']} | "
            f"Department : {employee['department']}"
        )


def view_leave_requests():
    if not leave_requests:
        print("No leave requests are found")
        return
    print("\nLeave Requests")
    print("-"*40)
    for request in leave_requests:
        print(
            f"Employee ID: {request['employee_id']} | "
            f"Days: {request['leave_days']} | "
            f"Reason: {request['reason']} | "
            f"Status: {request['status']}"
        )

def view_leave_balance():
    employee_id = input("Enter employee ID to view leave balance: ")
    if employee_id in leave_balances:
        balance = leave_balances[employee_id]
        print(f"Leave Balance for Employee ID {employee_id}:")
        print(f"Total Leave: {balance['total_leave']}")
        print(f"Used Leave: {balance['used_leave']}")
        print(f"Remaining Leave: {balance['remaining_leave']}")
    else:
        print(f"No leave balance found for Employee ID {employee_id}.")


def main():
    while True:
        print("\n=====Employee Leave Management System=====")
        print("1. Add Employee")
        print("2. Apply Leave")
        print("3. View Employees")
        print("4. View Leave Requests")
        print("5. View Leave Balance")
        print("6. Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            add_employee()
        elif choice == 2:
            apply_leave()
        elif choice==3:
            view_employees()
        elif choice == 4:
            view_leave_requests()
        elif choice == 5:
            view_leave_balance()
        elif choice == 6:
            print("Exiting Application")
            break
        else:
            print("Invalid Choice. Please try again")

if __name__ =='__main__':
    main()