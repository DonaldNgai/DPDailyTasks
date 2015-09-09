import win32com.client
import datetime
import re

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def extractFromString(item,_string):
    regexExp = (r"[\s]" + item + r"[\s]*:[\s]*(.*?);")
    
    matchedRegex = re.search( regexExp, _string)
##    print _string
##    print regexExp
    
    if matchedRegex:
##        print item + str(matchedRegex.group(1))
        return int(matchedRegex.group(1));
    else:
        print item + " was not found!";
        return 0
    

##Change this to the correct date
start_date = datetime.date(2015, 9, 3)
end_date = datetime.date(2015, 9, 6)
end_date = end_date + datetime.timedelta(days=1)
aColumn = 10
dColumn = 9

excel = win32com.client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(r'D:\PythonScripts\DailyTaskAutomation\tab2.csv')
##wb = excel.Workbooks.Open(r'D:\PythonScripts\DailyTaskAutomation\test.xlsx')
ws = wb.Sheets(1)
easyCopy = "";
excel.InputBox

for single_date in daterange(start_date, end_date):
    nextDate = single_date + datetime.timedelta(days=1)
    
    print "Getting Tab 2 info for: " + single_date.strftime("%Y/%m/%d")
    ##1 is the enum for "and"
    ws.Columns("A:C").AutoFilter(1, ">" + single_date.strftime("%m/%d/%Y"), 1 , "<" + nextDate.strftime("%m/%d/%Y"))
    ##(y,x)
    ws.Cells(1,10).Value = "TotalBet"

    rowCount = 0;
    totalBetSum = 0;
    PayoutSum = 0;

    ##12 is the enum for all visible cells
    for cell in ws.Columns(dColumn).SpecialCells(12):
        rowInfo = cell.Value
        if rowCount == 0:
            rowCount = rowCount + 1
##            print "continue"
            continue
        if rowInfo == None:
##            print "break"
            break
##        totalBet = 0;
        totalBet = extractFromString("TotalBet",rowInfo);
        Payout = extractFromString("Payout",rowInfo);
        rowCount = rowCount + 1
        totalBetSum = totalBetSum + totalBet;
        PayoutSum = PayoutSum + Payout;

    print "TotalBet: " + str(totalBetSum) + " Payout: " + str(PayoutSum) + " Number of Rows: " + str(rowCount-1)
    easyCopy += str(totalBetSum) + " " + str(PayoutSum) + "\n"
    

print easyCopy

wb.Close(SaveChanges=1)
excel.Quit()
