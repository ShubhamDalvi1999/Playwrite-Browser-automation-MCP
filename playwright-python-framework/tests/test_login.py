import pytest


def test_valid_login(login_page):
    # Navigate to the login page
    login_page.navigate()
    
    # Perform login with valid credentials
    login_page.login('standard_user', 'secret_sauce')
    
    # Verify successful login
    assert 'inventory.html' in login_page.get_current_url(), 'User was not redirected to inventory page'
    assert not login_page.is_on_login_page(), 'Login form is still visible after login'

def test_locked_out_user(login_page):
    # Navigate to the login page
    login_page.navigate()
    
    # Perform login with locked out user
    login_page.login('locked_out_user', 'secret_sauce')
    
    # Verify error message and that user remained on login page
    assert login_page.is_on_login_page(), 'User was redirected from login page'
    error_message = login_page.get_error_message()
    assert 'Sorry, this user has been locked out' in error_message, f'Expected locked out error message, got: {error_message}' 