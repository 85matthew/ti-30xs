# TI-30XS MultiView Calculator Simulator

A standalone, embeddable web application that recreates the TI-30XS MultiView scientific calculator.

## Features

- **Scientific Functions:** sin, cos, tan, log, ln, and more.
- **2nd Function Key:** Access inverse trig, square root, and other secondary functions.
- **Angle Modes:** Toggle between Degree (DEG) and Radian (RAD).
- **History:** Multi-line display showing previous calculations. Click on any history item to recall the expression.
- **Keyboard Support:** Operate the calculator using your physical keyboard.
- **Standalone:** Self-contained in `index.html`.

## How to Use

Simply open `index.html` in any modern web browser.

### Embedding

To embed this calculator in your website, use the following iframe code:

```html
<iframe src="path/to/index.html" width="350" height="600" frameborder="0"></iframe>
```

## Testing

To verify the functionality, you can run the automated tests using Playwright.

### Prerequisites

- Python 3
- Playwright (`pip install playwright`)
- Browser binaries (`playwright install chromium`)

### Running Tests

You can create a test script (like the one below) to verify core functions:

```python
from playwright.sync_api import sync_playwright
import os

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")

        # Test 5+5
        page.click('button[data-val="5"]')
        page.click('button[data-val="+"]')
        page.click('button[data-val="5"]')
        page.click('button[data-val="enter"]')
        print(f"5 + 5 = {page.inner_text('#current-line')}")

        # Test sin(30) in DEG
        page.click('button[data-val="mode"]')
        page.click('button[data-val="sin"]')
        page.click('button[data-val="3"]')
        page.click('button[data-val="0"]')
        page.click('button[data-val=")"]')
        page.click('button[data-val="enter"]')
        print(f"sin(30) DEG = {page.inner_text('#current-line')}")

        browser.close()

if __name__ == "__main__":
    run_tests()
```

## Tech Stack

- **HTML5 / CSS3** (Grid & Flexbox)
- **JavaScript** (ES6+)
- **math.js** (External library for calculations)
