:: start "" creates a new cmd window

:: Test for Jönköping
:: Test for Swedish sites
start /b python -m pytest .\tests\jonkoping\sv\headerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\sv\headerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\jonkoping\sv\footerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\sv\footerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\jonkoping\sv\indexTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\sv\indexTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\jonkoping\sv\productTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\sv\productTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\jonkoping\sv\employeeTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\sv\employeeTest.py --headless --settings-file=.\tests\phoneSettings.py

:: Test for English sites
start /b python -m pytest .\tests\jonkoping\en\indexEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\en\indexEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\jonkoping\en\footerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\en\footerEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\jonkoping\en\headerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\en\headerEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\jonkoping\en\productEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\en\productEnTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\jonkoping\en\employeeEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\jonkoping\en\employeeEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

:: Test for Luleå
:: Test for Swedish sites
start /b python -m pytest .\tests\lulea\sv\headerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\sv\headerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\lulea\sv\footerTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\sv\footerTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\lulea\sv\indexTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\sv\indexTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\lulea\sv\productTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\sv\productTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\lulea\sv\employeeTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\sv\employeeTest.py --headless --settings-file=.\tests\phoneSettings.py

:: Test for English sites
start /b python -m pytest .\tests\lulea\en\indexEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\en\indexEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\lulea\en\footerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\en\footerEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\lulea\en\headerEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\en\headerEnTest.py --headless --settings-file=.\tests\phoneSettings.py 

start /b python -m pytest .\tests\lulea\en\productEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\en\productEnTest.py --headless --settings-file=.\tests\phoneSettings.py

start /b python -m pytest .\tests\lulea\en\employeeEnTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\lulea\en\employeeEnTest.py --headless --settings-file=.\tests\phoneSettings.py

:: Test for landing page

:: Test for Swedish sites
start /b python -m pytest .\tests\landingPage\sv\indexTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\landingPage\sv\indexTest.py --headless --settings-file=.\tests\phoneSettings.py

:: Test for English sites
start /b python -m pytest .\tests\landingPage\en\enTest.py --headless --settings-file=.\tests\customSettings.py
start /b python -m pytest .\tests\landingPage\en\enTest.py --headless --settings-file=.\tests\phoneSettings.py & pause

