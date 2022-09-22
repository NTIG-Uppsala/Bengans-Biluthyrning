:: start "" creates a new cmd window
start /b python -m pytest .\tests\indexTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\productTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\employeeTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\indexPhoneTest.py --headless --settings-file=.\tests\phoneSettings.py
start /b python -m pytest .\tests\productPhoneTest.py --headless --settings-file=.\tests\phoneSettings.py & pause
:: python -m pytest .\tests\mainTest.py
:: python -m pytest .\tests\mainTestCopy.py