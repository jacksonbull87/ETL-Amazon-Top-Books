

def convert_rating(rating):
    if x == 'None':
        return 0
    else:
        return float(rating[0:3])


#lets create a function that converts all this data to a simple boolean value. 1 if its a hardcover. 0 if its not
import re

def convert_cover_data(cover):
    lower_co = cover.lower()
    if re.match('hardcover', lower_co):
        return True

#create a function that converts the values in this columns to an integer
def convert_num_page_to_int(num_page):
    num = re.findall("\d+", num_page)
    if len(num) > 0:
        return int(num[0])
    else:
        return 'NaN'