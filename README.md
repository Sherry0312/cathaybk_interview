# cathaybk_interview

This is the Cathay Bank interview coding test.  
Including two files:

1. Program Logic
  - Rules for judging input numbers
  - Caculate the strings amount in the text
  
---  
  
2. Automation_assignment
  - page_object file
    - action_untils.py  
      To save the common method (e.g. find clickable element, save the screen shot).
    
    - creditcard_page.py  
    To save the element locators and the action method (e.g. click the element, check the element display status).
    
  - test_web file
    - conftest.py  
    Set the pytest fixture to create the Chrome driver.
    
    - test_credit_cart_page.py  
    Steps to perform the test case
    
  - Screenshot file  
  Store the screenshots in the execution process.
    
  - pytest.ini  
  To definition the log and pytest info.
