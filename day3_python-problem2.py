positive = {"happy": 1, "great": 2, "good": 1, "helpful": 1, "amazing": 2, "love": 2}
negative = {"bad": -2, "sad": -1, "boring": -1, "never": -2, "terrible": -2, "unhelpful": -1, "bug": -2}
def score(text):
    total_score = 0
    cleaned_text = text.lower()
    # Split into words
    words = cleaned_text.split()
    for word in words:
        # Clean punctuation 
        word = word.strip(".?!,;:") 
        if word in positive:
            total_score += positive[word]
        elif word in negative:  
            total_score += negative[word]
    if total_score > 0:
        label = "positive"
    elif total_score == 0:
        label = "neutral"
    else:
        label = "negative"
    # Return the results
    return total_score, label
user_input = input("Say something.. ")
final_score, final_label = score(user_input)
print(f"Sentiment score: {final_score} ({final_label})")