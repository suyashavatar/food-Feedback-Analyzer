import pandas as pd
# import nltk
#    nltk.download('vader_lexicon')    # run only once
from analyzer import analyze_lst, analyze_feedback

print("resturant feedback analyzer")
print("1.with csv file ")
print("2.with sentences (type exit to stop) ") 
user_in = input("Enter your choice(1/2): ")

#  CSV analysis
if user_in == "1":
    file = input("\nEnter csv file path  : ")
    print(f"working on {file}")
    df = pd.read_csv(file)
# find what we neeed to analyze 
    if "review" not in df.columns:
        print("Couldn't find 'review' column. Available columns:")
        print(df.columns.tolist())
        exit()
    
    feedback = df["review"].tolist()
    print(f"Found {len(feedback)} entries")
    print("Analyzing feedbacks......")
    print("------")
    results = analyze_lst(feedback)  
    pos_hit = 0
    neg_hit = 0
    neutral_hit = 0 
    for r in results:
        feedback = str(r["feedback"]).strip().lower()
        if feedback == "positive":
            pos_hit += 1
        elif feedback == "negative":
            neg_hit  += 1
        else:
            neutral_hit +=  1  
    print("RESULTS")
    print("-------")
    print(f"Total Entries: {len(results)}")
    print(f"Positive: {pos_hit}")   
    print(f"Negative: {neg_hit}")
    print(f"Neutral:  {neutral_hit}")  
    df["analyzed_feedback"] = [r["feedback"] for r in results]
    df["analyzed_points"] = [r["points"] for r in results]  
    out_file =  file.replace(".csv", "_scanned.csv")
    df.to_csv(out_file, index=False)
    print(f"\nresults saved to: {out_file}")
#  sentence analysis 
elif user_in == "2":
    print("\ngive one sentence (type exit to quit):\n") 
    while True: 
        user_in2 = input("Enter sentence: ")
        if user_in2.lower()  == "exit":
            print("SEE YOU!!!!")
            break
        result = analyze_feedback(user_in2)
        print(f"feedback: {result['feedback']}")
        print(f"points: {result['points']}\n")
else:
    print("Please enter 1 or 2 only")