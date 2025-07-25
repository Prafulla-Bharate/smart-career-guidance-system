from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
import pandas as pd

def get_trends(keyword):
    pytrend = TrendReq(hl='en-US', tz=330)
    keyword = keyword.strip().lower()

    if not keyword or len(keyword) < 2:
        return {"error": "Invalid keyword"}
    
    try:
        pytrend.build_payload([keyword], timeframe='today 5-y')
        time_df = pytrend.interest_over_time().reset_index()
        region_df = pytrend.interest_by_region().reset_index()

        return {
            "time": time_df[['date', keyword]],
            "region": region_df[['geoName', keyword]]
        }
    except Exception as e:
        return {"error": str(e)}
