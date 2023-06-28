# import urllib
#use urllib.request to get the data from the art
# write a function that takes a url
# return a response

import urllib.request as urllib


def main(url):
    print("checking connectivity..... ")
    response = urllib.urlopen(url)
    print("connected to", url, "sucessfully")
    print("the response code was", response.getcode())


print("this is site connectivity cheker")
input_url= input("enter the urls: ")

main(input_url)

