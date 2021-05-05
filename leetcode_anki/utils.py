"""
Author       : zhangxianbing
Date         : 2021-03-12 17:45:51
Description  : 
LastEditTime : 2021-03-12 18:25:25
LastEditors  : zhangxianbing
"""
import browser_cookie3
import requests
from requests.cookies import RequestsCookieJar

from leetcode_anki.settings import BASE_URL, DEFAULT_BROWSER, LOGIN_URL


def browser_cookies(browser=DEFAULT_BROWSER) -> dict:
    if not hasattr(browser_cookie3, browser):
        raise ValueError(
            f"{browser} not in supported browsers: chrome, firefox, opera, edge, and chromium"
        )
    browser_cookies = getattr(browser_cookie3, browser)()
    cookies = {
        cookie.name: cookie.value
        for cookie in browser_cookies
        if BASE_URL.rfind(cookie.domain)
    }

    return cookies


def login(browser=DEFAULT_BROWSER) -> requests.Session:
    # cookies
    cookies = browser_cookies(browser)
    is_login = cookies.get("LEETCODE_SESSION") != None
    login_info = "successful" if is_login else "failed"
    print(f"login status: {login_info} on {browser}")

    # headers
    headers = {
        "Origin": BASE_URL,
        "Referer": LOGIN_URL,
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "x-csrftoken": cookies["csrftoken"],
    }

    return headers, cookies


if __name__ == "__main__":
    print(browser_cookies())
