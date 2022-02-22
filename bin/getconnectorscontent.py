# to do:
# Add API request parameter to for single connector 
# Add flags to restrict to md or json
# Add flag to overwrite existing md and json or write new files only
# Add temp section to append placeholder json until fields added and populated in the connectors db/API response
# Confirm naming conventions
# Confirm permalinks

import requests
import re
import os
import json

response = requests.get('https://my.cyclr.com/api/connectors?pageSize=1000&details=true')
if response.status_code == 200 :
	json_data = response.json()

	template_md = os.path.join(os.path.dirname(__file__), './assets/template.md')
	# print(__file__)
	# print(template_md)
	# parse each connector in the response array
	for item in json_data:
		# derive the connector filenames 
		connector_name = item['Name']
		file_name = re.sub("[^a-zA-Z0-9]", "", connector_name).lower()
		file_md = '../pages/connectors-new/connector-'+file_name+'.md'
		file_md_full = os.path.join(os.path.dirname(__file__), file_md)
		file_json = "../_data/connectors-new/connector-"+file_name+".json"
		file_json_full = os.path.join(os.path.dirname(__file__), file_json)
		# print("Write md "+file_md_full+" and json "+file_json_full)

		# inject the connector name into the md template
		# open the template file and the new file
		with open(template_md,'r') as fromfile, open(file_md_full,'a') as tofile:
			for line in fromfile:
				# replace text 
				# append to new md
				newline = re.sub("connectortitle", connector_name,line)
				newline = re.sub("connectorname", file_name,newline)
				tofile.write(newline)

		# write the connector object to the json file
		json_string = json.dumps(item, indent=4)
		with open(file_json_full, "w") as filejson:
			filejson.write(json_string)