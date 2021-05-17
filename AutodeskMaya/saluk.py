#written in 2013
#Nitin Peter
#export loader for scripts
def jloader(fil):
   import json
   json_data=open(fil).read()
   data = json.loads(json_data)
   return data
