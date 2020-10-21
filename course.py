import json
import re
with open('course.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements = data["elements"][0]
course=[]
for item in elements["profileCourses"]["elements"]:
    course_item = {}
    if "name" in item.keys():
        course_item["course_name"]=item["name"]
    if "number" in item.keys():
        course_item["coure_number"]=item["number"]
    course.append(course_item)
print(course)