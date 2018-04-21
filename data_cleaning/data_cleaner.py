from html_sanitizer import Sanitizer
sanitizer = Sanitizer()  # default configuration
sanitized_html = sanitizer.sanitize('<html>sample text</html>')