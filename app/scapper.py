import csv

from app.utils import *


def convert_currency(breal):
    breal = breal.replace(',', '.')
    price = float(breal) / 3.3
    return "%.2f" % price


def get_sizes():
    elements = find_elements_by_class("lower")
    sizes = ""
    for element in elements:
        sizes+= element.text
        sizes+= "|"

    return sizes[:-1]


def save_listing():
    csv_path = os.path.dirname(os.path.realpath(__file__)).replace(r"\app", "\download\output.csv")

    action = "VerifyAdd"
    category = "45333"
    title = find_element(".product-name > h1:nth-child(1)").text
    description = r' Melissa Kazakova. Now is the time for you to take this step with theMelissa Kazakova! The ' \
                  r'"Kazakova" is part of the preview of the upcoming2018 Mapping Collection ! ' \
                  r'NEW - Launch 2018 Mapping Collection.'
    condition_id = "1000"
    pic_url = find_element("#product-img").get_attribute("data-zoom-image")
    quantity = "1"
    price_format = "FixedPrice"
    price = convert_currency(find_element("#product-price-55060 > span:nth-child(1) > span:nth-child(2)").text)
    duration = "10"
    location = "Cacapava, Sao Paulo, Brazil"
    paypal_accepted = "1"
    paypal_email = "unit_1@abv.bg"
    returns_accept = "ReturnsNotAccepted"
    dispatch_time = "3"
    shipping_type = "Calculated"
    shipping_service_option = "USPSFirstClass"
    shoe_size = get_sizes()
    style = find_element("div.detalhes:nth-child(2) > dl:nth-child(2) > dt:nth-child(1)").text.replace("Tipo: ", "")
    brand = "Melissa"
    colour = ""

    data = list()
    data.append(action)
    data.append(category)
    data.append(title)
    data.append(description)
    data.append(condition_id)
    data.append(pic_url)
    data.append(quantity)
    data.append(price_format)
    data.append(price)
    data.append(price)
    data.append(duration)
    data.append(location)
    data.append(paypal_accepted)
    data.append(paypal_email)
    data.append(returns_accept)
    data.append(dispatch_time)
    data.append(shipping_type)
    data.append(shipping_service_option)
    data.append(shoe_size)
    data.append(style)
    data.append(brand)
    data.append(colour)

    with open( csv_path, "a") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(data)


open_main_page()
elements_list = find_element(".products-grid").find_elements_by_tag_name("li")
urls = list()

#TODO for debug purposes
# urls.append("https://lojamelissa.com.br/mapping/vixen")
for element in elements_list:
    url = element.find_element_by_tag_name("a").get_attribute("href")
    urls.append(url)

for url in urls:
    open_page(url)
    save_listing()

driver.close()