"""
*   Title:            ManStaff.py
*   Project:          ManEz
*   Description:      Functions for staffs' account management. This module will
*                     be used by the frontend.
*
*   Team:             TAP2J
*
*   Last Created by: Perat Damrongsiri
*   Date Created:    26 Feb 2021
"""

import ManClass as mc
import ManDB as db

shopEmp = {}

"""
*   Function: read_emp_db
*   Description: This function reads the employee database and put it in the
*                dictionary for internal use.
*
*   Date: 8 Mar 2021
*   Created by: Perat Damrongsiri
*   Edit History: 8 Mar 2021 - Perat Damrongsiri
*                 v1.0: Created this function.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1: Bugs fixed
"""


def read_emp_db():
    # calling the database class from ManDB
    emp_database = db.EmployeesDatabase()
    emp_database.start_session()
    # read the database
    emp_list = emp_database.read_db()
    # create temporary employee for adding employees to dictionary
    temp = mc.Employee(name='temp')
    # loop through the list of employees data that receive from the database
    for emp in emp_list:
        emp_temp = temp.create(emp.name, emp.pass_hash, emp.permission, emp.recov_key)
        shopEmp[emp.name] = emp_temp

def get_emp_list():
    return shopEmp

"""
*   Function: is_emp_db_empty
*   Description: This function check that the employee database is empty or not.
*                return true if empty, else return false.
*
*   Date: 4 Mar 2021
*   Created by: Alex Villa
*   Edit History: 5 Mar 2021 - Perat Damrongsiri
*                 v1.0: Added half of the functionality.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.0.1: Finished creating the function
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1: Bugs fixed
"""


def is_emp_db_empty():
    emp_database = db.EmployeesDatabase()
    # checking if the database is exist
    if not emp_database.is_exist():
        # not exist
        ret = True
    else:
        # exist
        emp_database.start_session()
        # checking that it is empty or not
        if not emp_database.read_db():
            # empty
            ret = True
        else:
            # not empty
            ret = False
    return ret


"""
*   Function: add_employee
*   Description: This function adds employee to the dictionary and employee database.
*                return recovery key on successfully added else returns error code.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Added half of the functionality.
*                 4 Mar 2021 - Alex Villa
*                 v1.1: Linked it with employee database.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1.1: Fixed the some changes.
*                 8 Mar 2021 - Perat Damrongsiri
*                 v1.1.2: Fixed functionality issue.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1.3: Bugs fixed.
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def add_employee(name, current_user, password, firstrun=False, add_to_db=True):
    # check that name is not in the dictionary
    if name not in shopEmp:
        # check that the current user is in the dictionary
        if current_user is None or current_user in shopEmp:
            # checking the optional parameter.
            if firstrun:
                # if firstrun is true and current_user is None, it will automatically make the
                # first employee as an admin
                temp = mc.Employee(name='temp@#$', permission='admin')
                new_emp = temp.add_employee(name)
                new_emp = temp.set_to_admin(new_emp, None)
            else:
                # if not, create employee normally.
                new_emp = shopEmp[current_user].add_employee(name)

            # checking the return value from creating employee/admin
            if new_emp == 1:
                # Error #1 invalid name (string is empty)
                print("Error: ManStaff: add_employee(): Invalid name.")
                ret = 2
            elif new_emp == 2:
                # Error #2 current_user is not an admin
                print("Error: ManStaff: add_employee(): Required admin permission.")
                ret = 3
            else:
                # Successfully create
                shopEmp[name] = new_emp
                shopEmp[name].set_password(password)
                print("Successfully added new employee.")
                if add_to_db:
                    # add to database
                    emp_database = db.EmployeesDatabase()
                    emp_database.start_session()
                    emp_database.add_employee(new_emp)
                    print("Employee added to database.")
                ret = new_emp.get_key()
        else:
            print("Error: ManStaff: add_employee(): current user does not exist.")
            ret = 37
    else:
        print("Error: ManStaff: add_employee(): name is already exist.")
        ret = 36
    return ret


"""
*   Function: login
*   Description: This function handle the login action. It will set the login time.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 8 Mar 2021 - Perat Damrongsiri
*                 v1.0.1: Fixed the wrong error message.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1: Bugs fixed
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: add checking username
"""


def login(name, password):
    # check that the username is exist
    if name in shopEmp:
        # checking the password
        if shopEmp[name].checkpass(password):
            # check that is the user login already or not.
            if shopEmp[name].set_login_time():
                # successfully login
                print("ManStaff: login(): Successfully login.")
                ret = 4
            else:
                # already login
                print("ManStaff: login(): Already login.")
                ret = 5
        else:
            # wrong password
            print("ManStaff: login(): Wrong password.")
            ret = 6
    else:
        print("ManStaff: login(): Employee does not exist.")
        ret = 35
    return ret


"""
*   Function: logout
*   Description: This function handle the logout action. It will set the logout time
*                and record it to the database.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 8 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to work time database.
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: add checking username
"""


def logout(name, password):
    # check that the username is exist
    if name in shopEmp:
        # checking password
        if shopEmp[name].checkpass(password):
            res = shopEmp[name].set_logout_time()
            # check the return value from set logout time
            if res == 1:
                # successfully logout
                print("ManStaff: logout(): Successfully logout.")
                # add work time to the database using ManDB
                timedb = db.WorkTimeDatabase()
                timedb.start_session()
                timedb.checkout(shopEmp[name])
                # set login and logout time to None
                shopEmp[name].reset_time()
                ret = 7
            elif res == 2:
                # already logout
                print("ManStaff: logout(): Already logout.")
                ret = 8
            else:
                # did not login yet.
                print("ManStaff: logout(): This employee did not login yet.")
                ret = 9
        else:
            # wrong password
            print("ManStaff: logout(): Wrong password.")
            ret = 10
    else:
        print("ManStaff: logout(): Employee does not exist.")
        ret = 35
    return ret


"""
*   Function: remove_employee
*   Description: This function remove the employee from the dictionary and employee database.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to employee database.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1.1: Bugs fixed
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def remove_employee(name, current_user, password):
    # checking that thte current_user is exist
    if current_user in shopEmp:
        # checking that current user is an admin
        if shopEmp[current_user].is_admin():
            # check the admin's password
            if shopEmp[current_user].checkpass(password):
                # checking that the employee exist.
                if name in shopEmp:
                    # the employee exist
                    # delete from dictionary
                    del shopEmp[name]
                    # delete from employee database
                    emp_database = db.EmployeesDatabase()
                    emp_database.start_session()
                    emp_database.delete_employee(name)
                    print("Successfully remove employee.")
                    ret = 11
                else:
                    # the employee does not exist
                    print("Error: ManStaff: remove_employee(): This Employee does not exist.")
                    ret = 12
            else:
                # wrong password
                print("Error: ManStaff: remove_employee(): Wrong Password.")
                ret = 13
        else:
            # the current user is not an admin
            print("Error: ManStaff: remove_employee(): Require Admin Permission.")
            ret = 14
    else:
        # the current user not exist
        print("Error: ManStaff: remove_employee(): current user does not exist.")
        ret = 37
    return ret


"""
*   Function: add_admin
*   Description: This function adds the new admin into the dictionary and employee database.
*                This function only allow admin to use else it will just returns error message.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to employee database.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1.1: Bugs fixed
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def add_admin(name, current_user, new_ad_pass, curr_user_pass):
    # checking that thte current_user is exist
    if current_user in shopEmp:
        # create new employee object with admin permission
        new_admin = shopEmp[current_user].add_admin(name, curr_user_pass)
        # check the return value of add_admin
        if new_admin == 2:
            # wrong admin's password
            print("Error: ManStaff: add_admin(): Wrong Password.")
            ret = 15
        elif new_admin == 3:
            # the current_user is not an admin
            print("Error: ManStaff: add_admin(): Require Admin Permission.")
            ret = 16
        else:
            # successfully created
            new_admin.set_password(new_ad_pass)
            shopEmp[name] = new_admin
            print("Successfully added admin.")
            # add to database
            emp_database = db.EmployeesDatabase()
            emp_database.start_session()
            emp_database.add_employee(new_admin)
            print("admin added to database.")
            ret = new_admin.get_key()
    else:
        # the current user not exist
        print("Error: ManStaff: add_admin(): current user does not exist.")
        ret = 37
    return ret


"""
*   Function: promote_to_admin
*   Description: This function promotes employee to admin. Only admin can use it.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to employee database.
*                 8 Mar 2021 - Perat Damrongsiri
*                 v1.1.1: Bugs Fixed.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1.2: Bugs fixed
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def promote_to_admin(name, current_user, password):
    # checking that thte current_user is exist
    if current_user in shopEmp:
        # checking that thte name is exist
        if name in shopEmp:
            # set the employee to admin
            suc = shopEmp[current_user].set_to_admin(shopEmp[name], password)
            # check the return value of set admin
            if type(suc) == mc.Employee:
                # suc is employee
                # update the database
                emp_database = db.EmployeesDatabase()
                emp_database.start_session()
                emp_database.edit_employee(name, 'permission', 'admin')
                print("Successfully promoted.")
                ret = 18
            elif suc == 2:
                # wrong admin's password
                print("Error: ManStaff: promote_to_admin(): Wrong Password.")
                ret = 19
            elif suc == 3:
                # current_user is not an admin
                print("Error: ManStaff: promote_to_admin(): Require Admin Permission.")
                ret = 20
            elif suc == 4:
                # employee is not Employee object
                print("Error: ManStaff: promote_to_admin(): employee is not Employee object.")
                ret = 21
        else:
            # name does not exist
            print("Error: ManStaff: promote_to_admin(): name does not exist.")
            ret = 38
    else:
        # the current user not exist
        print("Error: ManStaff: promote_to_admin(): current user does not exist.")
        ret = 37
    return ret


"""
*   Function: demote_from_admin
*   Description: This function demotes admin to employee. Only admin can use it.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to employee database.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.1.1: Bugs fixed.
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def demote_from_admin(name, current_user, password):
    # checking that thte current_user is exist
    if current_user in shopEmp:
        # checking that thte name is exist
        if name in shopEmp:
            # demote admin to employee
            suc = shopEmp[current_user].demote_from_admin(shopEmp[name], password)
            # check the return value
            if suc == 1:
                # successfully demote
                # update the database
                emp_database = db.EmployeesDatabase()
                emp_database.start_session()
                emp_database.edit_employee(name, 'permission', 'emp')
                print("Successfully demoted.")
                ret = 22
            elif suc == 2:
                # wrong admin's password
                print("Error: ManStaff: demote_from_admin(): Wrong Password.")
                ret = 23
            elif suc == 3:
                # current_user is not an admin
                print("Error: ManStaff: demote_from_admin(): Require Admin Permission.")
                ret = 24
        else:
            # name does not exist
            print("Error: ManStaff: demote_from_admin(): name does not exist.")
            ret = 38
    else:
        # the current user not exist
        print("Error: ManStaff: demote_from_admin(): current user does not exist.")
        ret = 37
    return ret


"""
*   Function: change_password
*   Description: This function is for the user to change their password.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 28 Feb 2021 - Perat Damrongsiri
*                 v1.1: Update the logic and returning value to be more robust.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.2: Linked it to employee database.
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.3: added username checking.
"""


def change_password(name, old_pass, new_pass):
    # checking that thte name is exist
    if name in shopEmp:
        # call change password in ManClass
        res = shopEmp[name].change_password(old_pass, new_pass)
        # check the return value
        if res == 1:
            # successfully changes password
            # update the database
            emp_database = db.EmployeesDatabase()
            emp_database.start_session()
            emp_database.edit_employee(name, 'password', shopEmp[name].get_pass_hash())
            print("Successfully change password.")
            ret = 29
        elif res == 2:
            # invalid new password
            print("New password has to be 4 characters.")
            ret = 29
        elif res == 3:
            # invalid old password
            print("Invalid Password (Previous Password does not match).")
            ret = 31
    else:
        # name does not exist
        print("Error: ManStaff: demote_from_admin(): name does not exist.")
        ret = 38
    return ret


"""
*   Function: forgot_password
*   Description: This function is for the user to change their password when they
*                forgot it.
*
*   Date: 27 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 27 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Linked it to employee database.
*                 11 Mar 2021 - Perat Damrongsiri
*                 v1.2: added username checking.
"""


def forgot_password(name, key, new_pass):
    # checking that thte name is exist
    if name in shopEmp:
        if len(new_pass) != 4:
            # invalid new password
            print("New password has to be 4 characters.")
            ret = 32
        elif shopEmp[name].forgot_password(key, new_pass):
            # successfully reset password
            # update the database
            emp_database = db.EmployeesDatabase()
            emp_database.start_session()
            emp_database.edit_employee(name, 'password', shopEmp[name].get_pass_hash())
            print("Successfully change password.")
            ret = 33
        else:
            # wrong recovery key
            print("Error: ManStaff: forgot_password(): Wrong recovery key.")
            ret = 34
    else:
        # name does not exist
        print("Error: ManStaff: demote_from_admin(): name does not exist.")
        ret = 38
    return ret


"""
*   Function: is_admin
*   Description: This function check that the <name> is an admin or not
*
*   Date: 11 Mar 2021
*   Created by: Perat Damrongsiri
*   Edit History: 11 Mar 2021 - Perat Damrongsiri
*                 v1.0: Created.
"""


def is_admin(name):
    # check that the name is exist
    if name in shopEmp:
        ret = shopEmp[name].is_admin()
    else:
        ret = False
    return ret


"""
*   Function: admin_entry
*   Description: This function checks that the user is admin and verifying the password.
*
*   Date: 11 Mar 2021
*   Created by: Perat Damrongsiri
*   Edit History: 11 Mar 2021 - Perat Damrongsiri
*                 v1.0: Created.
"""


def admin_entry(name, password):
    # check that the name is exist
    if name in shopEmp:
        if shopEmp[name].is_admin():
            # is admin
            if shopEmp[name].checkpass(password):
                # correct password
                print("Successfully enter.")
                ret = 39
            else:
                # wrong password
                print("Error: ManStaff: admin_entry(): wrong password.")
                ret = 19
        else:
            # not an admin
            print("Error: ManStaff: admin_entry(): not an admin.")
            ret = 40
    else:
        # name does not exist
        print("Error: ManStaff: admin_entry(): name does not exist.")
        ret = 38
    return ret


"""
*   Function: get_message
*   Description: This function will convert the error code to error message, and
*                boolean to indicate that it's error or success.
*
*   Date: 28 Feb 2021
*   Created by: Perat Damrongsiri
*   Edit History: 28 Feb 2021 - Perat Damrongsiri
*                 v1.0: Created.
*                 6 Mar 2021 - Perat Damrongsiri
*                 v1.1: Added the message and boolean that are needed to return.
*                 10 Mar 2021 - Perat Damrongsiri
*                 v1.2: Fixed some message.
"""


def get_message(code):
    # check the code
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
    elif code == 35:
        ret = "Username does not exist.", False
    elif code == 36:
        ret = "Username is already exist.", False
    elif code == 37:
        ret = "current user does not exist.", False
    elif code == 38:
        ret = "name does not exist.", False
    elif code == 39:
        ret = "Successfully enter.", True
    elif code == 40:
        ret = "not an admin.", False
    elif code > 999:
        ret = ("Successfully added new admin/employee. Recovery key is: " + str(code)), True
    return ret
