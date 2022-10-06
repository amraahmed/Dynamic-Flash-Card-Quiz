from urllib import response
import requests
para = {
    "amount":10,
    "type":"boolean"
}
res = requests.get("https://opentdb.com/api.php",params=para)
res.raise_for_status()
data = res.json()
question_data = data["results"]
