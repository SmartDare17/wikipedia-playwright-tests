
from urllib.parse import urlparse
from pages.home_page import WikipediaHomePage
from pages.article_page import WikipediaArticlePage
from playwright.sync_api import expect

# 1) Basic search → assert heading
def test_search_python_language(page):
    home = WikipediaHomePage(page).open()
    home.search("Python (programming language)")

    article = WikipediaArticlePage(page)
    article.expect_loaded()

    heading = article.get_heading_text()
    assert "Python" in heading, f"Expected heading to contain 'Python', got {heading}"

# 2) Sidebar exists on article pages
def test_sidebar_exists(page):
    home = WikipediaHomePage(page).open()
    home.search("Software testing")

    article = WikipediaArticlePage(page)
    article.expect_loaded()
    assert article.sidebar.is_visible(), "Sidebar navigation should be visible"

# 3) Refine search changes article
def test_refine_search(page):
    home = WikipediaHomePage(page).open()
    home.search("Manual testing")

    article = WikipediaArticlePage(page)
    article.expect_loaded()
    first_heading = article.get_heading_text()

    article.refine_search("Automation testing")
    article.expect_loaded()
    second_heading = article.get_heading_text()

    assert first_heading != second_heading, "Expected heading to change after refining search"

# 4) Language switch from home (Español)
def test_language_switch_to_spanish(page):
    home = WikipediaHomePage(page).open()
    # Click Español language tile
    page.get_by_role("link", name="Español").click()
    # Assert URL contains /es/
    expect(page).to_have_url(lambda url: "/es/" in url)
    # Main page heading in Spanish should be visible
    main_heading = page.locator("#firstHeading")
    expect(main_heading).to_be_visible()

# 5) Table of contents is present on longer articles
def test_table_of_contents_present(page):
    home = WikipediaHomePage(page).open()
    home.search("Software testing")

    article = WikipediaArticlePage(page)
    article.expect_loaded()

    toc = page.locator("#toc")
    expect(toc).to_be_visible()
    # At least a few TOC items
    assert page.locator("#toc li").count() >= 3, "Expected at least 3 items in TOC"

# 6) Search suggestions appear when typing (without submitting)
def test_search_suggestions_dropdown(page):
    home = WikipediaHomePage(page).open()
    search_box = page.locator("input[name='search']")
    search_box.fill("Selenium")
    # Wikipedia suggestions container is 'div.suggestions' with links inside
    suggestions = page.locator("div.suggestions")
    expect(suggestions).to_be_visible()

# 7) Internal navigation: click link from Python article to Guido van Rossum
def test_internal_link_navigation(page):
    home = WikipediaHomePage(page).open()
    home.search("Python (programming language)")

    article = WikipediaArticlePage(page)
    article.expect_loaded()

    # Try to click the Guido van Rossum link if present
    link = page.get_by_role("link", name=lambda n: n and "Guido van Rossum" in n)
    if link.count() == 0:
        # Fallback: click first link in infobox
        link = page.locator(".infobox a").first()
    old_heading = article.get_heading_text()
    link.first.click()

    article.expect_loaded()
    new_heading = article.get_heading_text()
    assert new_heading and new_heading != old_heading, "Heading should change after internal navigation"

# 8) Infobox exists on Python article
def test_infobox_present(page):
    home = WikipediaHomePage(page).open()
    home.search("Python (programming language)")
    article = WikipediaArticlePage(page)
    article.expect_loaded()

    infobox = page.locator(".infobox")
    expect(infobox).to_be_visible()

# 9) First paragraph exists and has text
def test_first_paragraph_has_text(page):
    home = WikipediaHomePage(page).open()
    home.search("Software testing")
    article = WikipediaArticlePage(page)
    article.expect_loaded()

    first_paragraph = page.locator("div.mw-parser-output > p").first
    expect(first_paragraph).to_be_visible()
    text = first_paragraph.text_content() or ""
    assert len(text.strip()) > 0, "Expected first paragraph to contain text"

# 10) Confirm canonical article URL contains slug
def test_article_url_contains_slug(page):
    home = WikipediaHomePage(page).open()
    home.search("Python (programming language)")
    article = WikipediaArticlePage(page)
    article.expect_loaded()

    current_url = page.url
    assert "/wiki/Python_(programming_language)" in current_url, f"Unexpected URL: {current_url}"
