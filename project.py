import json
with open('pub_pro_patent.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
"""
title
description
startDate
endDate
"""
elements=data["elements"][0]
project=[]
for item in elements["profileProjects"]["elements"]:
    project_item={}
    start_year_month = ""
    end_year_month = ""
    if "title" in item.keys():
        project_item["title"]=item["title"]
    if "description" in item.keys():
        project_item["description"] = item["description"]
    if "dateRange" in item.keys():
        if "start" in item["dateRange"].keys():
            start_year_month = ""
            if "year" in item["dateRange"]["start"].keys():
                year = str(item["dateRange"]["start"]["year"])
                start_year_month = year
            if "month" in item["dateRange"]["start"].keys():
                month = str(item["dateRange"]["start"]["month"])
                start_year_month = start_year_month + "-" + month
        if "end" in item["dateRange"].keys():
            end_year_month = ""
            if "year" in item["dateRange"]["end"].keys():
                year = str(item["dateRange"]["end"]["year"])
                end_year_month = year
            if "month" in item["dateRange"]["end"].keys():
                month = str(item["dateRange"]["end"]["month"])
                end_year_month = end_year_month + "-" + month
    project_item["endDate"] = end_year_month
    project_item["startDate"] = start_year_month
    project.append(project_item)
    a=json.dumps(project)
with open("test111.txt", 'w') as f:
    f.write(a)
print(project)