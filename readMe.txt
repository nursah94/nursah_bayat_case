Virtual env activation:
python3 -m venv venv
source venv/bin/activate
deactivate

Setup:
pip install -r requirements.txt

To Run Tests:
pytest tests/test_insider.py --browser=chrome
pytest tests/test_pet_api.py --api-key=special-key
locust -f tests/locustfile.py --host=https://www.n11.com

TO-DO
allure report
waits too much to complete all
gitignore
static scrolll! look for it.