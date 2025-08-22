
# Paste your cookie string here
cookie_string = "curl ^"https://www.nfl.com/compiledassets/css/base.css?_t=a4565cfda331459519de131b259fb20e^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  -H ^"If-None-Match: ^\^"1dc0e1e2d83dbae^\^"^" ^
  -H ^"Referer: https://fantasy.nfl.com/^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36^" ^
  -H ^"sec-ch-ua: ^\^"Not;A=Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"139^\^", ^\^"Chromium^\^";v=^\^"139^\^"^" ^
  -H ^"If-Modified-Since: Fri, 15 Aug 2025 19:52:49 GMT^" ^
  -H ^"sec-ch-ua-mobile: ?0^""

# Dict to store cookies
cookies = {}

# Loop through each cookie
for cookie in cookie_string.split('; '):
    # Split cookie into name and value
    cookie_parts = cookie.split('=')
    cookies[cookie_parts[0]] = cookie_parts[1]
