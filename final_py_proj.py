# -*- coding: utf-8 -*-
"""
English Voice Actor Database
Final Python 2 Project

Started on 4/19/20

This program's purpose is to scrape a list of voice actors and all of their
roles from Behind the Voice Actors(BTVA).

4/19 goal:  Scrape a VA's page for all voice credits and output in a
seemingly pleasant list.

4/28/20 goal:  From a directory (in this case, M/21), follow each VA's link
and scrape their credits.
NOTE:  This script will SKIP ANY CREDIT THAT IS ADDITIONAL VOICES, as they
are, for whatever reason, not designated by medium (video game, movie, etc.).

5/2/20 goal:  From a directory, go to the next numbered page of voice actors
and extract their data.  In this case, go from M/21 to M/22.

5/3/20 goal:  Exception handling on HTTPError.  Pretty much everything is done.
Plop into csv file and create another sheet for visualizing the data.
"""

import pandas as pd
import urllib
from bs4 import BeautifulSoup

def getSearchURL(term):
	"""
		Given a search term, builds a query.
	"""

	url = "https://www.behindthevoiceactors.com/voice-actors/%s" % (str(term))
	return url

def getPageText(url):
    """
        Requests url.  Returns HTML.
        
        Exceptions:
            HTTPError is a result of the count system below breaking due to a
            broken link.  On one of the VA links, it leads to a generic 404
            page.  The link in this case has the query "404" instead of, say,
            "Matthew-Mercer".  Returning "notalink" will feed into the logic
            below to skip this page and move on.
    """
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            return response.read()
    except urllib.error.HTTPError:
        return "notalink"

def buildSoup(term1, term2, func):
    """
        This is a generator only because I had no idea how to cleanly get both
        soup and s out of it, and I need soup later only to find "va".
    """
    pageText = getPageText(func(term1))
    if func(term1) == "notalink":
        soup = "nothing doing"
        s = "nadda thing"
        yield soup
        yield s
    else:
        soup = BeautifulSoup(pageText, 'html.parser')
        yield soup
        s = soup.find_all('a', term2)
        yield s

def grab_name(search):
    for element in search:
        bro = element.next_sibling
        if bro.find() == None:
            yield bro['href']

def buildLinkList(s):
    link_list = []
    for result in grab_name(s):
        link_list.append(result)
    return link_list

def linkFollow(term):
    try:
        url = "%s" % (str(term))
        
    except urllib.error.HTTPError:
        url = "notalink"
    return url

def extractCredit(s, soup):
    try:
        for element in s:
            credit = []
            va = soup.h1.string
            va = va.strip()
            credit.append(va)
            role = element['title']
            credit.append(role)
            parent = element.parent
            sibling = parent.previous_sibling
            title = sibling.a.string
            credit.append(title)
            medium = sibling.find('span').string
            credit.append(medium)
            year = sibling.contents[1]
            year = year.strip(' ')
            year = year.lstrip('(')
            credit.append(year)
            yield credit
    except AttributeError:
        credit == []

def main():
    credit_list = []
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    temp_count = 0
    count = 1
    for index in range(len(letter)):
        try:            
            abc = letter[temp_count]
            dummy_count = temp_count
            while dummy_count == temp_count:
                s_count = str(count)
                qwerty = abc + "/" + s_count
                print(qwerty)
                directory = buildSoup(qwerty, 'gray_border_img', getSearchURL)
                next(directory)
                dir_s = next(directory)
                if dir_s != []:                
                    dir_list = buildLinkList(dir_s)
                    for item in dir_list:
                        lalala = buildSoup(item, 
                                           'credit_pic_float char_no_clip', 
                                           linkFollow)
                        soup = next(lalala)
                        s = next(lalala)
                        if soup == "nothing doing":
                            None
                        else:
                            for result in extractCredit(s, soup):
                                credit_list.append(result)
                    count += 1
                elif dir_s == []:
                    count = 1
                    temp_count += 1
        except IndexError:
            break
    
    #print("Yay!")
    df = pd.DataFrame(data=credit_list, 
                          columns = ['va', 'title', 'medium', 'role', 'year'])
    
    df.to_csv('va_data.csv')
    
    """
        Refer to project_visualizations for more code.
    """
            
    #ax = df['va'].value_counts().plot('bar')
    #ax.set_xlabel('Voice Actor')
    #ax.set_ylabel('# of credits')
    
if __name__ == "__main__":
    main()