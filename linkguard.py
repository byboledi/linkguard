from urllib.parse import urlparse
import re

url = input("Enter a URL: ")

warnings = []

if not url.startswith("https://"):
    warnings.append("❌ Not using HTTPS")

suspicious_words = [
    "login",
    "verify",
    "password",
    "winner",
    "claim",
    "free-money"
]

for word in suspicious_words:
    if word in url.lower():
        warnings.append(f"⚠️ Suspicious keyword: {word}")

domain = urlparse(url).netloc

if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain):
    warnings.append("⚠️ Uses an IP address instead of a domain")

if len(url) > 75:
    warnings.append("⚠️ URL is unusually long")

print("\n===== LINKGUARD REPORT =====")

if warnings:
    for warning in warnings:
        print(warning)
else:
    print("✅ No obvious red flags detected")

print("============================")