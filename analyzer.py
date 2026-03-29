from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

pos_hints = {"loved", "excellent", "amazing", "perfectly cooked", "great ambiance", "highly recommended", "best", "superb", "very satisfying", "friendly", "delicious"}
neg_hints = {"terrible", "undercooked", "not worth", "bad experience", "oily", "slow delivery", "overpriced", "unhygienic", "awful", "wait forever", "worst", "bland", "cold", "rude", "stale"}
neutral_hints = {"okay", "average", "decent", "acceptable", "standard", "neither great nor bad", "met expectations", "could be better", "passable", "nothing special", "regular", "quick meal"}

def count_hints(text, cues):
    return sum(1 for cue in cues if cue in text)  

def analyze_feedback(text):  
    text = str(text)
    low = text.lower()
    points = sia.polarity_scores(text)  
    compound = points['compound']
    pos_hit = count_hints(low , pos_hints)
    neg_hit = count_hints(low, neg_hints)
    neutral_hit = count_hints(low , neutral_hints)
# threshold tweaking (hit and try)
    adjusted = compound + (0.12 * pos_hit) - (0.12 * neg_hit) - (0.05 * neutral_hit)
    adjusted = max(-1.0, min(1.0, adjusted))
    if neutral_hit > 0 and pos_hit == 0 and neg_hit == 0 and abs(adjusted) < 0.45:
        sentiment = "Neutral"
    elif adjusted >= 0.12:
        sentiment = "Positive"
    elif adjusted <= -0.12:
        sentiment = "Negative"  
    else: 
        sentiment = "Neutral"

    return {
        "feedback": sentiment ,
        "points": round(adjusted,  2)
    }

def analyze_lst(reviews):
    results = []
    for review in reviews:
        result = analyze_feedback(review)
        result["review"] = review
        results.append(result)
    return results
