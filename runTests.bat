:: start "" creates a new cmd window
start /b python -m pytest .\tests\indexTest.py --headless
start /b python -m pytest .\tests\productTest.py --headless & pause
:: python -m pytest .\tests\mainTest.py
:: python -m pytest .\tests\mainTestCopy.py