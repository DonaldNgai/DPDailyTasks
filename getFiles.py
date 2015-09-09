import urllib2
import urllib

print("Start Program");

url = 'https://dev.flurry.com/secure/loginAction.do'

values = {'loginEmail' : 'dptngai@uwaterloo.ca ',
          'loginPassword' : 'Q456!258w'
          }

data = urllib.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

with open('firstPage.html', 'w') as file_:
        file_.write(the_page)

##req = urllib2.Request('https://dev.flurry.com/analyticsUsersNewUsers.do?projectID=468116&versionCut=versionsAll&intervalCut=30Days&segmentID=0&channelID=0&networkId=0&canCalculateHourly=true&canCalculateDayparting=true')
##response = urllib2.urlopen(req)
##the_page = response.read()
##with open('firstPage.html', 'w') as file_:
##    file_.write(the_page)

print("End Program");
