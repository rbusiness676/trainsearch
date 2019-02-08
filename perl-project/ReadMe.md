Note: This docker file is not tested,Hence it may not work properly.


How to run
==========

#Run the docker-compose up command from the top level directory for your project.

$docker-compose up
Now our application running , http://localhost:8000/

Or

$python manage.py runserver

TestData:
=======
Please place all files in "providerData" directory under "app/" directory.
Default, Application try to read data from "app/providerData/*" files.

API testing
===========

Case1:
=====

curl http://localhost:8000/train/search?origin='MUM'&destination=''

Or

curl http://localhost:8000/train/search?origin=''&destination='DEL'

Or

curl http://localhost:8000/train/search?origin=''&destination=''


output:
======
400 Bad Request HTTP1.1
Input Empty


Case 2:
=======
curl http://localhost:8000/train/search?origin='MUM'&destination='DEL'

output:
======
200 OK HTTP1.1

[
  {
    "Origin": "MUM",
    "Destination": "DEL",
    "Time": {
      "Departure Time": "4/30/2016 9:30:00",
      "Destination Time": "4/30/2016 16:30:00"
    },
    "Price": "150",
    "Currency": "INR"
  },
  {
    "Origin": "MUM",
    "Destination": "DEL",
    "Time": {
      "Departure Time": "4/30/2016 11:42:00",
      "Destination Time": "4/30/2016 16:30:00"
    },
    "Price": "550",
    "Currency": "INR"
  },
  {
    "Origin": "MUM",
    "Destination": "DEL",
    "Time": {
      "Departure Time": "4/30/2016 11:41:01",
      "Destination Time": "4/30/2016 17:25:00"
    },
    "Price": "650",
    "Currency": "INR"
  }
]



