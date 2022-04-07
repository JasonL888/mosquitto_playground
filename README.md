# mosquitto_playground
Local Docker environment with sample pub/sub clients to test out eclipse mosquitto MQTT server

# Pre-requisite
* Docker desktop installed
* If using the python clients
  * Python3 installed
  * Setup virtual environment
```
python3 -m venv ./venv
. ./venv/bin/activate
```
  * install Paho MQTT
```
pip install paho-mqtt
```

# Usage
## Start Up
* In the folder with docker-compose.yml,
```
docker-compose up -d
```
* Check the logs
```
tail -f log/mosquitto.log
```
  * should see following
```
1649341003: mosquitto version 2.0.14 starting
1649341003: Config loaded from /mosquitto/config/mosquitto.conf.
1649341003: Opening ipv4 listen socket on port 1883.
1649341003: Opening ipv6 listen socket on port 1883.
1649341003: mosquitto version 2.0.14 running
```


## Test drive with Paho MQTT
* in first terminal
```
. ./venv/bin/activate
python3 paho-mqtt/pub.py
```
* in second terminal
```
. ./venv/bin/activate
python3 paho-mqtt/sub.py
```

## Troubleshoot
* check the logs
```
tail -f log/mosquitto.log
```

* get into docker
```
docker exec -it sh
```

## Miscellaneous
* enter docker env
```
docker exec -it mosquitto /bin/sh
```
* add new user/password
  * use the [mosquitto_passwd](https://mosquitto.org/man/mosquitto_passwd-1.html) to generate
  * update to config/password_file

## Shut Down
```
docker-compose down
```

# Credits
* Learnt alot from following links
  * [Steve's Internet Guide](http://www.steves-internet-guide.com/into-mqtt-python-client/)
  * [Eclipse Mosquitto](https://mosquitto.org/)
  * [Original source of pub/sub python code](https://www.codestudyblog.com/sfb2109a/0906142542.html)
