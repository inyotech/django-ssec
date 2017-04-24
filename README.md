# Animated Satellite Weather Images

This application displays an animated sequence of current weather
images downloaded from the [Space Sciences and Engineering Center
(SSEC) at the University of
Wisconsin-Madison](http://www.ssec.wisc.edu/data/)
These images are produced at regular intervals and made available for
public download [here](http://www.ssec.wisc.edu/data/).

This project contains a periodic task that downloads these images to
local storage.  A minimal django python web application serves these
images on demand to a javascript animator for display.  An online
instance of this web application can be found
[here](http://weather.inyotech.com/)

## Installation

1. Clone this repository.

```
$ git clone https://github.com/inyotech/ssec.git
```

2. (optional) create and activate a local python virtual environment
for python dependencies.

```
$ python -m venv venv

$ source venv/bin/activate
```

3. Install the required packages.

```
$ pip install -r requirements.txt
```

4. Images are downloaded with a custom django management command, This
command can be run periodically to continually download images when
they are available.

```
$ python manage.py downloadimage


