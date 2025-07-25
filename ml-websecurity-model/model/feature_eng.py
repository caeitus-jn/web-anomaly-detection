# Feature engineering extracting html from CISC.
import json
import math
import pandas as pd
import re


# Load Log Data
def load_logs(path):
    data = []
    with open(path, 'r') as file:
        for line in file:
            try:
                log = json.loads(line.strip())
                data.append(log)
            except json.JSONDecodeError:
                continue
    return data

# Global Variable
logs = load_logs("ml-websecurity-model/app/labelled_dataset/mixed_attack.log")
print("Loaded", len(logs), "requests")

logs_V2 = load_logs("ml-websecurity-model/app/labelled_dataset/normal_training.log")
print("Loaded", len(logs_V2), "requests")




def extract_features(log):
    username = log.get("username", "")
    password = log.get("password", "")
    combined = f"{username} {password}".lower()

    key = r"\b(UNION|SELECT|ORDER|GROUP|DROP|INSERT|OR)\b"
    key_match = bool(re.search(key, 
                               combined, 
                               re.I))
    break_key = r"(?:\b1=1\b|\b1=0\b|1--|')"
    break_match = bool(re.search(break_key, 
                                combined, 
                                re.I))
    comment_match = ("--" in combined) or ("/*" in combined)
    is_sql = sum([key_match, break_match, comment_match]) >= 2

    xss_key = r"(<script\b|</script>|onerror=|onload=|javascript:|alert\()"
    is_xss = bool(re.search(xss_key,
                            combined,
                            re.I))

    s_quotes = len(re.findall(r"'", combined))
    d_quotes = len(re.findall(r'"', combined))


    if is_sql or is_xss:
        is_attack = -1
    else:
        is_attack = 1

    total_sql = len(re.findall(key, combined)) + len(re.findall(break_key, combined))
    total_xss = len(re.findall(xss_key, combined))

    features = {
        "username_length": len(username),
        "password_length": len(password),
        "shannon_entropy": entropy(combined),
        "contains_SQL": is_sql,
        "contains_XSS": is_xss,
        "sql_count": total_sql,
        "xss_count": total_xss,
        "no_squotes": s_quotes,
        "no_dquotes": d_quotes,
        "true_label": is_attack
    }

    return features


def entropy(combined):
    freq = {char: combined.count(char) / len(combined) for char in set(combined)}
    return -sum(p * math.log2(p) for p in freq.values())


def save_file(logs, path):
    features = [extract_features(log) for log in logs]
    df = pd.DataFrame(features)
    df.to_csv(path, index=False)
    return  

path = "ml-websecurity-model/app/labelled_dataset/attack_log.csv"
save_file(logs, path)
path = "ml-websecurity-model/app/labelled_dataset/normal_log.csv"
save_file(logs_V2, path)