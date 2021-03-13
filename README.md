# Welcome to EZ Point of Sale system ManEZ!

    *   Title: ReadME.md
    *   Project: ManEz
    *   Team: TAP2J
    *   Course Name: CIS 422
    *   Assignment: Project 2
    *   Description: ReadME file of our proejct
    *   Date: 11 March 2021
    *   Last Created by: Theodore Yun
    *   Edit History: 11 Mar 2021 - Theodore Yun
                      v1.0: First create file
                      v1.1: Finalize readme
                  
 
## Introduction
    Point of Sale system
    Current Point of Sale system is overcomplicated and expensive for business owner ex) restaurant, warehouse
    Easeir and more efficient program for new users.

## Authors
    Perat Damronsiri, Jarett Nishijo, Jay Shin, Alex Villa, Theodore Yun

## How to use
    Refer to ManEZ_Software_Guide for installation and user guide of our program

## Modules - Python files that we used and functions in each file.
    
#### ManUI.py
    Class: App
        reset() : Clear the screen of all current widgets
        init_screen() : initial screen brought up upon installation
        main_login_screen() : main screen brought up upon future program launches
        pin_screen() : pin screen to validate all screens requiring a pin
        settings_menu() : settings menu screen
        New_account() : new account screen used to add new accounts to database
        create_account() : insert the account name into database
        add_menu() : screen to add new menus to database
        order_screen() : brings up a UI for new orders
        analysis() : brings up screen used for analyzing sale data
        emp_analysis() : brings up screen used for analyzing employee data

    Class: ShowEmpData
        Show_employees() : bring a list of employees
        show_work_hours() : bring a list of hours worked for each employee
        show_time_options() : style dates according to options

    Class: ShowSaleData
        _calcTotalPeriod() : calculate the total sales for the given period
        _calcTotalDay() : calculate the total sales for the day
        _calcTotal() : calculate the total for a given collection
        findBySale() : find a receipt by sale date
        findByCategory() : find a receipt by category
        findByItem() : find a receipt by item

    Class: UpdatingCategories
        insert_item() : add an item to a category
        update_cat_list() : update a category list
        show_cat_list() : show category list
        create_category() : create a category
        create_item() : create an item for a category
        toggle_item() : turn on and off visibility of items

    Class: DynamicMenu
        get_send_button() : get the send button
        show_cat_list() : show the category list
        create_items() : create an item for menu
        insert_item() : insert an item to a menu
        delete_item() : delete an item from a menu
        _delete_order_grid() : delete the order grid
        delete_order_grid() : reset the widgets in the order grid
        delete_whole_order() : delete an order
        send_order() : send order to database
    
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
        
#### ManReport.py
      get_sale_list() : obtain sales data from the input start date to end date
      total_sale_by_date() : obtain total sales amount from the input start date to end date
      total_profit_by_date() : obtain total sales profit from the input start date to end date
      report_by_item() : get report by item (coke: 5)
      report_by_category() : get report by category(drink:5)
      daily_worktime_report() : get daily work time report during the input date period
      total_worktime_report() : get total work time during the input period
      pay_employee() : calculate the employee payment during the input period
