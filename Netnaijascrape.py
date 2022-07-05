from bs4 import BeautifulSoup
import requests, openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "18 netnaija movies"
print(excel.sheetnames)
sheet.append(['Movie Category', 'Movie name'])

try:
    source = requests.get('https://www.thenetnaija.net/videos')
    source.raise_for_status()
    print(source)
    soup = BeautifulSoup(source.text,'html.parser')
    Movies = soup.find('div', class_="video-files").find_all('article')


    for Movie in Movies:
        Movie_category = Movie.find('div',class_='category').a.text
        Movie_name = Movie.find('h2').a.text
        print(Movie_category, Movie_name)
        sheet.append([Movie_category, Movie_name])








except Exception as e:
    print(e)
excel.save('NetnaijaScraping.xlsx')