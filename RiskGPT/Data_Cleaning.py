import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Data_API import get_weather_data, get_news_data, get_gdp_data_usa
def cleaned_weather_data():
    weather_data = get_weather_data()
    weather_df = pd.json_normalize(weather_data)
    return weather_df
# analyze news article. 
# can be very helpful for operational risks
def cleaned_news_data():
    news_data = get_news_data()
    sid = SentimentIntensityAnalyzer()
    articles = news_data.get("data", [])
    for article in articles:
        article["sentiment"] = sid.polarity_scores(article["title"])["compound"]
    news_df = pd.DataFrame(articles)
    news_df = news_df[["title", "sentiment", "description", "url"]]
    return news_df
# Compute year-over-year percentage changes in GDP values
def cleaned_gdp_data():
    gdp_data = get_gdp_data_usa()
    gdp_df = pd.DataFrame(gdp_data)
    gdp_df = gdp_df[["date", "value"]].sort_values("date").dropna()
    gdp_df["gdp_change"] = gdp_df["value"].pct_change() * 100
    gdp_df.rename(columns={"value": "GDP in USD", "gdp_change": "Yearly Change (%)"}, inplace=True)
    return gdp_df
# print(cleaned_gdp_data())
# print(cleaned_news_data())
# print(cleaned_weather_data())
