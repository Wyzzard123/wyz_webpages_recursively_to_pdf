# Download Webpages Recursively to PDF
The module, linkpdfs.py, downloads all relevant pages linked to a given webpage up to a given recursion depth as one consolidated PDF. This utilises pdfkit, wkhtmltopdf.exe and BeautifulSoup.

The purpose behind me making this was to facilitate my studying of documentation for professional certifications. Instead of needing to click what seemed like hundreds of pages of documentation, I could download everything to a few consolidated PDF files.

This is something I always wish I could have done back when I was in school studying non-programming-related topics, where all relevant study material was scattered all over a website. However, I did not have the programming know-how to implement a solution until now.

* See example.py for an example of how to implement this.
** The example shows how one may download documentation, and organise files and folders using the functions provided in linkpdfs.py.

* See also example_workaround.py to see how to get a file directly. 
** The download_all_pdfs function sometimes has issues, and it may be better to apply download_as_pdf directly to a list of links. 
** Hence, download_all_pdfs also outputs a text file with all the links formatted as a list.

* A smaller scale example is provided in if __name__ = "__main__".

* See https://pythonspot.com/extract-links-from-webpage-beautifulsoup/

At the moment, this file also writes a LINKS_.txt file to keep all the links, and also to keep track of any split files. This is needed because the download_to_pdf function can be rather unreliable when used repeatedly. 

If the file size of a particular file is too small, it is likely there was an error and the page could not be fetched. In that case, please use the list written in LINKS_.txt for the relevant file and use download_as_pdf on the relevant list of links directly.



* *Note*: Sometimes the number of pages or filesize may vary slightly because the elements on a page (especially the graphic elements) don't all load. 

## Getting Started

Install Python 3.81 (some walrus operators used).

Install requirements.txt as follows:

```
pip install -r requirements.txt
```

Install wkhtmltopdf for your OS at https://wkhtmltopdf.org/downloads.html.

Set your PATH_TO_WKHTMLTOPDF_EXE to the location of wkhtmltopdf.exe. You need to download wkhtmltopdf.exe for your OS. 

```
PATH_TO_WKHTMLTOPDF_EXE = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=PATH_TO_WKHTMLTOPDF_EXE)
```
*See: https://www.tutorialexample.com/fix-oserror-no-wkhtmltopdf-executable-found-in-win-10-for-pdfkit-beginner-python-pdfkit-tutorial/
*See: https://pypi.org/project/pdfkit/
*See also https://wkhtmltopdf.org/
*See also https://pdfkit.org/docs/getting_started.html

## Available Functions
```
download_all_pdf(start_html_page, root_html_page, file_name="outfile", folder_name=".", filter = "prefix", regex_link_filter=r"http(s)?://", max_depth = 1, attribute='href', html_tag='a', config = pdfkit.configuration(wkhtmltopdf=PATH_TO_WKHTMLTOPDF_EXE), options={'javascript-delay': 200}, current_depth = 0, links=[], link_set=set())
```
Writes all links as well as links within those links up to a given recursion max_depth to a PDF file in a given folder name.
Uses download_as_pdf.
This will split the list and corresponding PDF if there are too many links, to prevent issues with pdfkit.from_url().
Note that this will ignore errors (and only print a generic error message), as pdfkit.from_url() is prone to them. Uncomment the try except blocks to see more details of any given error.

Returns the list of all links found if successful, or False if unsuccessful.
```
download_as_pdf(link_or_list, file_name="outfile", folder_name=".", config =pdfkit.configuration(wkhtmltopdf=PATH_TO_WKHTMLTOPDF_EXE), options={'javascript-delay': 200})
```
Download files from one link or multiple links in a list to a given file and folder. If the folder does not exist, it will be created.
Serves as a wrapper around pdfkit.from_url().
This will split the list and corresponding PDF if there are too many links, to prevent issues with pdfkit.from_url().
Note that this will ignore errors (and only print a generic error message), as pdfkit.from_url() is prone to them. Uncomment the try except blocks to see more details of any given error.

Returns true if successful, or False if unsuccessful.
```
gather_links(start_html_page, root_html_page, filter = "prefix", regex_link_filter=r"http(s)?://", attribute='href', html_tag='a')
```

Gathers all the links fitting the required criteria in a list. Takes as arguments: Returns the list.

* start_html_page -> Where we will begin our search.

* root_html_page -> This is normally the same as start_html_page, save where the filter is 'suffix' rather than 'prefix'. 

* filter -> Either 'prefix' or 'suffix'. This denotes whether the regex_link_filter provided searches for the beginning or the end of the link respectively. Suffix would be used if, for example, the regex filter is for '/help/support' rather than 'https://'.

* regex_link_filter -> Sieves out relevant links with a regular expression.

* attribute -> The html attribute to search for. Generally 'href'.

* html_tag -> The html tag to search for, generally 'a'.

```
gather_links_within_links(start_html_page, root_html_page, filter = "prefix", regex_link_filter=r"http(s)?://", attribute='href', html_tag='a', max_depth = 1, current_depth = 0, links=[], link_set=set())
```

Performs gather_links, but also appends to the list every link which meets the same requirements which can be found within each link. In other words, this recursively finds more and more links. Set a recursion limit with max_depth. 

The current_depth, links and link_set arguments should not generally be modified. These are just to facilitate the recursion. 

However, it may be a good idea to reset these every time the function is called, especially if the function is being called multiple times in a row. Otherwise, you may face multiple repeated pages.
 
## Known Issues and Workarounds

### Known Error

The download_as_pdf function appears to break with a list of more than around 200 links. Usually there is a [WinError206] for the length of the list being too long. Even if this error does not occur, too high a length usually results in the PDF file being unreadable or completely in plaintext. 

### Workaround 1: 

If the list length is greater than 100 we will split the PDF into parts of length 150 to feed into download_as_pdf.

As a redundancy, this is repeated in both download_as_pdf and download_all_pdf

### Workaround 2: 
If the files do not come out right, please simply use download_as_pdf() individually on the lists of links recorded in the output txt file.

If the size of the document is too small, you probably have to use this.

#### Workaround 3: 
If the pages come out as plaintext, set the 'javascript-delay' to a higher number (of milliseconds).

## TODO

1. Use iterative instead of recursive functions to prevent memory issues.
1. Make the code more efficient instead of checking for the same links over and over again.
1. Make the part_split a parameter to be passed in.
1. Make the text file with links optional (though it would not be recommended to turn this off).
1. Re-merge all split PDFs.

## Other Acknowledgments

See Raymond Hettinger's code for the fastest way to get all unique values in a list but preserve the order, taking advantage of how Python's dictionaries are now ordered:

* https://twitter.com/raymondh/status/944125570534621185
* Benchmarking: https://www.peterbe.com/plog/


