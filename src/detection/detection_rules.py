HIGH_RISK_IPS = [
    "185.220.101.1",
    "45.33.32.156",
    "103.21.244.0"
]

MALICIOUS_DOMAINS = [
    "malware-test.com",
    "bad-domain.net",
    "evil-site.org"
]

RISK_SCORE_THRESHOLD = 80


def is_high_risk_ip(ip):
    return ip in HIGH_RISK_IPS


def is_malicious_domain(domain):
    return domain in MALICIOUS_DOMAINS


def is_high_risk_score(score):
    return score >= RISK_SCORE_THRESHOLD

