import mechanize
def patterncounter():       #defining function
    count=0                          #declaring variable count for counting
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
#initialising browser
    browser.set_handle_robots(False)
    browser.open("http://www.minerbots.blogspot.in/")  #opening URL  
    html = browser.response().readlines() #Fetching web contents
    for i in range(0,len(html)):   #Searching for pattern 'Vicz' line by line
      if 'Vicz' in html[i]:              
        count=count+1    
    print "%d No of times found"%count #analyzing and producing results 
    
    
patterncounter();