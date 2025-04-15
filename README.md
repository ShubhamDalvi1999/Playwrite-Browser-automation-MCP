# Playwright Python Framework

This project contains automated tests for the Sauce Demo website using Playwright with Python.

## Project Structure

```
playwright-python-framework/
|--requirements.txt
|--pages/
|    |--__init__.py
|    |--login_page.py
|--tests/
|    |--test_login.py
|    |--pytest.ini
|    |--conftest.py
|--README.md
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
python -m playwright install
```

## Running Tests

To run all tests:

```bash
pytest
```

To run with verbose output:

```bash
pytest -v
```

To run with a specific browser:

```bash
pytest --browser-name=firefox
```

Available browser options:
- chromium (default)
- firefox
- webkit

To run a specific test:

```bash
pytest tests/test_login.py::test_valid_login -v
```

## Test Scenarios

The framework currently includes the following test scenarios:

1. **Valid Login Test**
   - Navigates to the login page
   - Logs in with valid credentials (standard_user)
   - Verifies successful redirection to inventory page
   - Verifies login form is no longer visible

2. **Locked Out User Test**
   - Navigates to the login page
   - Attempts to log in with locked_out_user credentials
   - Verifies user remains on login page
   - Verifies appropriate error message is displayed

## Page Object Model

This framework uses the Page Object Model design pattern:
- `login_page.py` - Contains methods and selectors for the login page
- Tests interact with pages through these objects rather than directly with UI elements

## Technologies Used

- Playwright - Browser automation library
- pytest - Testing framework
- pytest-playwright - Pytest plugin for Playwright integration
