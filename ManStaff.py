import ManClass as mc
import ManDB as db

shopEmp = {}

def is_emp_db_empty() -> bool:
    # Someone please make me a function that can check if the employee database is empty/not created yet - Alex
    return True

def add_employee(name, password, position='emp', add_to_db=True):
    if name:
        new_emp = mc.Employee(name=name, permission=position)
        if new_emp:
            new_emp.set_password(password)
            print("Successfully added new employee.")
            if add_to_db:
                emp_database = db.EmployeesDatabase()
                emp_database.start_session()
                emp_database.add_employee(new_emp)
                print("Employee added to database.")
            ret = new_emp.get_name()
        else:
            print("Error: ManStaff: add_employee(): Invalid name.")
            ret = 2
    else:
        print("Error: ManStaff: add_employee(): Invalid name.")
        ret = 3
    return ret

def login(name, password):
    if shopEmp[name].checkpass():
        if shopEmp[name].set_logout_time():
            print("ManStaff: login(): Successfully login.")
            ret = 4
        else:
            print("ManStaff: login(): Already login.")
            ret = 5
    else:
        print("ManStaff: login(): Wrong password.")
        ret = 6
    return ret

def logout(name, password):
    if shopEmp[name].checkpass(password):
        res = shopEmp[name].set_logout_time()
        if res == 1:
            print("ManStaff: logout(): Successfully logout.")
            ret = 7
        elif res == 2:
            print("ManStaff: logout(): Already logout.")
            ret = 8
        else:
            print("ManStaff: logout(): This employee did not login yet.")
            ret = 9
    else:
        print("ManStaff: logout(): Wrong password.")
        ret = 10
    return ret

def remove_employee(name, current_user, password):
    if shopEmp[current_user].is_admin():
        if shopEmp[current_user].checkpass(password):
            if name in shopEmp:
                del shopEmp[name]
                print("Successfully remove employee")
                ret = 11
            else:
                print("Error: ManStaff: remove_employee(): This Employee does not exist.")
                ret = 12
        else:
            print("Error: ManStaff: remove_employee(): Wrong Password.")
            ret = 13
    else:
        print("Error: ManStaff: remove_employee(): Require Admin Permission.")
        ret = 14
    return ret

def add_admin(name, current_user, password):
    new_admin = shopEmp[current_user].add_admin(name, password)
    if new_admin == 2:
        print("Error: ManStaff: add_admin(): Wrong Password.")
        ret = 15
    elif new_admin == 3:
        print("Error: ManStaff: add_admin(): Require Admin Permission.")
        ret = 16
    else:
        print("Successfully added admin.")
        ret = 17
    return ret

def promote_to_admin(name, current_user, password):
    suc = shopEmp[current_user].set_to_admin(shopEmp[name], password)
    if suc == 1:
        print("Successfully promoted.")
        ret = 18
    elif suc == 2:
        print("Error: ManStaff: promote_to_admin(): Wrong Password.")
        ret = 19
    elif suc == 3:
        print("Error: ManStaff: promote_to_admin(): Require Admin Permission.")
        ret = 20
    elif suc == 4:
        print("Error: ManStaff: promote_to_admin(): employee is not Employee object.")
        ret = 21
    return ret

def demote_from_admin(name, current_user, password):
    suc = shopEmp[current_user].demote_from_admin(shopEmp[name], password)
    if suc == 1:
        print("Successfully promoted.")
        ret = 22
    elif suc == 2:
        print("Error: ManStaff: demote_from_admin(): Wrong Password.")
        ret = 23
    elif suc == 3:
        print("Error: ManStaff: demote_from_admin(): Require Admin Permission.")
        ret = 24
    elif suc == 4:
        print("Error: ManStaff: demote_from_admin(): employee is not Employee object.")
        ret = 25
    return ret

def set_password(name, password):
    suc = shopEmp[name].set_password(password)
    if suc == 1:
        print("Successfully set password.")
        ret = 26
    elif suc == 2:
        print("Error: ManStaff: set_password(): password has to be 4 characters.")
        ret = 27
    elif suc == 3:
        print("Trying to pass this wall?? no way!!!")
        ret = 28
    return ret

def change_password(name, old_pass, new_pass):
    res = shopEmp[name].change_password(old_pass, new_pass)
    if res == 1:
        print("Successfully change password.")
        ret = 29
    elif res == 2:
        print("New password has to be 4 characters.")
        ret = 29
    elif res == 3:
        print("Invalid Password (Previous Password does not match).")
        ret = 31
    return ret

def forgot_password(name, key, new_pass):
    if len(new_pass) != 4:
        print("New password has to be 4 characters.")
        ret = 32
    elif shopEmp[name].forgot_password(key, new_pass):
        print("Successfully change password.")
        ret = 33
    else:
        print("Error: ManStaff: forgot_password(): Wrong recovery key.")
        ret = 34
    return ret

def get_message(code):
    if code == 2:
        ret = "Invalid name."
    elif code == 3:
        ret = "Invalid name."
    elif code == 4:
        ret = ""
    elif code == 5:
        pass
    elif code == 6:
        pass
    elif code == 7:
        pass
    elif code == 8:
        pass
    elif code == 9:
        pass
    elif code == 10:
        pass
    elif code == 11:
        pass
    elif code == 12:
        pass
    elif code == 13:
        pass
    elif code == 14:
        pass
    elif code == 15:
        pass
    elif code == 16:
        pass
    elif code == 17:
        pass
    elif code == 18:
        pass
    elif code == 19:
        pass
    elif code == 20:
        pass
    elif code == 21:
        pass
    elif code == 22:
        pass
    elif code == 23:
        pass
    elif code == 24:
        pass
    elif code == 25:
        pass
    elif code == 26:
        pass
    elif code == 27:
        pass
    elif code == 28:
        pass
    elif code == 29:
        pass
    elif code == 30:
        pass
    elif code == 31:
        pass
    elif code == 32:
        pass
    elif code == 33:
        pass
    elif code == 34:
        pass
    elif code > 999:
        ret = "Successfully added new employee. Recovery key is: " + str(code)
