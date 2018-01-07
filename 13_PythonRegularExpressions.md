# Python Regular Expressions 

```python
import re
from pprint import pprint
import requests

sentence = "the quick brown fox jumped over the lazy dog"

o = re.search('quick', sentence)
# get starting and ending position of the match
print(o.start(), o.end())  # 4, 9
print(o.span(), type(o.span()))  # (4, 9) <class 'tuple'>
print(o.group())  # quick


sentence = "the 1 quick brown fox jumped over 10 lazy dogs"
# character sets in brackets
# A-Z, a-z are ranges
first_word = re.search('[a-zA-Z]+', sentence)
print(first_word)  # <_sre.SRE_Match object; span=(0, 3), match='the'>
print(first_word.group())  # the

words = re.findall('[a-zA-Z]+', sentence)
print(words)  # ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'lazy', 'dogs']

numbers = re.findall('\d+', sentence)
print(numbers)  # ['1', '10']

# \w is equivalent to the character set [A-Za-z0-9_]
everything = re.findall('\w+', sentence)
print(everything)  # ['the', '1', 'quick', 'brown', 'fox', 'jumped', 'over', '10', 'lazy', 'dogs']

# negated sets
words_only = re.findall('[^\d ]+', sentence)
print("words_only: {}".format(words_only))

# word boundaries n - match anything not \w or [A-Za-z0-9_]
# \b represents the backspace character, which is why raw strings are being used
word_boundary = re.findall(r'\bjump\b', sentence)
print(word_boundary)  # []
word_boundary = re.findall(r'\bjumped\b', sentence)
print(word_boundary)  # ['jumped']

phone = '867-5309'
print(re.findall('\d', phone))  # ['8', '6', '7', '5', '3', '0', '9']
print(re.findall('\D', phone))  # ['-']


ZIP_PATTERN = '^(\d{5})(-\d{4})?$'

zip5 = '89999'
print("zip match {}: {}".format(zip5, re.match(ZIP_PATTERN, zip5)))

zip9 = '89999-1234'
print("zip match {}: {}".format(zip9, re.match(ZIP_PATTERN, '89999-1234')))


EMAIL_PATTERN = '^[\w\.\-]+@([\w\-]+\.)+[a-zA-Z]+$'


def is_valid_email(email_address):
    match_result = re.match(EMAIL_PATTERN, email_address)
    if match_result:
        return True
    else:
        return False


print(is_valid_email('me@example.com'))  # True
print(is_valid_email('example.com'))  # False
print(is_valid_email('www.example.com'))  # False


# Tab-delimited File
def process_stocks_file(txt):
    header_row = []
    stocks = re.split('\n', txt)
    stock_info_list = []

    fields_remove_quotes = ["Company Name", "Volume"]
    fields_format_amount = ["Volume"]

    for stock in stocks:
        if re.match('^Symbol', stock):
            header_row = re.split('\t', stock)
        else:
            stock_info_row = re.split('\t', stock)
            stock_info = {}

            if len(stock_info_row) > 1:
                for idx, column in enumerate(stock_info_row):

                    header = header_row[idx]
                    if header in fields_remove_quotes:
                        column = re.sub('"', '', column)
                    if header in fields_format_amount:
                        column = int(re.sub(',', '', column))

                    stock_info[header] = column

                stock_info_list.append(stock_info)
    return stock_info_list


# get contents from file
# using context manager (https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)
with open('./files/stocks.txt', 'r') as f:
    stocks_txt = f.read()
# print(stocks_txt)
stocks = process_stocks_file(stocks_txt)
for stock in stocks:
    pprint(stock)

company_names = [stock['Company Name'] for stock in stocks]
print(company_names)


REALLY_SIMPLE_URL_PATTERN = "(?:https?|ftp)://(?:[A-Za-z0-9.\/\-\#=&\?]+)"

# <a href="https://google.com" id="an_id" rel="a_rel">google</a>
# <a href="../link.html" id="an_id" rel="a_rel">my page</a>
ANCHOR_TAG_PATTERN = '<a(?:.+)</a>'

url = "https://docs.python.org/3.4/library/re.html"
# make sure requests is installed using pip
response = requests.get(url)
text = response.text

print(text)
hyperlinks = re.findall(REALLY_SIMPLE_URL_PATTERN, text)
for link in hyperlinks:
    print(link)

a_tags = re.findall(ANCHOR_TAG_PATTERN, text)
for link in a_tags:
    print(link)
```
