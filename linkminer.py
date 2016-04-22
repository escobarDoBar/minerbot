import mechanize
def linkminer():                      
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)
    browser.open("http://www.minerbots.blogspot.in/")  #you can give your url
    html = browser.response().readlines()
    for link in browser.links():
      print link.text, link.url
      print 
  
  
linkminer();