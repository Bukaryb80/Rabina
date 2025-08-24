from modules.translation import translate_text
from modules.investment import get_investment_advice
from interfaces.voice_chatbot import speak_text, listen_to_user

if __name__ == "__main__":
    translator_key = "YOUR_TRANSLATOR_API_KEY"
    translator_region = "YOUR_TRANSLATOR_REGION"
    marketstack_key = "YOUR_MARKETSTACK_API_KEY"

    # Translation
    original_text = "Hello, how are you?"
    target_lang = "fr"
    translated = translate_text(original_text, target_lang, translator_key, translator_region)
    print("Translated Text:", translated)
    speak_text(translated)

    # Investment Advice
    stock_symbol = "AAPL"
    advice = get_investment_advice(stock_symbol, marketstack_key)
    print("Investment Advice:", advice)
    speak_text(advice)