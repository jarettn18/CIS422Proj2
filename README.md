# CIS422Proj2 -ManEZ

## Introduction
    Point of Sale system
    Current Point of Sale system is overcomplicated and expensive for business owner ex) restaurant, warehouse
    Easeir and more efficient program for new users.

## User Guide
## Documentation
    Python files that we used and funtions in each file.
#### ManUI.py
    UI
#### ManCus.py
    add_item() : add new data into the list
    query_item() : add new data into the list
    add_order() : add order
    edit_item() : Selection of food options(add-ons) and set discount rate
    edit_order() : edit order data
    delete_menu() : delete menu from list
    delete_order() : delete order from list
    show_item() : present current items
    show_order() : present current orders
    get_total() : calculate total
    pay_order() : Send order data to DB

#### ManClass.py
    Class for item
    
      Class variables
          name: order’s name
          category: order’s category	
          price: order’s price
          discount: menu’s discount
        
      Getter and Setter for each class
          get_name(): get order’s name
          get_category(): get order’s category	
          get_price(): get order’s price
          get_discount(): get discount rate
          set_name(): set order’s name
          set_category(): set order’s category	
          set_price(): set order’s price
          set_discount(): set discount rate
         
    Class for order
    
        Class Variable
            item: name of item
            amount: amount of order
        
       Getter and Setter for receipt class
             get_item(): get item name
             get_amount(): get amount of item
             set_item(): set item name
             set_item(): set amount of item
    
    Class for receipt
    
        Class Variable
              customer_name: Name of Customers
              orders: list of orders
              total: total price
              discount: discount rate that is applied
        Getter and Setter for receipt class
              get_customer_name(): get customer’s name
              get_orders(): get orders list
              get_total(): get total cost
              get_discount(): get discount rate
              set_customer_name(): set customer’s name	
              set_orders(): set orders list
              Set_total(): set total cost
              Set_discount(): set discount rate
        
    Class for Employee
    
        Class Variable
            _name: name of the employee
            _password_hash: security hash for the employee
            _login_time: login time of the employee
            _logout_time: logout time of the employee
            _recovery_key: key to recover the employee account
        
        Getter and Setter for receipt class
             create(): create employee account
             is_admin(): check whether the current user is administer
             set_login_time(): set the log in time in real time
             set_logout_time(): set the log out time in real time
             set_password(): set the password
             set_recovery_key(): set the recovery key for recovering password
             change_password(): change password
             forgot_password(): set the new password with the user recovery key
             get_login_time(): get the saved log in time
             get_logout_time(): get the saved log out time
             get_name(): get the name of the user
             set_to_admin(): set the user as an administer
             add_employee(): add new employee
             add_admin(): add new administer
             demote_from_admin(): demote current user from administer
             checkpass(): check whether the input password is valid
             get_key(): get the recovery key
             get_permission(): get the user permission
             get_pass_hash(): get the user password hash
             reset_time(): reset the log time data of the current user

#### ManStaff.py
#### ManDB.py

    Item database
        add_item(): add item into the database 
        delete_item(): delete item from the database
        edit_item(): edit item in the database
        read_db(): read database
        
    Receipt database
        add_receipt(): add receipt to the database
        delete_receipt(): delete a receipt from the database
        get_period(): get receipts from input start date to end date
        
    WorkTime database
        checkout(): check out the employee and save the log info to the database for the analysis
        
    Employees database
        add_employee(): add employee data into the database
        delete_employee(): delete employee data into the database
        edit_employee(): edit employee data from the database
        is_exist(): check if employee exists in the database
        is_empty(): check whether the employee database is empty or not
        read_db(): read database
