import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"DX5P8x5jksrpLaLkmFvUk7uXlhkAtedSO4Jyd6XciOVPNMp4AXlyDM7cnq8t","message":"This is test message","language":"english","route":"q","numbers":"7972846137,9420597784"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)