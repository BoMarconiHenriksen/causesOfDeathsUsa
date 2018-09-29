"""
This class is used to download a file when there is no file information in the url.
"""


from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi


"""
This method is used when there is no file information in the url.
The Content-Disposition header will contain the filename.
"""
def download(url):
    # Open the url for reading as a request object.
    remotefile = urlopen(url)

    # Hvis requestet indeholder en fil, der skal downloades så kan Content-Disposition fortælle hvad filen hedder.
    file_information = remotefile.info()['Content-Disposition']
    # file_information indeholder nu: attachment; filename=NCHS_-_Leading_Causes_of_Death__United_States.csv

    # Returner et dictioinary med filename og navnet på filen.
    value, params = cgi.parse_header(file_information)
    file_name = params["filename"]
    print("Downloading file...")

    # Henter filen og gemmer den lokalt.
    urlretrieve(url, file_name)
    return file_name
