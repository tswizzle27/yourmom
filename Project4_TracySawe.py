
import urllib.request
def ebay ():
    search=str(input("What would you like to search?"))
    url="https://www.ebay.com/sch/i.html?_nkw="+search
    page = urllib.request.urlopen(url).read().decode("UTF-8")
    itemlist=page.split("class=s-item__link href=")

    #price
    itemlist=page.split("class=s-item__link href=")
    filename="ebay"+search+".csv"
    ebayfile=open(filename, "w")
    for p in range (1,len(itemlist)):
        item=itemlist[p]
        dstart=item.find("$")
        dend=item.find("<",dstart)
        price=item[dstart:dend]
        

    #name
        nstart=item.find("class=s-item__title>")
        nend=item.find("</h3>",nstart)
        nstart=nstart+20
        name=item[nstart:nend]
        


    #url
        ustart=item.find("https:")
        uend=item.find("class=s-item__title>",ustart)
        iurl=item[ustart:uend]
        ebayfile.write(name, iurl, price)
        ebayfile.write("\n")
        
    ebayfile.close()
ebay ()
