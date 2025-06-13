# Playwright Pytest Automation

A simple Playwright test suite using Pytest to automate UI testing on the web page.

---

## Project Structure

- `test_automation.py` — Test cases
- `test_product_data.py` — Test cases
- `conftest.py` — Fixtures and setup for WebDriver
- `screenshots/` — Saved screenshots from failed tests
- `reports/report.html` — Test execution report (generated automatically)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/hemanth-kumar-j/playwright-pytest.git
cd playwright-pytest
```

### 2. Install Rye (if not already installed)
Visit [https://rye-up.com](https://rye-up.com) for installation instructions.

### 3. Set Up the Environment
```bash
rye sync
```

### 4. Run Tests (Headless Chromium by Default)
```bash
pytest
```

### 5. Run Tests with Parallel Execution
```bash
pytest -n 3
pytest --browser webkit -n 2
```

### 6. Run Tests with Browser UI (Headed Mode)
```bash
pytest --headed
```

### 7. Run Tests with Other Browsers
```bash
pytest --browser firefox
pytest --browser webkit
```

### 8. Run Tests with Parallel Execution In Parallel Browsers
```bash
pytest --browser chromium --browser webkit -n 2
pytest --browser chromium --browser firefox --browser webkit -n 3
```

### 9. View Test Report
Open `reports/report.html` in your browser.

---

## Notes

- Failing tests will save screenshots in the `screenshots/` folder.
- Code is auto-formatted using `black`.

---
