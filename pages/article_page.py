# pages/article_page.py
from playwright.sync_api import Page, expect

class WikipediaArticlePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator("#firstHeading")
        self.sidebar = page.locator("#mw-panel")
        # Use the unique header search box instead of the generic "input[name='search']"
        self.search_box_header = page.locator("#searchInput")  
        self.search_box_sticky = page.locator("#vector-sticky-search-form input[name='search']")
        self.main_menu_button = page.get_by_role("button", name="Main menu")

    def expect_loaded(self):
        expect(self.heading).to_be_visible()

    def get_heading_text(self) -> str:
        return self.heading.text_content() or ""

    def refine_search(self, new_query: str):
        # Prefer the header search input if visible; else use sticky
        if self.search_box_header.is_visible():
            box = self.search_box_header
        else:
            box = self.search_box_sticky

        expect(box).to_be_visible()
        box.fill(new_query)
        box.press("Enter")
