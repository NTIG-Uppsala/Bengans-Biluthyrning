:: start "" creates a new cmd window
start /b python -m pytest .\tests\indexTest.py
start /b python -m pytest .\tests\productTest.py & pause
:: python -m pytest .\tests\mainTest.py
:: python -m pytest .\tests\mainTestCopy.py