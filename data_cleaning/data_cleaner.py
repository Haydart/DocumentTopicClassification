from html_sanitizer import Sanitizer
import os

sanitizer = Sanitizer()  # default configuration
sanitized_html = sanitizer.sanitize('<html>sample text</html>')

articles_path = '../org_dataset/articles'
not_labels = ["__init__.py", "Artykuly.csv"]
article_directories = [dir_name for dir_name in os.listdir(articles_path) if dir_name not in not_labels]

print(article_directories)

for directory in article_directories:
    print(directory)
    files_under_directory = os.listdir(articles_path + "/" + directory)
    print(files_under_directory)
