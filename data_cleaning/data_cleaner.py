from html_sanitizer import Sanitizer
import os
import html2text

sanitizer = Sanitizer()  # default configuration

org_articles_path = '../org_dataset/articles'
preprocessed_articles_path = '../preprocessed_dataset/articles'
not_labels = ["__init__.py", "Artykuly.csv"]
article_directories = [dir_name for dir_name in os.listdir(org_articles_path) if dir_name not in not_labels]

print(article_directories)

for directory in article_directories:
    print(directory)
    files_under_directory = os.listdir(org_articles_path + "/" + directory)
    print(files_under_directory)

    for filename in files_under_directory:
        with open(preprocessed_articles_path + "/" + directory + "/" + filename, 'w') as outfile:
            with open(org_articles_path + "/" + directory + "/" + filename, 'r', encoding='utf-8') as infile:
                input_text = infile.read()
                sanitized_html = sanitizer.sanitize(input_text)
                plain_text = html2text.html2text(sanitized_html)
                outfile.writelines(plain_text)
