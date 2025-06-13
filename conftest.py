import os
import base64
import pytest
import pytest_html
from playwright.sync_api import Browser, Page
from pytest_metadata.plugin import metadata_key


@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "playwright_pytest"

    # Ensure the screenshots folder exists
    os.makedirs("screenshots", exist_ok=True)


def pytest_html_report_title(report):
    report.title = "Automation Report"


# This hook adds screenshots and page URL to the HTML report on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute other hooks to get the report object
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            page = item.funcargs.get("page", None)
            if page:
                # Save screenshot
                screenshot_path = os.path.join("screenshots", f"{item.name}.png")
                page.screenshot(path=screenshot_path, full_page=True)

                # Read and encode the image in base64
                with open(screenshot_path, "rb") as f:
                    encoded_image = base64.b64encode(f.read()).decode()

                # Embed screenshot into report using base64
                html_img = f'<div><img src="data:image/png;base64,{encoded_image}" alt="screenshot" style="max-width:600px; max-height:400px;" /></div>'
                extras.append(pytest_html.extras.html(html_img))

                # Optionally add the page URL
                extras.append(pytest_html.extras.url(page.url))

        report.extras = extras
