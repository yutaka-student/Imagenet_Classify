Imagenet_Classify

This is "Recognize Image Web Application".
Returns the result of recognizing the image sent from the web with vgg16 of the python server.

First, start the python server by starting "engine.py" under "python_script".

The command to start the python server is:

python engine.py

Also, put the IP address of your server in "your IP address" in line 57 of "engine.py". If you start it on the local server, comment out line 57 and enable line 55.

Next, start "index.html" under "recognize_image". When opened, the button is arranged. For PC, press this button to select an image file. For smartphones, the camera will start and you can release the shutter.

Similarly, in the 57th line of "index.html", enter the IP address of the server you started up in "your server IP address".
