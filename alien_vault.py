import requests


def verify_ipv4_node(node):
    api_url = "https://otx.alienvault.com/api/v1/indicators/IPv4/{}".format(node)
    r = requests.get(api_url)
    data = r.json()
    try:
        tags = []
        for tag in data["pulse_info"]["pulses"][0]["tags"]:
            tags.append(tag)
        return {"tags":tags, "country_name":data["country_name"]}
    except Exception as e:
        return False


