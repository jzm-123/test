import json
import re
with open('shuju1.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
# people=[]
# for item in viewers_data["elements"]:
#     people_item = {}
#     if "miniProfile" in item.keys():
#         if "lastName" in item["miniProfile"].keys() and "firstName" in item["miniProfile"].keys():
#             people_item["name"] = item["miniProfile"]["lastName"] + item["miniProfile"]["firstName"]
#         if "occupation" in item["miniProfile"].keys():
#             people_item["occupation"] = item["miniProfile"]["occupation"]
#         if "publicIdentifier" in item["miniProfile"].keys():
#             people_item["screen_name"] = item["miniProfile"]["publicIdentifier"]
#         if "objectUrn" in item["miniProfile"].keys():
#             people_item["user_id"] = item["miniProfile"]["objectUrn"].split(":")[-1]
#     people.append(people_item)
endorsement = []
# for item in data["elements"]:
#     endorsement_item = {"category": item["categoryName"],
#     "skills": [],"endorsementCount":[],"endorser_name":[],"endorser_occupation":[],"endorser_id":[]}
#     for skill_item in item["endorsedSkills"]:
#         if "name" in skill_item["skill"].keys():
#             endorsement_item["skills"].append(skill_item["skill"]["name"])
#         if "endorsementCount" in skill_item.keys():
#             endorsement_item["endorsementCount"].append(skill_item["endorsementCount"])
#         for endorsements in skill_item["endorsements"]:
#             if "lastName" and "firstName" in endorsements["endorser"]["miniProfile"].keys():
#                 endorsement_item["endorser_name"].append(endorsements["endorser"]["miniProfile"]["lastName"]+endorsements["endorser"]["miniProfile"]["firstName"])
#             if "occupation" in endorsements["endorser"]["miniProfile"].keys():
#                 endorsement_item["endorser_occupation"].append(endorsements["endorser"]["miniProfile"]["occupation"])
#             if "objectUrn" in endorsements["endorser"]["miniProfile"].keys():
#                 endorsement_item["endorser_id"].append(endorsements["endorser"]["miniProfile"]["objectUrn"].split(':')[-1])
#         endorsement.append(endorsement_item)

endorsement = []
for item in data["elements"]:
    endorsement_item = {"category": item["categoryName"],"skills":[]}
    for skill_item in item["endorsedSkills"]:
        if "name" in skill_item["skill"].keys():
            endorsement_item["skills"].append(skill_item["skill"]["name"])
        if "endorsementCount" in skill_item.keys():
            endorsement_item["endorsementCount"] = skill_item["endorsementCount"]
        for endorsements in skill_item["endorsements"]:
            if "lastName" and "firstName" in endorsements["endorser"]["miniProfile"].keys():
                endorsement_item["endorser_name"] = endorsements["endorser"]["miniProfile"]["lastName"] + " " + \
                                                    endorsements["endorser"]["miniProfile"]["firstName"]
            if "occupation" in endorsements["endorser"]["miniProfile"].keys():
                endorsement_item["endorser_occupation"] = endorsements["endorser"]["miniProfile"]["occupation"]
            if "objectUrn" in endorsements["endorser"]["miniProfile"].keys():
                endorsement_item["endorser_id"] = endorsements["endorser"]["miniProfile"]["objectUrn"].split(':')[-1]
    endorsement.append(endorsement_item)

print(endorsement)
a=json.dumps(endorsement)
with open("test111.txt", 'w') as f:
    f.write(a)