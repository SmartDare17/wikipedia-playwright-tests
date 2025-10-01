# Wikipedia.org E2E Tests (Playwright + Python)

This project demonstrates a clean Page Object Model (POM) setup using **pytest** and **Playwright**.
It automates basic Wikipedia workflows:

- Search for articles (e.g., "Python (programming language)")
- Validate article headings
- Check for sidebar navigation
- Refine searches and verify different results

## Tech
- Python 3.x
- Playwright (sync API)
- Pytest with Page Object Model (POM)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Run Tests
```bash
pytest
```

Debug with headed browser:
```bash
pytest --headed
```

Enable tracing:
```bash
pytest --tracing=on
playwright show-trace test-results/**/trace.zip
```



---

## Author
👤 **Smart Dare**
QA Engineer | Software Tester 
