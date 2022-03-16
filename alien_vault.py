import requests


def verify_ipv4_node(node):
    api_url = "https://otx.alienvault.com/api/v1/indicators/IPv4/{}".format(node)
    r = requests.get(api_url)
    data = r.json()
    try:
        tags = []
        for pulse in data["pulse_info"]["pulses"]:
            for tag in pulse["tags"]:
                tags.append(tag)
        tags = list(set(tags))
        return {"tags":tags, "country_name":data["country_name"]}
    except Exception as e:
        return {"tags":[], "country_name":data["country_name"]}


