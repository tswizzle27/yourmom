#Tracy Sawe
#December 6
#Ebay Scrape



#library import
import urllib.request
def ebay ():
    search=str(input("What would you like to search?"))
    url="https://www.ebay.com/sch/i.html?_nkw="+search
    page = urllib.request.urlopen(url).read().decode("UTF-8")
    #splits into list at the begining of class=s
    itemlist=page.split("class=s-item__link href=")

    #price
    itemlist=page.split("class=s-item__link href=")
    filename="ebay"+search+".csv"
    ebayfile=open(filename, "w")
    #doesn't start at 0
    for p in range (1,len(itemlist)):
        #extracts the prices
        item=itemlist[p]
        dstart=item.find("$")
        dend=item.find("<",dstart)
        price=item[dstart:dend]
        

        #exstracts the names
        nstart=item.find("class=s-item__title>")
        nend=item.find("</h3>",nstart)
        nstart=nstart+20
        name=item[nstart:nend]
        

        #extracts the urls
        ustart=item.find("https:")
        uend=item.find("class=s-item__title>",ustart)
        iurl=item[ustart:uend]


        #writes into a file
        ebayfile.write(name)
        ebayfile.write(",")
        ebayfile.write(price)
        ebayfile.write(",")
        ebayfile.write(iurl)
        ebayfile.write("\n")
    ebayfile.close()
ebay ()
