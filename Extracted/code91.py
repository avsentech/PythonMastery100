# Code #91: Scrape Headlines from a News Website
"""
    💡 Why This Matters?
    Used in:
    - 📰 Content aggregation bots
    - 📈 Sentiment and keyword analysis
    - 🧾 Monitoring current events for AI-driven tools
    - 📣 Real-time alerts or newsletter  
"""
# Tier: Intermediate
# Goal: Use requests and BeautifulSoap to extract headlines from a news page

# Python Code
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, tag="h3", class_name=None):
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Failed to load page:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    if class_name:
        headlines = soup.find_all(tag, class_=class_name)
    else:
        headlines = soup.find_all(tag)

    print("📰 Scraped Headlines:")
    for i, headline in enumerate(headlines[:10], start=1):
        text = headline.get_text(strip=True)
        print(f"{i}. {text}")

# Sample Usage

scrape_headlines("https://www.bbc.com/news", tag="h2", class_name=None)


# Sample Output
"""
    📰 Scraped Headlines:
        1. UK and 24 nations accuse Israel of 'drip feeding' aid to Gaza civilians as they condemn 'horrifying' killings
        2. At least 19 dead after air force jet crashes into Bangladesh school
        3. China begins building world's largest dam, fuelling fears in India
        4. Ryanair considers increasing bonus for staff who spot oversized bags
        5. China blocks Wells Fargo banker from leaving due to 'criminal case'
        6. At least 19 dead after air force jet crashes into Bangladesh school
        7. Watch: Bangladesh plane crash eyewitness describes moment he heard explosion
        8. Carmaking giant says Trump tariffs have cost it €300m
        9. Victims' families criticise report blaming pilot error for South Kor
"""
# Note: Actual results depend on the current sttructure and content of the webpage.


# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    requests.get()      Fetches the HTML content of the page
    BeautifulSoup       Parses the HTML into searchable DOM Structure
    find_all()          Filters tags like <h3> optionally by class
    get_text()          Extract clean headline text from each element
"""
# Use browser tools (Inspect Element) to find accurate tag/class names if structure changes.

# Real-World Connection
"""
    - Build a trending headlines dashboard
    - Feed curated news into Telegram bots or Slack notifications
    - Track keywords for podcasts or YouTube script planning
    - Analyze headline tone or frequency using NLP tools
"""
