:: start "" creates a new cmd window

:: Test for Swedish sites
start /b python -m pytest .\tests\headerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\headerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\footerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\footerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\indexTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\indexTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\productTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\productTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\employeeTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\employeeTest.py --headless --settings-file=.\tests\phoneSettings.py

:: Test for English sites
start /b python -m pytest .\tests\indexEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\indexEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\footerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\footerEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\headerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\headerEnTest.py --headless --settings-file=.\tests\phoneSettings.py & pause


:: python -m pytest .\tests\mainTest.py
:: python -m pytest .\tests\mainTestCopy.py