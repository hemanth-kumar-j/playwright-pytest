# Playwright Pytest Automation

A simple Playwright test suite using Pytest to automate UI testing on the web page.
Supports multiple browsers, parallel execution, screenshots on failure, and HTML reports.

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
Rye is a modern Python packaging tool for managing dependencies and virtual environments.
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

### 7. Run Tests in Specific Browsers
```bash
pytest --browser firefox
pytest --browser webkit
```

### 8. Run Tests Sequentially in Multiple Browsers
```bash
pytest --browser chromium --browser firefox --browser webkit
pytest --browser firefox --browser chromium
```

### 9. Run Tests in Parallel Across Multiple Browsers
```bash
pytest --browser chromium --browser webkit -n 2
pytest --browser chromium --browser firefox --browser webkit -n 3
```

### 10. Clean Old Screenshots Before Running Tests
```bash
pytest --remove
```

### 11. View Test Report
Open `reports/report.html` in your browser.

---

## Snapshot Testing

This project uses **pytest-playwright-snapshot** for visual regression testing.
Snapshots (baseline images) are stored inside the `__snapshots__` directory.

### Updating Baseline Images
Run tests with the `--snapshot-update` flag to update baseline images:

```bash
pytest --snapshot-update
```
This will replace the old baseline with the new screenshot.

### Manual Updates

You can also manually replace images inside the __snapshots__ directory.

Just drop your updated image with the same name as the existing baseline.

### Troubleshooting

If tests fail due to small rendering differences, run with --snapshot-update to regenerate baselines.

Make sure your test environment (browser, OS, resolution) is consistent to avoid false mismatches.

If snapshots keep failing, delete the corresponding image in __snapshots__ and rerun with --snapshot-update.

---

## Notes

- Failed tests automatically save screenshots in the `screenshots/` folder.
- Reports are generated using pytest-html and stored in reports/report.html.
- Code is auto-formatted using `black`.

---

## Tech Stack

- Python
- Pytest
- Playwright
- Rye
- Black

---
