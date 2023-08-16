import requests,json,time,random,os
from multiprocessing import Pool

headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.",
#"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
"Cache-Control":"max-age=0",
"Cookie":"_gid=GA1.2.1918226941.1691976546; ASP.NET_SessionId=maomoy35cx2sxewe31cjjzb3; .ASPXAUTH=095B7FB930693CCF9125CCB41DF73A3FF0C2CAF4307B9868A7E115E1739DD5E6583791916B028BADB9F1DDE7F45F40114ADDE6BBEAEA2AA014B096C866D3C5BA47524518CFD9B56BF77171FB988FD85F28590420910257B42291A6840FCF5109BFABCDBDDC7117795F8C6914169212F68E0F8BCAAC3161FE3CCD31E6AADC1DEBD232D893239D03036A04E700C85F8361EDFC5034D7DAC0F4803B31161C263412C18710063541AC338740E47FBB9C4F6C8CD38E63A172AC6693DBC5CEF2222AB7F0F439448A247BE34310760DED52960B82BC98F8; www.nettruyenmax.comportalroles=A75856516A97B34CF23B1838E50481FCDE01B1CDDE4E18B417C442C0A1CFC68E6EB68DE3840CEDD474601EBD94A915DC4E25FEB5AACB4B96361EF072E96AE8120425D8B9210BCD92E79C299C09E15D0CFBC9C29363CFC22DA7DE720E2680F146C25AF8DCF1EAA9E5B061B5B9294E99ACBD334211204747C0425FF2DAAC57AE204C414B788DD86A2697CBA34F1922D3D128C39F86B3C3EC940DB2DEDCEFBA7F0D258356B19DDBA13C4512994F74E05CEA29DE48A3; _gat_gtag_UA_57670566_10=1; comment_name=; comment_email=; _ga=GA1.2.739477405.1691976546; _ga_4X7L3HYB4K=GS1.1.1692008230.50.1.1692009723.0.0.0",
"Referer":"https://www.nettruyenmax.com/",
"Sec-Ch-Ua":"""Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115""",
"Sec-Ch-Ua-Mobile":"?0",
"Sec-Ch-Ua-Platform":"Windows",
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"same-origin",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }
def main(i,cl ,red):

            id = i["chapterId"]
            data ={
                "chapterId": "",
                "comicToken": "72869ef1-129c-f5fd-dc2b-0cdc7df19e35",
                "userToken": ""
            }
            data2 = {
                "chapterId": "",
                "token": ""
            }
            data["chapterId"]=id
            chapter_loaded=cl.post("https://f.nettruyenmax.com/Comic/Services/ComicService.asmx/ChapterLoaded" ,headers=headers, data=data)
            load = chapter_loaded.status_code
            #print(load)
            #print(chapter_loaded.text)
            res = json.loads(chapter_loaded.text)
            if res["success"]==True and load ==200:
                token = res["token"]
                data2["chapterId"]=id
                data2["token"]=token
                read = red.post("https://f.nettruyenmax.com/Comic/Services/ComicService.asmx/Read" ,headers=headers, data=data2)
                #print(read.status_code)
                res = json.loads(read.text)
                #print(res)
                if res["success"]==True:
                    
                    return (i["name"])
                    #print("Đã đọc xong", i["name"])
                else: return("Loi") 
            else: return("Loi") 

time.sleep(1)
lis= ["17696"]#"4638", "17023",
rd =random.choice(lis)
tot=requests.get(f"https://www.nettruyenmax.com/Comic/Services/ComicService.asmx/ProcessChapterList?comicId={rd}", headers=headers)
while tot.status_code!=200:
    tot=requests.get(f"https://www.nettruyenmax.com/Comic/Services/ComicService.asmx/ProcessChapterList?comicId={rd}", headers=headers)
print(tot.status_code)
total=tot.text
data_c=json.loads(total)
c=0
chapter = data_c["chapters"]
print(len(chapter))
#luong=int(input("Luoong:"))
# for i in range(luong):
diem=0
while True:
    cl = requests.Session()
    red=requests.Session()
    for i in reversed(range(len(chapter))):
            if i%10==0:
                os.system('cls')
            result=main(i=chapter[i],cl=cl,red=red)
            ch = "Chapter" in result
            if ch ==True:
                diem+=1
                print(result,diem)
