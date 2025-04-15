class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = '#user-name'
        self.password_input = '#password'
        self.login_button = '#login-button'
        self.error_message = '[data-test="error"]'

    def navigate(self):
        self.page.goto('https://www.saucedemo.com')

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.error_message)

    def is_on_login_page(self):
        return self.page.is_visible(self.login_button)
        
    def get_current_url(self):
        return self.page.url 