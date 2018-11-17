#! /usr/bin/python3

import time
import datetime
import re
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select

def trademescraper():

    # directory = os.getcwd()
    outFile = open('/home/trademebot/tmdata_temp.csv', 'w+')

    global recordCount
    recordCount = 0
    
    browser = webdriver.Firefox(executable_path='/home/trademebot/geckodriver')
    
    time.sleep(3)
    browser.get("http://www.trademe.co.nz/property")
    time.sleep(3)

    select = Select(browser.find_element_by_xpath('//form[@id="PropertySearch"]/div/div/span[@class="drop-container"]/select[@id="PropertyRegionSelect"]'))
    regions = []
    for option in select.options:
        regions.append(option.text)
    
    browser.quit()

    for region in regions:
        if region == 'All New Zealand':
            continue
        browser = webdriver.Firefox(executable_path='/home/trademebot/geckodriver')
        time.sleep(3)
        browser.get("http://www.trademe.co.nz/property")
        time.sleep(3)
        select = Select(browser.find_element_by_xpath('//form[@id="PropertySearch"]/div/div/span[@class="drop-container"]/select[@id="PropertyRegionSelect"]'))
        select.select_by_visible_text(region)
        browser.find_element_by_xpath('//form[@id="PropertySearch"]/div/div/div/button[@type="submit"]').click()
        time.sleep(15)
        district = 'All Districts'
        suburb = 'All Suburbs'
        listings = browser.find_element_by_xpath('//div[@class="listing-count-label listing-count-holder listing-count-holder-header"]').text
        print(region,district,suburb,listings.split(' ',1)[0],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        outFile.write(','.join([region,district,suburb,str(listings.split(' ',1)[0]),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]))
        outFile.write('\n')
        recordCount = recordCount + 1
        time.sleep(1)
        select = Select(browser.find_element_by_xpath('//form[@id="sidebarSearch"]/div/span[@class="drop-container"]/select[@id="135"]'))
        time.sleep(1)
        districts = []
        for option in select.options:
            districts.append(option.text)
        for district in districts:
            if district == 'All districts' or district == '':
                continue
            print(region,district.rsplit(' ',1)[0],suburb,re.findall('([0-9]+)',district)[-1],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            outFile.write(','.join([region,district.rsplit(' ',1)[0],suburb,re.findall('([0-9]+)',district)[-1],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]))
            outFile.write('\n')
            recordCount = recordCount + 1
            select.select_by_visible_text(district)
            time.sleep(1)
            suburbs = browser.find_elements_by_xpath('//ul[@class="switch-list"]/li/span/input[@name="136"]')
            for suburb in suburbs:
                suburb = suburb.get_attribute('text')
                if suburb == 'All suburbs' or suburb == '':
                    continue
                print(region,district.rsplit(' ',1)[0],suburb.rsplit(' ',1)[0],re.findall('([0-9]+)',suburb)[-1],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                outFile.write(','.join([region,district.rsplit(' ',1)[0],suburb.rsplit(' ',1)[0],re.findall('([0-9]+)',suburb)[-1],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]))
                outFile.write('\n')
                recordCount = recordCount + 1
        browser.quit()

    outFile.close()

    print('Complete with ' + str(recordCount) + ' records written to temp file!')
    return recordCount
