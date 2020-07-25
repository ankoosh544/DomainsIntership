from django.shortcuts import render, redirect
from app.models import DomainsModel
from pywhoisxml.lookup import Lookup
import whois
from datetime import datetime
import requests
import pandas as pd
import dns.resolver



# Create your views here.
def showIndex(request):
    dd = DomainsModel.objects.values()
    return render(request, "design.html", {"data": dd})


def displayIndex(request):
        global itserver, comserver, euserver, netserver, orgserver, infoserver, bizserver
        dd = DomainsModel.objects.all()
        if request.method == "POST":
            ff = request.FILES["f"]
            print(ff)
            text = ff.read()
            txt = text.split("\n".encode('utf-8'))
            l = len(txt)
            for x in range(l):
                res = txt[x].decode('utf-8')
                res2 = [txt[x].decode('utf-8')]
                comstring = res.replace("it", "com")
                comstring1 = [comstring]
                eustring = res.replace("it", "eu")
                eustring1 = [eustring]
                netstring = res.replace("it", "net")
                netstring1 = [netstring]
                orgstring = res.replace("it", "org")
                orgstring1 = [orgstring]
                infostring = res.replace("it", "info")
                infostring1 = [infostring]
                bizstring = res.replace("it", "biz")
                bizstring1 = [bizstring]


                try:
                    for a in res2:
                        a2 = a.replace("\r","")
                        w = whois.whois(a2)
                        # d= (w.creation_date).date()
                        # print(d)
                        print(w)
                        # res= w.domain_name +" \n \n" + str(w.creation_date)
                        itserver = w.name_servers
                        print("servername is", itserver)

                except (whois.parser.PywhoisError):
                    print(" no match found so free domain")
                    itserver=""

                try:
                    for a in comstring1:
                        a2 = a.replace("\r", "")
                        w = whois.whois(a2)
                        print(w)
                        comserver = w.name_servers
                        print("Server name is", comserver)
                        # comstring = w.domain_name + "\n"+ str(w.creation_date)
                except (whois.parser.PywhoisError):
                    print(" no match found so free domain")
                    comserver = ""


                try:
                    for a in eustring1:
                        a2 = a.replace("\r", "")
                        w = whois.whois(a2)
                        print(w)
                        euserver=w.name_servers
                        print(euserver)
                except (whois.parser.PywhoisError):
                    print(" no match found so free domain")
                    euserver = ""


                # try:
                #     for a in netstring1:
                #         a2 = a.replace("\r", "")
                #         w = whois.whois(a2)
                #         print(w)
                #         netserver=w.name_servers
                #         print(netserver)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")
                #     netserver=None
                #
                #
                # try:
                #     for a in orgstring1:
                #         a2 = a.replace("\r", "")
                #         w = whois.whois(a2)
                #         print(w)
                #         orgserver=w.name_servers
                #         print(orgserver)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")
                #     orgserver = None
                #
                #
                # try:
                #     for a in infostring1:
                #         a2 = a.replace("\r", "")
                #         w = whois.whois(a2)
                #         print(w)
                #         infoserver=w.name_servers
                #         print(infoserver)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")
                #     infoserver = None
                #
                #
                # try:
                #     for a in bizstring1:
                #         a2 = a.replace("\r", "")
                #         w = whois.whois(a2)
                #         print(w)
                #         bizserver = w.name_servers
                #         print(bizserver)
                # except (whois.parser.PywhoisError):
                #     print(" no match found so free domain")
                #     bizserver = None
                DomainsModel(it=res,com=comstring,eu=eustring,net=netstring,org=orgstring,info=infostring,biz=bizstring).save()
                # "netserver": netserver, "orgserver": orgserver, "infoserver": infoserver, "bizserver": bizserver
            return render(request, "design.html", {"data": dd,"itserver1":itserver,"comserver1":comserver,"euserver1":euserver})

        else:
                return showIndex(request)



def deleteData(request):
    print("delete")
    dd = DomainsModel.objects.all()
    dd.delete()
    displayIndex(request)
    return render(request, "design.html", {"data": dd})
