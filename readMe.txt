Virtual env activation:
python3 -m venv venv
source venv/bin/activate
deactivate

pip install selenium pytest pytest-html
pytest tests/test_insider.py --browser=chrome

TO-DO
load page - add timeout. 
allure report
waits too much to complete all
gitignore
pycache?
static scrolll! look for it.