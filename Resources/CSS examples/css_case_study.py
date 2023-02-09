#Part1
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

<style>
    .even {
        color: blue;
    }

    .odd {
        color: green;
    }
</style>

<body>
    <div>
        <p class="odd" id="first">First</p>
        <p class="even" id="second">Second</p>
        <p class="odd" id="third">Third</p>
    </div>

    <div>
        <p class="even" id="fourth">Fourth</p>
        <p class="odd" id="fifth">Fifth</p>
        <p class="even" id="sixth">Sixth</p>
    </div>
</body>

</html>
"""
#convert the HTML string into a Beautiful Soup object.
html_soup = soup(html, 'html.parser')

#Next, we’ll use that object to choose and retrieve specific parts of the HTML code
odds = html_soup.find_all("p", class_="odd")

#In the preceding code, notice that we use the Beautiful Soup find_all method. Whereas the find method returns the first result of a search, the find_all method returns all the results. And, this method takes two arguments:
#The first argument, "p", specifies that we're searching for paragraphs—that is, p elements.
#The second argument, class_="odd", specifies that the elements must belong to the odd class.

#also, Notice the underscore (_) at the end of class_. We use an underscore because class is a reserved word Links to an external site. in Python.

for odd in odds:
    print(odd)

#Part 2
first = html_soup.find("p", id="first")
print(first.text)