# Py Test

Py test is python framework that is used for unit testing. 


## Install pytest
You must have downloaded python and pip pakage manager to install pytest. You can download with this link https://packaging.python.org/en/latest/tutorials/installing-packages/ .Following are the steps to intall pytest.

1. Run the following command in your command line:

```bash
  pip install -U pytest
```
2. Check that you installed the correct version:
```bash
  pytest --version
```
# How to run Program
1. You can run the single test program by following command (here my program name is first_test.py) :
```bash
  pytest first_test.py
```
2. For multiple test case program you can run using testname bye sub-string maching or group test by marker.
    i. For sub-string matching following command is used(for example method1 is my test method) :
    ```bash
    py.test -k method1 -v
    ```
    here -k used for substring mathc and 
    -v icreases the posiiblilities.
    ii. Using marker program can be run by command (you have to declare the marker before the test function eg."@pytest.mark.first") :
    ```bash
    py.test -m one
    ```

# Install requests
To use the module requests in api test by pytest, you need to install request else it will so error "ModuleNotFoundError: No module named 'requests'" . To install request you should have install pip. Then hit following command:
  ```bash
    pip install requests
    ```
    Or you can read this stackoverflow solution
    https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests

