from bs4 import BeautifulSoup as soup

html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>
        <h2>First heading</h2>
        <p>First paragraph</p>
    </div>

    <div>
        <h2>Second heading</h2>
        <p>Second heading</p>
    </div>
</body>

</html>
"""
# Remember that in Python, we can enclose a string that spans multiple lines inside a pair of triple quotation marks ("""). We have enclosed a string that spans multiple lines inside a pair of triple quotation marks ("""). In the preceding code, notice that we’ve also assigned this string to a variable named html.

html_soup = soup(html, 'html.parser')
print(html_soup.prettify())
html_soup.title

#The preceding code gets the HTML code of the title element. Specifically, it returns <title>Document</title>. That is, html_soup is an object that holds the parsed HTML code. And, its title attribute contains the HTML code of the title.

doc_title = html_soup.title.text
print(doc_title)

div = html_soup.find("div")
print(div)

#Recall that the HTML document contains two <div> tags. Why did the Python code return only one? The reason is that on its own, the find method returns only the first instance of the element that it’s searching for.
#Now that we know that the Beautiful Soup find method returns the first instance of an element, let's use it to retrieve the text of the first h2 element in the HTML document. To do so, enter and run the following code in the next cell:

doc_heading = html_soup.find("h2").text

#Next, let’s try scraping the text of the first paragraph (p) element on the page and saving it to a variable named doc_paragraph. To do so, enter and run the following code in the next cell:
doc_paragraph = html_soup.find("p").text

#Finally, let's store the information that we scraped in a Python data structure. In this case, we'll use a dictionary. To do so, enter and run the following code in the next cell:

doc_info = {"title": doc_title,
            "heading": doc_heading,
            "paragraph": doc_paragraph}

#Depending on our needs, we can export a dictionary of scraped data to a JSON file, a Pandas DataFrame, or a MongoDB database.       