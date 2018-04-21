from html_sanitizer import Sanitizer
import os
import html2text
import re

sanitizer = Sanitizer()  # default configuration

org_articles_path = '../org_dataset/articles'
preprocessed_articles_path = '../preprocessed_dataset/articles'
not_labels = ["__init__.py", "Artykuly.csv"]
article_directories = [dir_name for dir_name in os.listdir(org_articles_path) if dir_name not in not_labels]

x = []
labels = []
i=0

# print(article_directories)

for directory in article_directories:
    files_under_directory = os.listdir(org_articles_path + "/" + directory)

    for filename in files_under_directory:
        with open(preprocessed_articles_path + "/" + directory + "/" + filename, 'w+') as outfile:
            with open(org_articles_path + "/" + directory + "/" + filename, 'r', encoding='utf-8') as infile:
                with open('labels', 'a+') as file:
                    input_text = infile.read()
                    sanitized_html = sanitizer.sanitize(input_text)
                    plain_text = html2text.html2text(sanitized_html)
                    text_without_whitespaces = re.sub(r"\s+", "", plain_text)
                    cleaned_text = re.sub(r'/[A-Za-z0-9]*/[a-zA-Z0-9_%:!@#$^&*()?;\'\"`~,.=+-]*[ \\\n\r\t]', '', plain_text, flags=re.MULTILINE)
                    cleaned_text = re.sub(r'https?:\/\/.*[\r\n]*', '', cleaned_text, flags=re.MULTILINE)
                    cleaned_text = re.sub(r'\W+', ' ', cleaned_text)
                    cleaned_text = re.sub(' +', ' ', cleaned_text)
                    cleaned_text = re.sub('_', '', cleaned_text)
                    outfile.writelines(cleaned_text)

                    x.append(cleaned_text)
                    labels.append(directory)
                    file.write(directory + ',')
                    print(i)
                    i+=1
