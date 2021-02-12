import requests, json, logging
from pyzabbix import ZabbixAPI

token = None

def getToken():
    jsondoc = {
        "username": "<your API user>",
        "password": "<your API password>"
    }

    url = '<API endpoint>'
    try:
        r = requests.post(url, data=jsondoc)
        if r.status_code == 200:
            response = json.loads(r.text)
            token = response['token']
            logging.info("Token has been retrieved")
            return token
        else:
            logging.error("Error getting token for portal")

    except Exception as e:
        logging.error(e)

def updateToken(token):
    try:
        zapi = ZabbixAPI("<zabbix url. ie: http://localhost>")
        zapi.login("<Zabbix API user>","<Zabbix API passwprd>")

        jsontoken = {
            'Authorization': 'Bearer '+ token
        }

	# Update your http agentchecks with the token. Use the item ID number found in the URL of the http agent itself.

        zapi.item.update(itemid='00000', headers=jsontoken)
        logging.info("Apperantly the token was updted... a double check won't hurt!")
    except Exception as e:
        logging.error(e)


token = getToken()
updateItem = updateToken(token)
