import json
import jsonschema

json_data_file = 'tbs-prov-std/Canadian_prov_terr_du_Canada.json'
json_schema_file = 'tbs-prov-std/Canadian_prov_terr_du_Canada_schema.json'

with open(json_data_file) as f:
    json_data = json.loads(f.read())

with open(json_schema_file) as f:
    json_schema = json.loads(f.read())

try:
    jsonschema.validate(instance=json_data, schema=json_schema)
except jsonschema.exceptions.ValidationError as err:
    print(err.message)
    print(err.cause)
    exit(1)

print("Good work, you did")
