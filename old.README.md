### Project information

Project information: N/A now

### Requirements

* Python 3.3+
* pip
* chromedriver — https://sites.google.com/a/chromium.org/chromedriver/downloads

Download and install latest Python 3 and chromedriver.

### Installation steps

1. Clone this repo.
2. Run `pip install -r requirements.txt`
3. Make sure your chromedriver is in /usr/local/bin and binary file named as chromedriver

### Run tests

Run all tests:
```
pytest -svv tests/
```

Run selected test:
```
pytest -svv tests/functional/test_user_login.py
```

Run tests with tag "debug":
```
pytest -svv -k 'debug'
```

### How to add new test

1. Create new file at **core/locators/** folder and add locators you need to work with.
2. Create new file at **pages/** folder and initialize added locators above (look at example).
3. Add feature file (Gherkin language) to **features/** folder. Each file should be self-descriptive. Example: `features/frontend/auth/registration.feature`
4. Add test file to **tests/** folder. Name starts with test_

Please follow folder structure.

### Contributing notes (examples)

TODO: Add contributing notes from examples:

1. https://github.com/matiassingers/awesome-readme/blob/master/readme.md
2. https://github.com/opengovernment/opengovernment/blob/master/CONTRIBUTING.md