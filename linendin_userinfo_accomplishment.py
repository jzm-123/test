import json
import re
with open('shuju6.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
accomplish=[]
# accomplishment = {"language_name": [], "language_proficiency": [],"course_name": [],"coure_number":[], "honor_title": [],"honor_issuer": [],'honor_issueTime':[],
#                   "test_score":[],"test_score_name":[],"test_score_time":[],"organization_name":[],"organization_startTime":[],
#                   "organization_endTime":[],
#                   "ororganization_description":[],"ororganization_position":[]}
for item in elements["profileLanguages"]["elements"]:
    accomplishment={}
    if "name" in item.keys():
        accomplishment["language_name"]=item["name"]
    if "proficiency" in item.keys():
        accomplishment["language_proficiency"]=item["proficiency"]
    accomplish.append(accomplishment)
for item in elements["profileCourses"]["elements"]:
    accomplishment = {}
    if "name" in item.keys():
        accomplishment["course_name"]=item["name"]
    if "number" in item.keys():
        accomplishment["coure_number"]=item["number"]
    accomplish.append(accomplishment)
for item in elements["profileHonors"]["elements"]:
    accomplishment={}
    if "title" in item.keys():
        accomplishment["honor_title"]=item["title"]
    if "issuer" in item.keys():
        accomplishment["honor_issuer"]=item["issuer"]
    if "issuedOn" in item.keys():
        if "month" in item["issuedOn"].keys():
            accomplishment['honor_issueTime']=str(item["issuedOn"]["year"])+"-"+str(item["issuedOn"]["month"])
        else:
            accomplishment['honor_issueTime']=str(item["issuedOn"]["year"])
    accomplish.append(accomplishment)
for item in elements["profileTestScores"]["elements"]:
    accomplishment={}
    if "score" in item.keys():
        accomplishment["test_score"]=item["score"]
    if "name" in item.keys():
        accomplishment["test_score_name"]=item["name"]
    if "dateOn" in item.keys():
        if "month" in item["dateOn"].keys():
            accomplishment["test_score_time"]=str(item["dateOn"]["year"])+"-"+str(item["dateOn"]["month"])
        else:
            accomplishment["test_score_time"]=str(item["dateOn"]["year"])
    accomplish.append(accomplishment)
for item in elements["profileOrganizations"]["elements"]:
    accomplishment={}
    if "name" in item.keys():
        accomplishment["organization_name"]=item["name"]
    if "dateRange" in item.keys():
        if"start" in item["dateRange"].keys():
            accomplishment["organization_startTime"]=str(item["dateRange"]["start"]["year"])+'-'+str(item["dateRange"]["start"]["month"])
        if"end" in item["dateRange"].keys():
            accomplishment["organization_endTime"]=str(item["dateRange"]["end"]["year"])+'-'+str(item["dateRange"]["end"]["month"])
    if "description" in item.keys():
        accomplishment["ororganization_description"]=item["description"]
    if "positionHeld" in item.keys():
        accomplishment["ororganization_position"]=item["positionHeld"]
    accomplish.append(accomplishment)
a=json.dumps(accomplish)
with open("test111.txt", 'w') as f:
    f.write(a)
print(accomplish)
