# CookieClicker
A Selenium automation project that automatically clicks the cookie in the Cookie Clicker game.
Cookie Clicker Bot

A Python automation script that plays Cookie Clicker automatically using Selenium WebDriver.
Description

This script:

    Opens the Chrome browser.

    Navigates to Cookie Clicker.

    Selects English as the language.

    Continuously clicks the big cookie to collect cookies.

    Prints the current cookie count to the console.

Requirements

    Python 3.7+

    selenium package

    webdriver_manager package

    Google Chrome browser installed

Installation

Install the required libraries:

pip install selenium webdriver-manager

How to Run

    Save the script as cookie_clicker_bot.py.

    Open a terminal or command prompt in the folder containing the file.

    Run the script:

python cookie_clicker_bot.py

What the Script Does

    Automatically opens the Cookie Clicker website.

    Waits for the language selection to appear and chooses English.

    Finds the big cookie element (bigCookie).

    Starts clicking the cookie extremely fast in an infinite loop.

    Continuously prints the number of cookies collected.

Notes

    The loop is infinite (while True), so you'll need to manually stop the script (CTRL+C or stop it from the terminal).

    The time.sleep(0.0000001) slightly delays the clicks but keeps them extremely fast.

    Make sure your ChromeDriver version matches your installed Chrome browser version — this is handled automatically using webdriver_manager.

Credits

    Based on Cookie Clicker.

    Automation by Selenium
pip install -r requirements.txt
