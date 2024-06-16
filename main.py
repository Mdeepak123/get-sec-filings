from sec_api import QueryApi, ExtractorApi
import pandas as pd

api_key = ""  
company_ticker = "" 

def get_most_recent_filing(api_key, company_ticker):
    # Set the endpoint URL
    url = "https://api.sec-api.io"

    query = {
    "query": f"ticker:{company_ticker} AND formType:\"10-Q\"",
    "from": "0",
    "size": "1",
    "sort": [{ "filedAt": { "order": "desc" } }]
    }
    queryApi = QueryApi(api_key=api_key)
    response = queryApi.get_filings(query)
    return response


#most recent quarterly filing
res = get_most_recent_filing(api_key,company_ticker)
filings = pd.DataFrame.from_records(res['filings'])

#extract sections using the link
extractorApi = ExtractorApi(api_key)
link = filings.loc[:,"linkToHtml"][0]
risk_factors = extractorApi.get_section(link, "part2item1a", "text")

print(risk_factors)

