```
Author: Sujayyendhiren Ramarao

Description: Learn all the devices in your home network. This framework can be extended to include a custom device. In initial attempt we can discover home network, is programmable devices are configured then can leverage this framework to access them via this micro web app.

Sections in this README.md give more insight into this micro app. If there are suggestions for  supporting more interesting devices or improvements in existing features, please do not hesitate to contact me.
```

### What does this micro app offer ?

1. Home network discovery and caching 
  - D3Js Forcelayout visualization of discovered devices. Hover mouse over any node to view
       IP address and hostname of device.
       ![Discovered home network](/static/img/samplenw.png)
  - Caching of discovered info that can be leveraged by other parts of automation
        Current logic leverages cached data by looking at hostname for key match.

2. Basic Hue Light controls - Already configured lights are discovered and displayed on the UI
   ![Philips Hue view](/static/img/samplehue.png)

3. Bose Soundtouch - Device info display
   ![BoseSoundtouch view](/static/img/samplebose.png)

4. Os detection of discovered devices 
   Note: Few entries are intentionally removed for security reasons.
   ![OS detection of home devices](/static/img/sampleosdetect.png)

5. Assuming that the app is running on a Raspberry Pi and is running 24*7. You'll need to configure audio in case it isnt configured yet. This app has an option 'Wifi Door bell', to make good use of it our handheld should be in the Home WiFi range and a few mp3s must be placed in the mp3 directory created within this repo. The directory 'mp3' is created once we run this app or we can create it manually before starting the app.

```
sudo apt-get install -y alsa-utils  mpg321 lame
sudo modprobe snd_bcm2835
```

![Wifi based doorbell](/static/img/samplewifidoorbell.png)

6. Enable a service on the server. On my Raspberry Pi 3 I have AIY Google voicekit setup. The service is enabled or disable via this app.

![Google AIY service control](/static/img/sampleaiy.png)

7. Initial analysis of Kaggle labelled datasets
   This tells us maximum occurrences per column
   - Upload a csv dataset using upload options.
   - Select a dataset and select top occurrence count in rows.


### What does this tool leverage
1. Tested on MAC with Python 3.6 and Python3.4 on Raspberry Pi3.
2. Flask + jinja2 + html + bootstrap + D3js + nmap + scapy


### Installation 
Please refer INSTALL.md

### Future plans
1. Code needs to be object oriented.
2. More home automation devices shall be integrated here.
3. Voice activated controls (Leveraging google assistant) 
   or integration with AIY Google kit.
4. Kaggle analysis is in early stages. Need to add more punch to it.
5. Release unittest options. For now it is evolving.
6. Plan to proximity detection.
7. Intrusion of new device should raise alarm (voice).


### Issues
- Container network and home network are different please do not build docker image yet.
- No logging in the initial commit
- Improvements in REST abstraction 
- Code assumes that ip address ending with '.1' is Gateway. In the next version default gateway from netstat -r shall be picked.


### Docker implementation

##### Build docker image
```
docker build -t homeautomation .
```

##### Run docker container
```
docker run -d --name="HomeAutomation" -p 80:80 sujayy1983/homeautomation
```

### Report issues and suggestions
- Contact: sujayy1983@gmail.com
- Author: Sujayyendhiren Ramarao (Sujay)
