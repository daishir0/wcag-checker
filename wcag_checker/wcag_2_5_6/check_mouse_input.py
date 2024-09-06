from wcag_checker.utils import fetch_url, parse_html

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        print("Failed to fetch URL content")
        return False

    soup = parse_html(html_content)
    
    # マウスイベントが使用されているかチェック
    mouse_events = ['onclick', 'onmouseover', 'onmouseout', 'onmousedown', 'onmouseup']
    for event in mouse_events:
        if soup.find(attrs={event: True}):
            return True

    # マウス関連のJavaScriptコードをチェック
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and any(event in script.string for event in mouse_events):
            return True

    print("手動確認が必要: マウス入力が許可されているか確認してください。")
    return None