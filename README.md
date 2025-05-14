# 🍪 Cookie Clicker Bot

A powerful **Python + Selenium** automation bot that plays [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) for you — clicking the big cookie endlessly and logging your cookie count in real-time.

---

## 🚀 Features

- Opens **Chrome** browser automatically
- Selects **English** as the game language
- Finds and clicks the **big cookie** continuously
- Logs your current cookie count to the terminal
- Uses `webdriver-manager` to manage ChromeDriver — **no manual setup needed!**

---

## 🖥️ Prerequisites

- Python **3.7+**
- Google Chrome browser installed
- Internet connection (for `webdriver-manager` to download driver)

---

## 📦 Installation

1. Clone this repository or download the project files.
2. Install required Python packages using:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install selenium webdriver-manager
```

---

## ▶️ How to Run

Run the script with:

```bash
python main.py
```

It will:

- Launch Chrome
- Open the Cookie Clicker website
- Select English
- Start clicking the cookie at **ultra-fast speed**
- Print your cookie count to the terminal continuously

---

## 🧠 How It Works

```python
driver.get("https://orteil.dashnet.org/cookieclicker/")
```

- Navigates to the game site.

```python
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()
```

- Selects English as the language.

```python
cookie = driver.find_element(By.ID, "bigCookie")
```

- Locates the big cookie.

```python
while True:
    time.sleep(0.0000001)
    cookie.click()
    ...
```

- Continuously clicks and prints the number of cookies collected.

---

## ⚠️ Notes

- The loop is **infinite**, so use `CTRL+C` to stop the script manually.
- The line `time.sleep(0.0000001)` introduces a minimal delay to avoid CPU overload.
- You don’t need to manually download ChromeDriver — it’s managed by `webdriver-manager`.

---

## 📁 Project Structure

```
cookie-clicker-bot/
├── main.py               # The automation script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🧪 Testing Ideas (Not Included)

Although this project doesn't include testing, here are ideas for expanding it:

- Verify cookie counter increases after clicks
- Track click rate and success per second
- Use `pytest` + `selenium` in headless mode for testing logic

---

## 👩‍💻 Author

Developed with ❤️ for fun, learning, and automation practice.

---

## 🏷 Tags

`#selenium` `#automation` `#cookieclicker` `#python` `#bot` `#qa`

