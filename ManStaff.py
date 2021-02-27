import ManClass

shopEmp = {}

def add_employee(name, current_user, firstrun=False, add_to_db=True):
    if name:
        if firstrun:
            position = 'admin'
        else:
            position = 'emp'

        new_emp = shopEmp[current_user].add_employee(name)
        if new_emp:
            shopEmp[name] = new_emp
            ret = new_emp.get_key()
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
