import storer
import svgs
from html2image import Html2Image
week_to_check = storer.get_info_from_file("active")

#print(week_to_check)



def infoToHtml(info,char):
    htmlString = ''
    htmlString += '<html><head><link rel="stylesheet" href="static/style.css" /></head><body class ="'+char+'">'
    htmlString += '<div class="class-grid">'    
    htmlString += '<div class="header-grid">'
    #htmlString += '<div class="class-image">'+svgs.class_svg[char]+'</div>'
    htmlString += '<div class="class-name"><span>'+char.capitalize()+'</span></div>'
    
    htmlString += '<div class="subtext">'
    htmlString += 'Made by: @D2WeeklyRolls'
    htmlString += '</div>'
    htmlString += '</div>'
    htmlString += '<div class="vendor-grid">'
    for vendor in info:
        if vendor != "total_notable_rolls":
            htmlString += '<div class="inventory-grid '+vendor+'">'
            htmlString += '<div class="vendor-header">'
            #htmlString += '<div class="vendor-image">'+svgs.vendors_svg["zavala"]+'</div>'
            htmlString += '<div class="vendor-name"><span>'+vendor+'</span></div>'
            htmlString += '</div>'
            htmlString += '<div class="item-grid">'

            #print(vendor)
            for armor in info[vendor]['items']:
                htmlString += '<div class="item-card '+info[vendor]["items"][armor]["affinity"]+'">'
                htmlString += '<div class="item-header">'
                if info[vendor]["items"][armor]["is_notable"]:
                    htmlString += '<div>'+svgs.notable_svg["notable"]+'</div>'
                else:
                    htmlString += '<div>'+svgs.notable_svg["not_notable"]+'</div>'
                htmlString += '<span>'+armor.capitalize()+'</span>'               
                htmlString += '<span>'+str(info[vendor]["items"][armor]["stat_total"])+'</span>'                
                htmlString += '</div>'              
                                    
                htmlString += '<div class="item-stat">'             
                for stat in info[vendor]["items"][armor]:
                    if stat != "is_notable" and stat != "stat_total" and stat!= "affinity":
                        
                        htmlString += '<span>'+stat+'</span>'            
                        htmlString += '<div class="stat-bar">'
                        htmlString += '<div class="bar">'
                        htmlString += '<div class="bar-value" style="width: '+str(info[vendor]["items"][armor][stat]/3.5)+'em;"> </div>'
                        htmlString += '</div>'
                        htmlString += '</div>'


                        htmlString += '<span class="item-stat-value">'+str(info[vendor]["items"][armor][stat])+'</span>'           
                            
                        
                        #print(stat) 
                htmlString += '</div>' 
                htmlString += '</div>' 
                #print(armor)
            
            htmlString+= '</div>'
            htmlString+= '</div>'
        #
    
    htmlString+= '</div>'
    htmlString += '<div class="footer-text">A armor roll is considered "notable" if it has any of these characteristics: 15+ on two stats, 20+ on one stat or 56+ stat total </div>'
    htmlString+= '</div>'
    htmlString+= '</body></html>'
    #print(info)
    return htmlString

def generateImg(info,char):
    outputHtml = infoToHtml(info[char],char)
    options ={
        "--width": "5000"
    }
    css = 'body{background-color: rgb(7, 13, 31);}.class-grid {display: inline-grid;grid-template-columns: auto auto auto auto;background-color: saddlebrown;grid-gap: 0.5rem;min-width: 100vw;min-height: 100vh;}.titan{background-color: rgb(150, 36, 36);}.hunter{background-color: rgb(36, 44, 150);}.warlock{background-color: rgb(252, 255, 65);}.vendor-grid{display: inline-grid;grid-template-columns: auto;background-color: #4f06c4;padding: 0.5rem;grid-gap: 0.5rem;border-radius: 1rem;}.zavala{background-color: orange;}.drifter{background-color: green;}.shaxx{background-color: red;}.devrim{background-color: rgb(6, 168, 74);}.item-card {display: inline-grid;grid-template-columns: auto auto auto;background-color: rgb(104, 103, 103);padding: 0.08rem;border-radius: 1rem;}.card-grid-item {padding: 0.25rem;text-align: center;}.notability-indicator{width: 1rem;height: 1rem;background-color: rgba(255, 0, 0, 0.466);border-radius: 1rem;}.bar{width: 12rem;min-height: 1rem;background-color: rgb(48, 47, 47);}.bar-value{width: 6rem;min-height: 1rem;background-color: rgb(212, 212, 212);}'


    cssFile = 'style.css'
    htmlFile = 'index.html'
    otherFiles = 'static/titan.svg'
    hti = Html2Image(chrome_path="/opt/google/chrome/chrome",size=(1920*2,1660*2))

    hti.screenshot(html_str=outputHtml, css_file=cssFile, save_as=char+'.png')


def generateHtml(info,char):
    outputHtml = infoToHtml(info[char],char)
    file_name = char
    with open(file_name+".html", "w") as file:
        file.write(outputHtml)


hti = Html2Image(chrome_path="/opt/google/chrome/chrome",size=(1920*2,2060*2))

def generateImgs(info):
    for char in info:
        if char != "all_notable_rolls":
            print(char)
            generateHtml(info,char)
            hti.screenshot(url=char+'.html', save_as=char+'.png')

def testTheThing():
    hti.screenshot(url='http://127.0.0.1:5500/index.html', save_as='index.png')

#doTheThing()
#testTheThing()

