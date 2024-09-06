from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    # Implement logic to check if line height is at least 1.5 times the font size
    # This is a placeholder for the actual implementation
    line_height_valid = True  # Replace with actual check
    return line_height_valid