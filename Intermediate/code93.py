# Code #93: Clean, Summarize & Format Text for Content Automation
"""
    💡 Why This Matters?
    Used in:
    - 🎥 Extracting key takeaways from transcripts
    - ✨ Condensing messy input into polished snippets
    - 🧠 AI-powered content repackaging
    - 📰 Creating headlines, tweet threads, or summarie
"""
# Tier: Intermediate
# Goal: Use Python to clean and structure input text, then generate a summary using NLP tools

# Python Code (Using sumy and re)
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def clean_text(text):
    # Remove extra whitespace, special characters, timestamps

    text = re.sub(r'\s+', ' ',text)  # collapse spaces

    text = re.sub(r'\[\d{1,2}:\d{2}(?:[:\d{2}]*)]', '', text) # remove timestamp

    text = re.sub(r'[^A-Za-z0-9.,?! ]+', '', text)    # Keep basic punctuation

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return "\n".jin(str(sentence) for sentence in summary)

# Sample Usage

raw_content = """
[00:01] Welcome to Python mastery. We're diving deep into automation. 
This module focuses on using APIs to streamline tasks. We'll build tools like currency converters, weather bots, and shorteners.
"""

cleaned = clean_text(raw_content)
summary = summarize_text(cleaned, sentence_count=2)

print("✅ Cleaned Text:\n", cleaned)
print("\n🧠 Summary:\n", summary)

# Concept Breakdown
"""
    Concept                     Description
    ----------------------------------------
    re.sub()                    Cleans timestamps and unwanted characters
    sumy.LsaSummarizer          NLP module to extract key sentences
    PlaintextParser             Converts cleaned text for NLP summarization
"""
# Extendable with other algorithms like LexRank, Luhn, or integrate Hugging Face transormers for deeper AI summerization

# Real-World Connection
"""
    - 🔄 Repackaging podcast/video transcripts
    - 📦 Generating titles and takeaways for newsletters
    - 🧠 Automating executive summaries of documents
    - 🤖 Content optimization inside RepurposePro’s pipeline
"""