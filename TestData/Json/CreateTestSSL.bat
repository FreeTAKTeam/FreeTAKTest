@echo off
setlocal enabledelayedexpansion

for /f "tokens=*" %%a in (testfileSSL.txt) do (
set "string=%%a"
set "testname=!string:_SSL.json=!"
  (
   echo {
   echo     "test_id": "%RANDOM%",
   echo     "test_name": "Test Case !testname!",
   echo     "test_description": "This is the SSL test for !testname!.xml",
   echo     "environment": {
   echo         "host": "localhost",
   echo         "port": 8089,
   echo         "protocol": "SSL"
   echo     },
   echo     "setup": {
   echo         "setup_resource": true,
   echo         "dependencies": {
   echo             "ancestors": {},
   echo             "descendents": {}
   echo         }
   echo     },
   echo     "test_info": {
   echo         "endpoint": {
   echo             "path": "NA",
   echo             "method": "NA"
   echo         },
   echo         "header-info": {
   echo             "Content-Type": "NA",
   echo             "Authorization": "NA"
   echo         },
   echo         "request": {
   echo             "file": "\src\FreeTAKTest\TestData\test_data\!testname!.xml"
   echo         },
   echo         "response": {
   echo             "file": "\src\FreeTAKTest\TestData\test_data\!testname!.xml"
   echo         },
   echo         "comparison": {
   echo             "compare_response_body": true,
   echo             "compare_response_headers": false
   echo         },
   echo         "teardown": {
   echo             "delete_resource": true
   echo         }
   echo }
  )>"%%a"
)