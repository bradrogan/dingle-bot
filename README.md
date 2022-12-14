# dingle-bot

A silly thing to ring a Raspberry Pi controlled cowbell every time a webhook is called (for example, from Jira).

## Install

For everything to work it's assumed this repo resides in `/home/pi/apps/dingle-bot/`. If it isn't, you'll need to edit the `*.service
` files accordingly.

Download and install the latest `ngrok` to `/home/pi/apps/` from http://ngrok.io. If you pick a differing location, you'll need to edit `start-ngrok.sh`.

```
./ngrok authtoken <token from ngrok.io account>
```

**Note:** You'll need to update your `subdomain` in `startup-ngrok.sh`

Add the system services so everything runs when the network is up and restart automagically when they die:

```
sudo cp *.service /lib/systemd/system/
sudo systemctl enable dingle-bot.service
sudo systemctl enable ngrok.service
```

Start them manually for the first time (or reboot instead):

```
sudo systemctl start dingle-bot.service
sudo systemctl start ngrok.service
```

## Using it

### Jira

Add the webhook to Jira `Settings -> System -> Webhooks` as `http://<subdomain>.ngrok.io/bell/<key>`

**Note:** The `key` is a one way hash. Generage your own using `hashlib.md5(str("<key string>").encode()).hexdigest()` and update `HASH` in `dingle-bot.py`

### Curl

```
curl -i -H "Content-Type: application/json" -X POST  https://<subdomain>.ngrok.io/bell/<key>

```
