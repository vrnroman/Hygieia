
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("http://localhost:5173")

            # Verify title
            expect(page).to_have_title("road-rules-tutor")

            # Verify content
            expect(page.get_by_text("Road Rules Tutor")).to_be_visible()
            expect(page.get_by_text("Hello World")).to_be_visible()

            page.screenshot(path="verification/hello_world.png")
            print("Screenshot taken successfully")

        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="verification/error.png")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
