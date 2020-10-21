import json
with open('pub_pro_patent.txt','r',encoding='UTF-8') as f:
    data=json.load(f)
elements=data["elements"][0]
# publicationment={"publication_name":[],"description":[],"publisher":[],"date":[],"url":[]}
publication=[]
for item in elements["profilePublications"]["elements"]:
    publicationment={}
    year=""
    month=""
    day=""
    if "publishedOn" in item.keys():
        if "year" in item["publishedOn"].keys():
            year=str(item["publishedOn"]["year"])
        if "month" in item["publishedOn"].keys():
            month=str(item["publishedOn"]["month"])
        if "day" in item["publishedOn"].keys():
            day=str(item["publishedOn"]["day"])
        if month=="":
            publicationment["date"]=year
        elif day=="":
            publicationment["date"]=year + "-" + month
        else:
            publicationment["date"]=year + "-" + month + "-" + day
    if "description" in item.keys():
        publicationment["description"]=item["description"]
    if "name" in item.keys():
        publicationment["publication_name"]=item["name"]
    if "publisher" in item.keys():
        publicationment["publisher"]=item["publisher"]
    if "url" in item.keys():
        publicationment["url"]=item["url"]
    publication.append(publicationment)
    a=json.dumps(publication)
with open("test111.txt", 'w') as f:
    f.write(a)
# print(publicationment["publication_name"])

print(publication)