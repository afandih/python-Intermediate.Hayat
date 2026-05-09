#THE LOGIC OF AI - CONCEPTUAL FRAMEWORK
#NAME: HAYAT /UTM PYTHON WORKSHOP

#AI HIERARCHY

#AI
 # Machine Learning
    # Supervised Learning
    # Unsupervised Learning
    # Reinforcement Learning
             # Deep Learning
              #Neural Networks



#AI   = machine that think
#ML   = machines that Learn from data
#Deep = ML using brain-like layer


#logic gap 
#traditional programming:
# Machine finds the rules maanually
# Input: Data + Output: Answer
# Example: if temperature > 90: send_alert()


#MACHINE LEARNING:
#    Machine finds the rules itself
#    Input: Data + rule -> Output: Rules (patterns)
#    Example: model learns WHEN to alert by studying past data


#THE GAP:
#   Traditional = YOU teach every rule
#  ML          +machine DISCOVERS the rule alone


#PART 3: 3 TYPES OF LEARNING

#SUPERVISED LEARNING
#      - Data has labels(correct answer)
#      -model learns from examples
#      -example: Email-> Spam or not Spam

#UNSUPERVISED LEARNING
#    - Data has No labels
#    - Gets reward for good actions
#    - Robot learns to walk

#PART4: 5 ENGINEEERING SCENARIOS

#1. PREDICT FACTORY MACHINE FAILURE
#   Type: SUPERVISED 
#   Why:  Historical data labeled (failed/ not failed)


# 2. Detect spam emails
#    Type: SUPERVISED
#    Why: Emails already labeled spam or not spam

# 3. Group customers by buying habits
#    Type: UNSUPERVISED
#    Why: No labels — model finds hidden groups itself

# 4. Robot learning to sort packages
#    Type: REINFORCEMENT
#    Why: Trial, error, and reward system

# 5. Detect unusual factory sensor readings
#    Type: UNSUPERVISED
#    Why: No labels — model detects abnormal patterns

# ─────────────────────────────────────────────
# PART 5: TITANIC — WHICH LEARNING TYPE?
# ─────────────────────────────────────────────

# Answer: SUPERVISED LEARNING
#
# Why?
# - We already HAVE the answer (Survived = 1 or 0)
# - Model trains on past passengers with known results
# - Then predicts survival for a NEW unknown passenger
#
# Features used:
# - Pclass, Sex, Age, Fare, Embarked
#
# This is Supervised Classification:
# Input: passenger details → Output: Survived (Yes/No)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("titanic.csv")
df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]].dropna()
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Predict a new passenger
new_passenger = [[3, 0, 25, 7.5]]  # 3rd class, male, age 25
result = model.predict(new_passenger)
print("Survived" if result[0] == 1 else "Did Not Survive")


# PART 6: WHY CLEAN DATA > COMPLEX ALGORITHM


# GOLDEN RULE: "Garbage In = Garbage Out"
#
# Bad Data + Complex Algorithm = WRONG results
# Good Data + Simple Algorithm = CORRECT results
#
# Why clean data matters more:
# 1. Dirty data teaches the model WRONG patterns
# 2. Model accuracy depends on data quality first
# 3. No algorithm can fix fundamentally bad data
# 4. In hospitals/factories — wrong predictions = danger
#
# Week 1 (Clean Data) → Week 2 (ML Model) → Accurate Predictions

print("\n=== DAY 8 COMPLETE ===")
print("AI > ML > Deep Learning")
print("Supervised | Unsupervised | Reinforcement")
print("Clean Data > Complex Algorithm")

