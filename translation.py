import requests

def translate_text(text, target_language, subscription_key, region):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    params = {"api-version": "3.0", "to": target_language}
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json"
    }
    body = [{"text": text}]
    response = requests.post(endpoint, params=params, headers=headers, json=body)
    response.raise_for_status()
    return response.json()[0]['translations'][0]['text']