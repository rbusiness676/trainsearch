Note: This docker file is not tested,Hence it may not promperly.


How to run
==========

#Run the docker-compose up command from the top level directory for your project.
$docker-compose up

Now our application running , http://localhost:8000/

TestData:
=======
Please place all files in "providerData" directory under "app/" directory.
Default, Application try to read data from "app/providerData/*" files.

API testing
===========

curl http://localhost:8000/train/search?origin='MUM'&destination='DEL'



