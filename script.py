from urllib.parse import urlparse
from urllib.request import http

def unshorten(shortURL):
    longURL = urlparse(shortURL)
    h = http.client.HTTPConnection(longURL.netloc)
    h.request("HEAD", longURL.path)
    response = h.getresponse()
    return response.getheader('Location')


if __name__ == "__main__":
    url = input("Enter the TinyURL you want decoded: ")
    realURL = unshorten(url)
    if realURL is not None:
        print("This is the (possible malicious) URL: ", realURL)
