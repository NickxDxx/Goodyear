import datetime
import time
import requests
from bs4 import BeautifulSoup
import csv
import re
import json

size_links = ['https://www.goodyear.com/en-US/tires/assurance-all-season/sizes-specs', 'https://www.goodyear.com/en-US/tires/assurance-comfortdrive/sizes-specs', 'https://www.goodyear.com/en-US/tires/assurance-maxlife/sizes-specs', 'https://www.goodyear.com/en-US/tires/assurance-weatherready/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-direzza-dz102-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-at20-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-at23-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-pt2a-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-sj6-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-st30-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-grandtrek-touring-as-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-signature-hp-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-signature-ii-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-31a-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-31-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sport-maxx-race/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sport-maxx-rt/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-01-dsst-rof-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-5000-dsst-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-5000m-dsst-ctt-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-5000m-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-5000-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-7000-as-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-7010-as-dsst-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-050/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-050-dsst-ctt/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-a1-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-gt600-dsst-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-gt-dsst-rof-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-sport-maxx-gt-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-winter-sport-3d-dsst-rof-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-winter-sport3d-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-winter-sport-4d/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-winter-sport-4d-noiseshield-technology/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-sp-winter-sport-4d-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-winter-maxx/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-winter-maxx-2/sizes-specs', 'https://www.goodyear.com/en-US/tires/dunlop-winter-maxx-sj8/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-exhilarate/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-2/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-2-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-3/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-3-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-3-sct/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-all-season/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-all-season-sct/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-run-on-flat/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-asymmetric-suv-at/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-gs-2-emt/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-gs-emt/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-super-car/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-supercar-3/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-supercar-3r/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-super-car-emt/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-f1-supercar-g2-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-gt-ii/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-ls/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-ls-2/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-ls-2-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-nct-5-emt/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-nct-5-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-rs-a/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-rs-a2/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-sport-all-season/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-sport-all-season-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-sport-all-season-sct/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-touring/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-touring-sct/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-ultragrip-gw-2/sizes-specs', 'https://www.goodyear.com/en-US/tires/eagle-ultragrip-gw-3/sizes-specs', 'https://www.goodyear.com/en-US/tires/efficient-grip-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/endurance/sizes-specs', 'https://www.goodyear.com/en-US/tires/excellence-rof/sizes-specs', 'https://www.goodyear.com/en-US/tires/excellence-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/fierce-attitude-mt/sizes-specs', 'https://www.goodyear.com/en-US/tires/fortera-hl/sizes-specs', 'https://www.goodyear.com/en-US/tires/fortera-sl/sizes-specs', 'https://www.goodyear.com/en-US/tires/integrity-tires/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-edge-as/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-edge-at/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-edge-hp/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-edge-ht/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-edge-ht-lt/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-safari-tsr/sizes-specs', 'https://www.goodyear.com/en-US/tires/kelly-winter-access/sizes-specs', 'https://www.goodyear.com/en-US/tires/ultra-grip-8-performance/sizes-specs', 'https://www.goodyear.com/en-US/tires/ultra-grip-ice-wrt/sizes-specs', 'https://www.goodyear.com/en-US/tires/ultra-grip-ice-wrt-lt/sizes-specs', 'https://www.goodyear.com/en-US/tires/ultra-grip-ice-wrt-suv/sizes-specs', 'https://www.goodyear.com/en-US/tires/ultra-grip-winter-tire/sizes-specs', 'https://www.goodyear.com/en-US/tires/wintercommand/sizes-specs', 'https://www.goodyear.com/en-US/tires/wintercommand-light-truck/sizes-specs', 'https://www.goodyear.com/en-US/tires/wintercommand-suv-cuv/sizes-specs', 'https://www.goodyear.com/en-US/tires/wintercommand-ultra/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-all-terrain-adventure/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-at/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-ats/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-duratrac/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-fortitude-ht/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-fortitude-ht-c-type/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-fortitude-ht-lt/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-hp/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-ht/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-mtr-kevlar/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-silentarmor/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-sr-a/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-st/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-trailrunner-at/sizes-specs', 'https://www.goodyear.com/en-US/tires/wrangler-trailrunner-at-lt/sizes-specs']


keys = ["Width","Aspect","Rim_size","Product_Code","Speed_Rating","Load_Index","Load_Range","Sidewall","Uniform_Tire_Quality_Grade","Max_Load", "Max_Inflation_Pressure","Approved_Rim_Width","Measured_Rim_Width","Section_Width","Tread_Depth","Outside_Diameter","Revs_Per_Mile","Price","Season","Terrain", "Warranty", "Brand_name", "Tire_name", "Image_links", "Features","Average_Rating","Total_reviews","Handling_rating","Tidecomfort","Threadlife","Traction","Wet_traction","Intertraction", "Product_Link", "Size_Link"]


with open("Goodyear tires .csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(keys)


headers = {
    'authority': 'www.goodyear.com',
    'method': 'GET',
    'scheme': 'https',
    'accept':'*/*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en',
    'referer': 'www.goodyear.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-arch':'"x86"',
    'sec-ch-ua-bitness': "64",
    "sec-ch-ua-full-version":'"108.0.5359.96"',
    'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.96", "Google Chrome";v="108.0.5359.96"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'some-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    "x-client-data": "CI62yQEIpbbJAQjEtskBCKmdygEItoXLAQiVocsBCIT5zAEI4vnMAQjf+swBCLKCzQEIw4LNAQi/hM0BCO+EzQE="

}

params = {'apikey': '801b220f-b6d5-42d1-93eb-0e5bc3f399a5',
'_noconfig': 'true'
}

proxies =  {'http': 'http://brd-customer-hl_4705e074-zone-data_center:73fny69jdzgf@zproxy.lum-superproxy.io:22225',
            'https': 'http://brd-customer-hl_4705e074-zone-data_center:73fny69jdzgf@zproxy.lum-superproxy.io:22225'}


start = time.time()
for url in size_links:
    print(url)
    final_list = []
    """Go to raw_link"""
    raw_link = url.replace("/sizes-specs", "")
    response2 = requests.get(raw_link, headers=headers)
    raw_page = BeautifulSoup(response2.content, 'html.parser')
    try:
        season = raw_page.find("span", "icon-all-weather--new").findNext().text
    except:
        try:
            season = raw_page.find("span", "icon-summer--new").findNext().text
        except:
            season = ""

    try:
        terrain = raw_page.find("span", "icon-all-terrain--new").findNext().text
    except:
        try:
            terrain = raw_page.find("span", "icon-run-flat--new").findNext().text
        except:
            terrain = ""
    try:
        warranty = raw_page.find("b", "bolder").text + " Tread Life Ltd. Warranty"
    except:
        warranty = ""

    # if season == "None" and terrain == "None" and warranty == "None":
    #     container2 = raw_page.find_all("span", "awr-pdp__feature-icons-text")
    #     for s in container2:
    #         season = s.text
    raw_name = raw_page.find("h1").text
    if raw_name == "Browse All Tires" or "Sorry" in raw_name:
        continue
    brand_name = raw_name.split(" ")[0]
    tire_name = raw_name.replace(brand_name,"")
    """Links """
    links_container = raw_page.select("ul.list-inline")
    links = []
    features = []
    for b in links_container:
        for link in b.find_all("img"):
            links.append(link["src"])
    if links == []:
        try:
            image_links = raw_page.select(".smart-image__image-item img")
            for x in image_links:
                links.append(x["src"])
        except:
            links = ""
    """Features"""
    features_container = raw_page.select("div.js-windowshade.gy-windowshade.tire-detail-tire-content-block")
    for content in features_container:
        f_container = content.find_all("h5", "gy-subhead")
        for feature in f_container:
            feature1 = feature.text.replace("\n", "")
            feature2 = feature1.replace("\t", "")
            features.append(feature2)
    del features[-3:]
    if features == []:
        features = ""
    print(raw_name)
    """Get season, terrain, warranty, features, links """



    """Go to review links """
    tire_raw_name = raw_link.replace("https://www.goodyear.com/en-US/tires/", "")
    review_link = f'https://display.powerreviews.com/m/2078993044/l/en_US/product/{tire_raw_name}/reviews?'
    params = {'apikey': '801b220f-b6d5-42d1-93eb-0e5bc3f399a5',
              '_noconfig': 'true'}
    response3 = requests.get(review_link, headers=headers, params=params)
    dic = response3.json()
    try:
        average_rating = dic["results"][0]["rollup"]["average_rating"]
    except:
        average_rating = ""
        total_review = ""
        handling_rating = ""
        ridecomfort = ""
        threadlife = ""
        traction = ""
        wettraction = ""
        intertraction = ""
        final_list.extend(
            [season, terrain, warranty, brand_name, tire_name, links, features, average_rating, total_review, handling_rating,
             ridecomfort, threadlife, traction, wettraction, intertraction, raw_link, url])
        response1 = requests.get(url, headers=headers)
        specs_page = BeautifulSoup(response1.content, 'html.parser')
        container = specs_page.select(
            "div.js-windowshade.gy-windowshade.sizes-specs-content-block.gy-collapsed-sm.gy-collapsed-lg")
        for x in container:
            first_list = []
            list_elements = x.find_all("span", "specs-description")
            # print(len(list_elements))
            size = re.findall('\d+', list_elements[0].text)
            width = size[0]
            aspect = size[1]
            rim_size = size[2]
            first_list.extend([width, aspect, rim_size])
            for raw_element in list_elements[1:16]:
                if "$" in raw_element.text:
                    first_list.append(raw_element.text.replace("$",""))
                else:
                    first_list.append(raw_element.text)
            final_results = first_list + final_list
            with open("Goodyear tires .csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(final_results)

            if len(list_elements) == 32:
                print(tire_raw_name+ "111111")
                second_list = []
                size2 = re.findall('\d+', list_elements[16].text)
                width2 = size2[0]
                aspect2 = size2[1]
                rim_size2 = size2[2]
                second_list.extend([width2, aspect2, rim_size2])
                for raw_element2 in list_elements[17:]:
                    if "$" in raw_element2.text:
                        second_list.append(raw_element2.text.replace("$", ""))
                    else:
                        second_list.append(raw_element2.text)
                final_results2 = second_list + final_list
                with open("Goodyear tires .csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(final_results2)
        continue
    total_review = dic["paging"]["total_results"]
    try:
        handling_rating = dic["results"][0]["rollup"]["properties"][3]["value"]
    except:
        handling_rating = "None"
    try:
        ridecomfort = dic["results"][0]["rollup"]["properties"][4]["value"]
    except:
        ridecomfort = "None"
    try:
        threadlife = dic["results"][0]["rollup"]["properties"][5]["value"]
    except:
        threadlife = "None"
    try:
        traction = dic["results"][0]["rollup"]["properties"][6]["value"]
    except:
        traction = "None"
    try:
        wettraction = dic["results"][0]["rollup"]["properties"][7]["value"]
    except:
        wettraction = "None"
    try:
        intertraction = dic["results"][0]["rollup"]["properties"][8]["value"]
    except:
        intertraction = "None"
    final_list.extend([season, terrain, warranty, brand_name, tire_name, links, features, average_rating, total_review, handling_rating,
         ridecomfort, threadlife, traction, wettraction, intertraction, raw_link, url])

    """Go to specs link"""
    response1 = requests.get(url, headers=headers)
    specs_page = BeautifulSoup(response1.content, 'html.parser')
    container = specs_page.select("div.js-windowshade.gy-windowshade.sizes-specs-content-block.gy-collapsed-sm.gy-collapsed-lg")
    for x in container:
        first_list = []
        list_elements = x.find_all("span", "specs-description")
        size = re.findall('\d+', list_elements[0].text)
        width = size[0]
        aspect = size[1]
        rim_size = size[2]
        first_list.extend([width, aspect, rim_size])
        for raw_element in list_elements[1:16]:
            if "$" in raw_element.text:
                first_list.append(raw_element.text.replace("$", ""))
            else:
                first_list.append(raw_element.text)
        final_results = first_list + final_list
        with open("Goodyear tires .csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(final_results)

        if len(list_elements) == 32:
            print(url+"111111")
            second_list = []
            size2 = re.findall('\d+', list_elements[16].text)
            width2 = size2[0]
            aspect2 = size2[1]
            rim_size2 = size2[2]
            second_list.extend([width2, aspect2, rim_size2])
            for raw_element2 in list_elements[17:]:
                if "$" in raw_element2.text:
                    second_list.append(raw_element2.text.replace("$", ""))
                else:
                    second_list.append(raw_element2.text)
            final_results2 = second_list + final_list
            with open("Goodyear tires .csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(final_results2)

    print(url)
stop = time.time()
print(stop-start)



