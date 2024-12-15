from bs4 import BeautifulSoup

from webscraping.example1 import html_content

html_content="""
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Webpage</title>
</head>
<body>
    <h1>Welcome to My Simple Webpage</h1>
    <p class='intro'>This is a paragraph</p>
    <div id="content">
        <p>Check out these links:</p>
        <a href="https://example.com">Example 1</a>
        <a href="https://example2.com">Example 2</a>
        <a href="https://example3.com">Example 3</a>
    </div>
</body>
</html>
"""
soup=BeautifulSoup(html_content, 'html.parser')
paragraph_text=soup.find("p",class_="intro").text




print(paragraph_text)
paragraph_text=soup.find("h1").text
print(paragraph_text)
paragraph_text=soup.find("div",id="content").text
print(paragraph_text)
links = soup.find("div", id="content").find_all("a")


for link in links:
    print("Link:",link['href'])