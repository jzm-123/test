import json
import re
with open('shuju6.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
language=[]
# language_item = {"language_name": [], "language_proficiency": [],"course_name": [],"coure_number":[], "honor_title": [],"honor_issuer": [],'honor_issueTime':[],
#                   "test_score":[],"test_score_name":[],"test_score_time":[],"organization_name":[],"organization_startTime":[],
#                   "organization_endTime":[],
#                   "ororganization_description":[],"ororganization_position":[]}
for item in elements["profileLanguages"]["elements"]:
    language_item={}
    if "name" in item.keys():
        language_item["language_name"]=item["name"]
    if "proficiency" in item.keys():
        language_item["language_proficiency"]=item["proficiency"]
    language.append(language_item)
print(language)