from playwright.sync_api import Page, expect

class WikipediaArticlePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator("#firstHeading")
        self.sidebar = page.locator("#mw-panel")
        self.search_box_top = page.locator("input[name='search']")

    def expect_loaded(self):
        expect(self.heading).to_be_visible()

    def get_heading_text(self) -> str:
        return self.heading.text_content() or ""

    def refine_search(self, new_query: str):
        self.search_box_top.fill(new_query)
        self.search_box_top.press("Enter")
