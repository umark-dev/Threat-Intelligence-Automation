import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your AbuseIPDB API key

input_file = "ips.txt"
output_file = "report.txt"

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        score = data["data"]["abuseConfidenceScore"]

        if score > 50:
            return f"[ALERT] Malicious IP: {ip} (Score: {score})"
        else:
            return f"[OK] Clean IP: {ip} (Score: {score})"
    else:
        return f"[ERROR] Could not check IP: {ip}"


def main():
    with open(input_file, "r") as file:
        ips = file.read().splitlines()

    results = []

    for ip in ips:
        result = check_ip(ip)
        print(result)
        results.append(result)

    with open(output_file, "w") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == "__main__":
    main()