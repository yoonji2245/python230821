import requests
from bs4 import BeautifulSoup
import time
import os
from openpyxl import Workbook

def crawl_blog_info(search_keyword, num_pages):
    wb = Workbook()
    ws = wb.active
    ws.append(["Blog Name", "Blog Address", "Post Date"])
    
    for page in range(1, num_pages + 1):
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 10}"
        
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            blog_entries = soup.find_all('li', class_='bx')
            
            for entry in blog_entries:
                blog_name = entry.find('a', class_='sh_blog_title').get_text()
                blog_address = entry.find('a', class_='sh_blog_title')['href']
                post_date = entry.find('dd', class_='txt_inline').get_text()
                
                ws.append([blog_name, blog_address, post_date])
                
            # Add a delay to be respectful of the website's resources
            time.sleep(1)
        else:
            print(f"Failed to fetch the webpage for page {page}.")
    
    # Create the 'work' folder if it doesn't exist
    save_folder = 'c:\\work'
    os.makedirs(save_folder, exist_ok=True)
    
    # Save the Excel file
    excel_file_path = os.path.join(save_folder, f"{search_keyword}_blog_info.xlsx")
    wb.save(excel_file_path)
    print(f"Data saved to {excel_file_path}")

if __name__ == "__main__":
    search_keyword = "맥북에어"
    num_pages = 5  # For demonstration purposes, you can adjust this as needed
    crawl_blog_info(search_keyword, num_pages)
