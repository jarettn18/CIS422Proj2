import ManClass as mc
import ManDB as db

shopEmp = {}

def read_emp_db():
    emp_database = db.EmployeesDatabase()
    emp_database.start_session()
    emp_list = emp_database.read_db()
    for emp in emp_list:
        temp = mc.Employee(name='temp')
        emp_temp = temp.create(emp.name, emp.pass_hash, emp.permission, emp.recov_key)
        shopEmp[emp.name] = emp_temp
    del shopEmp['temp']

def is_emp_db_empty():
    emp_database = db.EmployeesDatabase()
    if emp_database.is_exist() and not emp_database.is_empty():
        ret = False
    else:
        ret = True
    return ret

def add_employee(name, current_user, password, permission='emp', firstrun=False, add_to_db=True):
    if firstrun:
        position = 'admin'
    else:
        position = 'emp'

    new_emp = shopEmp[current_user].add_employee(name)
    if new_emp == 1:
        print("Error: ManStaff: add_employee(): Invalid name.")
        ret = 2
    elif new_emp == 2:
        print("Error: ManStaff: add_employee(): Required admin permission.")
        ret = 3
    else:
        shopEmp[name] = new_emp
        print("Successfully added new employee.")
        if add_to_db:
            emp_database = db.EmployeesDatabase()
            emp_database.start_session()
            emp_database.add_employee(new_emp)
            print("Employee added to database.")
        ret = new_emp.get_key()
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
            timedb = db.WorkTimeDatabase()
            timedb.start_session()
            timedb.checkout(shopEmp[name])
            shopEmp[name].reset_time()
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
                emp_database = db.EmployeesDatabase()
                emp_database.start_session()
                emp_database.delete_employee(name)
                print("Successfully remove employee.")
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
        emp_database = db.EmployeesDatabase()
        emp_database.start_session()
        emp_database.edit_employee(name, 'permission', 'admin')
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
        emp_database = db.EmployeesDatabase()
        emp_database.start_session()
        emp_database.edit_employee(name, 'permission', 'emp')
        print("Successfully demoted.")
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
        emp_database = db.EmployeesDatabase()
        emp_database.start_session()
        emp_database.edit_employee(name, 'password', shopEmp[name].get_pass_hash())
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
        emp_database = db.EmployeesDatabase()
        emp_database.start_session()
        emp_database.edit_employee(name, 'password', shopEmp[name].get_pass_hash())
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
        emp_database = db.EmployeesDatabase()
        emp_database.start_session()
        emp_database.edit_employee(name, 'password', shopEmp[name].get_pass_hash())
        print("Successfully change password.")
        ret = 33
    else:
        print("Error: ManStaff: forgot_password(): Wrong recovery key.")
        ret = 34
    return ret

def get_message(code):
    if code == 2:
        ret = "Invalid name.", False
    elif code == 3:
        ret = "Required admin permission.", False
    elif code == 4:
        ret = "Successfully login.", True
    elif code == 5:
        ret = "Already login.", False
    elif code == 6:
        ret = "Wrong password.", False
    elif code == 7:
        ret = "Successfully logout.", True
    elif code == 8:
        ret = "Already logout.", False
    elif code == 9:
        ret = "This employee did not login yet.", False
    elif code == 10:
        ret = "Wrong password.", False
    elif code == 11:
        ret = "Successfully remove employee.", True
    elif code == 12:
        ret = "This Employee does not exist.", False
    elif code == 13:
        ret = "Wrong Password.", False
    elif code == 14:
        ret = "Require Admin Permission.", False
    elif code == 15:
        ret = "Wrong Password.", False
    elif code == 16:
        ret = "Require Admin Permission.", False
    elif code == 17:
        ret = "Successfully added admin.", True
    elif code == 18:
        ret = "Successfully promoted.", True
    elif code == 19:
        ret = "Wrong Password.", False
    elif code == 20:
        ret = "Require Admin Permission.", False
    elif code == 21:
        ret = "employee is not Employee object.", False
    elif code == 22:
        ret = "Successfully demoted.", True
    elif code == 23:
        ret = "Wrong Password.", False
    elif code == 24:
        ret = "Require Admin Permission.", False
    elif code == 25:
        ret = "employee is not Employee object.", False
    elif code == 26:
        ret = "Successfully set password.", True
    elif code == 27:
        ret = "password has to be 4 characters.", False
    elif code == 28:
        ret = "Trying to pass this wall?? no way!!!", False
    elif code == 29:
        ret = "Successfully change password.", True
    elif code == 30:
        ret = "New password has to be 4 characters.", False
    elif code == 31:
        ret = "Invalid Password (Previous Password does not match).", False
    elif code == 32:
        ret = "New password has to be 4 characters.", False
    elif code == 33:
        ret = "Successfully change password.", True
    elif code == 34:
        ret = "Wrong recovery key.", False
    elif code > 999:
        ret = ("Successfully added new employee. Recovery key is: " + str(code)), True
