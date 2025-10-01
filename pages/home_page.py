from playwright.sync_api import Page, expect

class WikipediaHomePage:
    URL = "https://www.wikipedia.org/"

    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator("input[name='search']")

    def open(self):
        self.page.goto(self.URL)
        expect(self.search_box).to_be_visible()
        return self

    def search(self, query: str):
        self.search_box.fill(query)
        self.search_box.press("Enter")
