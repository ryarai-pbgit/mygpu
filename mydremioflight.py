from pyarrow import flight
from pyarrow.flight import FlightClient
import requests
import os

## Function to Retrieve PAT TOken from Dremio
def get_token(uri, payload):
 # Make the POST request
 response = requests.post(uri, json=payload)

 # Check if the request was successful
 if response.status_code == 200:
 # Parse the JSON response
   data = response.json()
 # Extract the token
   return data.get("token", "")
   print("Token:", token)
 else:
   print("Failed to get a valid response. Status code:", response.status_code)

## Arrow Endpoint
location = "grpc://<dremio server ip>:32010"

## Username and Password for Dremio Account
username = ""
password = ""

## Dremio REST API URL To Login and Get Token
uri = "http://<dremio server ip>:9047/apiv2/login"

## Payload for Get Token Requests
payload = {
 "userName": username,
 "password": password
}

## Auth Token
token = get_token(uri, payload)
print(token)

## Headers for Arrow Requests
headers = [
 (b"authorization", f"bearer {token}".encode("utf-8"))
 ]

## Query
query = """
SELECT * FROM mysnowflake."xxxx"."xxxx"."xxxx"
"""

## Create Arrow Flight Client
client = FlightClient(location=(location), disable_server_verification=False)

## Create Flight Call Options
options = flight.FlightCallOptions(headers=headers)

## Send Query
flight_info = client.get_flight_info(flight.FlightDescriptor.for_command(query), options)

## Get Query Results
results = client.do_get(flight_info.endpoints[0].ticket, options)

print(results.read_all())