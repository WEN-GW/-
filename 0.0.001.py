HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch(url: str, retry: int = 3) -> requests.Response | None:
    for attempt in range(1, retry + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)

            if resp.status_code == 404:
                return None

            resp.raise_for_status()

            resp.encoding = resp.apparent_encoding

            return resp

        except requests.RequestException:
            if attempt == retry:
                return None

            time.sleep(1.5 * attempt)