import requests
import json
SUBSCRIPTION_KEY = "c1f1b1c175c5457fb8bdd14c525b0b54"
vision_service_address = "https://pythonimageanalize.cognitiveservices.azure.com/"

address = vision_service_address + "analyze"

parameters  = {'visualFeatures':'Description,Color','language':'en'}


image_path = "pb.jpeg"
image_data = open(image_path, "rb").read()

headers    = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)

response.raise_for_status()

results = response.json()
print(json.dumps(results))

