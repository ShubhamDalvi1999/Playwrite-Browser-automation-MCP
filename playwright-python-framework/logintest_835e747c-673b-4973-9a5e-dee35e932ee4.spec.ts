
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('LoginTest_2025-04-15', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('#user-name', 'standard_user');

    // Fill input field
    await page.fill('#password', 'secret_sauce');

    // Click element
    await page.click('#login-button');

    // Navigate to URL
    await page.goto('https://www.saucedemo.com');

    // Fill input field
    await page.fill('#user-name', 'locked_out_user');

    // Fill input field
    await page.fill('#password', 'secret_sauce');

    // Click element
    await page.click('#login-button');
});