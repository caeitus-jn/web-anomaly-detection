from urllib.parse import urlparse, parse_qs, unquote_plus

def parse_http_request(raw_request):
    lines = raw_request.strip().split("\n")
    request_line = lines[0].strip()
    method, full_url, _ = request_line.split()

    parsed_url = urlparse(full_url)
    uri = parsed_url.path
    query_params = parse_qs(parsed_url.query)
    
    params = {k: unquote_plus(v[0]) for k, v in query_params.items()}

    headers = {}
    for line in lines[1:]:
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            headers[key] = value.strip()

    return {
        "method": method,
        "uri": uri,
        "params": params,
        "headers": headers,
        "body": "" 
    }