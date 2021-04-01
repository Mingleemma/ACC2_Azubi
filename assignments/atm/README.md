# ATM Flow
## 1. display welcome and allow use to enter username
## 2. Prompt user to enter pin
    a. if fails, display incorrect pin and number of attempts left(max 3)
        - if continues to fail, log them out
    b. if passes, continue down
## 3. Ask whether user wants to:
 #### a. Withdraw money
    - ask user to select the currency to withdraw
    - ask user to enter amount to withdraw (do not allow above max balance)
    - withdraw and update the account accordingly
    - ask whether receipt must be printed
        * if yes then print receipt, if not print nothing
    - generate transaction ID and log transaction
    - ask to perform another transaction
        * if yes, go back to 3, if not then log out
#### b. check balance
    - display balance for all currencies available
    - ask whether receipt must be printed
        * if yes then print receipt, if not print nothing
    - generate transaction ID and log transaction
    - ask to perform another transaction
        * if yes, go back to 3, if not then log out
#### c. change pin
    - tell user to enter old pin
    - tell user to enter new pin
    - tell user to confirm new pin
    - update the new pin on the user
    - generate transaction ID and log transaction
    - ask to perform another transaction
        * if yes, go back to 3, if not then log out
#### d. view statements
    - display list of past transactions for logged in user 