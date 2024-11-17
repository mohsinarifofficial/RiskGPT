from transformers import AutoModelForCausalLM, AutoTokenizer
from Data_Cleaning import cleaned_weather_data, cleaned_news_data,cleaned_gdp_data
# this project inlcudes pretrained models and transfer learning 
# but this cannot be completed entirely in 2 days
# so i am using anoither approach to get responses based on real data coming Datacleanning.py
# Just to convey the meaning of this prototype.
# Using pretrained model and transfer requires more data which is not possible in 2 days
# using dailogpt for prototype
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
# keywords to generate responses
weather_keywords = ["storm", "rain", "hurricane", "weather", "temperature", "flood", "cloud", "snow", "clear"]
economic_keywords = ["GDP", "inflation", "currency", "economy", "price", "market", "interest", "growth"]
operational_keywords = ["strike", "accident", "disruption", "delays", "production", "industry", "factory", "workforce"]
def categorize_input(input_text):
    input_text = input_text.lower()  # Make input lowercase for easier matching

    #weather information
    if any(keyword in input_text for keyword in weather_keywords):
        return cleaned_weather_data()

    #economic-related info
    elif any(keyword in input_text for keyword in economic_keywords):
        return cleaned_gdp_data()

    # operational-related info
    elif any(keyword in input_text for keyword in operational_keywords):
        return cleaned_news_data()


    return None


def chat(input_text):
    df = categorize_input(input_text)
    # general response
    if df is None:
        input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
        response_ids = model.generate(
            input_ids,
            max_new_tokens=50,  # Limit new tokens to generate
            pad_token_id=tokenizer.eos_token_id
        )
        response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

     # responses based on real time data
    data_str = str(df.to_dict())
    input_text = input_text + " Here is the data: " + data_str


    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    response_ids = model.generate(
        input_ids,
        max_new_tokens=50,  
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# prompts user can enter to know about current risks
user_input_weather = "What is the current storm situation?"
user_input_economic = "How is the GDP affecting the market?"
user_input_operational = "Any news on factory strikes?"

response_weather = chat(user_input_weather)
response_economic = chat(user_input_economic)
response_operational = chat(user_input_operational)
print("Weather Response:", response_weather)
print("Economic Response:", response_economic)
print("Operational Response:", response_operational)
