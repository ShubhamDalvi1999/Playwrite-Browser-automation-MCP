Use the Playwright MCP Server to navigate to the website https://ww.saucedemo.com. Ensure that the MCP Server is actively handling the browser automation to validate its integration. Do not simulate the tests statically or bypass the MCP Server. All interactions must be routed through MCP.

On the login page, execute the following two scenarios:

Scenario 1: Valid Login

Click the Login button.
Verify that:
The user is redirected to /inventory.html.
No error message is displayed.
The login form is no longer visible.
The inventory page is displayed successfuly.
Scenario 2: Locked Out User

Enter the username as "locked_out _user" and the password as "secret _sauce".
Click the Login button.
Verify that:
The user remains on the login page.
The login form is still visible.
The following error message is displayed:
"Epic sadface: Sorry, this user has been locked out."
 After both scenarios are validated:

 Close the browser.
At the same time Generate Python code using Playwright with MCP integration to execute the above scenarios.


Once you have the code gen thru the MCP server, and use the code generated. Organize the project inside a parent folder named playwright-python-framework.
The folder structure must follow this format:

playwright-python-framework/
|--requirements. txt
|—-pages
|    |--init_.py
|    |--todo_page.py
|--tests/
|  |-—test_login.py
|  |--pytest. ini
|  |--conftest-py
|-- README. md


Use pytest as the test runner. Save all files and dependencies inside playwright-python-framework only. Do not place any files in the root directory. Also, use the page object model to store the URL, locators/attributes, and actions of the login page.