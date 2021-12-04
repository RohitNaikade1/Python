import json


with open("google_us_querygen.json","r") as read_file:
    b=json.load(read_file)

# b=json.dumps(b)

posfilter=list()
negfilter=list()
negprof=list()
FT=list()
cvfilter=list()
year=list()
branches=list()
degree=list()
university=list()


for key in b['posfilter']['values']:
    posfilter.append(key)

for key in b['negfilter']['values']:
    negfilter.append(key)

for key in b['negprof']['values']:
    negprof.append(key)

for key in b['FT']['values']:
    FT.append(key)

for key in b['cvfilter']['values']:
    cvfilter.append(key)

for key in b['branches']['values']:
    branches.append(key)

for key in b['year']['values']:
    year.append(key)

for key in b['degree']['values']:
    degree.append(key)

for key in b['university']['values']:
    university.append(key)

result=list()
for ft in FT:

    str=""
    str = str + ft +"\\"
    
    for negf in negfilter:
        negf=  str + negf + "\\"
        
        for negp in negprof:
            negp= negf + negp + "\\"
            # print(str)

            for cvf in cvfilter:
                cvf= negp+ cvf + "\\"

                for uni in university:
                    uni= cvf+ uni + "\\"

                    for br in branches:
                        br= uni+ "-" + br + "\\"

                        for deg in degree:
                            deg= br+ "-" + deg + "\\"

                            for yr in year:
                                yr= deg+ yr + "\\"
                                result.append(yr)


f = open("queries.txt", "w")

for str in result:
    f.write(str)
    f.write("\n")
f.close()