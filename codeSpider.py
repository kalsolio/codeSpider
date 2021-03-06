from pyquery import PyQuery as pq
import urllib.request
import os
import sys

#write the file
def writeFile(fileName, fileContent):
    if not os.path.exists('./src'):
        os.mkdir('src')
    
    if not os.path.isfile(fileName):
        f = open('src/'+fileName+'.java', 'w+')
        f.write('public class '+fileName + ' {\n')
        f.write(fileContent)
        f.write('\n}')
        f.close()
        return True
    else:
        return False

try:
    #get the url from input stream
    url = input('Enter the url of stackoverflow:\n')
    #get the source code of the web page
    page = urllib.request.urlopen(url)
    page_content = page.read().decode('utf-8')
    #use pyquery for get DOM in the web page
    mainPage = pq(page_content)
    print(mainPage('#question-header').text())
    question = mainPage('#question-header').text()
    i=0
    for answer in mainPage('.answer'):
        vote = pq(answer)('.vote-count-post')
        if int(vote.text()) < 1:
            continue 
        answerCode = pq(answer)('pre code')
        allCode = ''
        i += 1
        for codeSnippet in answerCode:
            allCode += pq(codeSnippet).text() + '\n'
        #print(pq(codeSnippet).text(), end='\n----------------------\n')
        writeFile('impl'+str(i), allCode)
except:
    print("Unexpected error:", sys.exc_info())

