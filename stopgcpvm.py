from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials

cred = ServiceAccountCredentials.from_json_keyfile_name("F:/My First Project-1c3e575f1f7c.json")

service = discovery.build('compute', 'v1', credentials=cred)

# Project ID for this request.
project = 'silicon-axle-200014'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'southamerica-east1-a'  # TODO: Update placeholder value.

# Name of the instance resource to stop.
instance = 'lab-node'  # TODO: Update placeholder value.

request = service.instances().stop(project=project, zone=zone, instance=instance)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
