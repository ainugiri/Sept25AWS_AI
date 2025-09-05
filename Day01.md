Artificial Intelligence

Artificial : Man made 
Intelligence : The ability to acquire and apply knowledge and skills.

1956 - Dartmouth Conference: The birth of AI as a field.
Computer Generation at 1956 : The first generation of computers, characterized by vacuum tubes and magnetic drums.
 - Vacuum tubes
 - Magnetic drums
 - functions: Basic arithmetic operations, data storage and retrieval

Computer can think like human, performs tasks such as learning.


Rule Based AI:
 - No Learning
 - Finite set (input - output)
 - Signal (red - Stop, green - Go, yellow - Caution)

MYCIN: Rule based expert system for diagnosing bacterial infections and recommending antibiotics.
input: Patient symptoms and medical history
output: Recommended antibiotics based on rules and patient data
Rule based system 1-1 mapping, then it will useful for specific cases.

But multiple value for a single input can lead to ambiguity and requires more complex rules or additional context to resolve.


1970 - Winter Period, AI research funding decreased, many projects halted.

Machine Learning:
 - Learn from data
 1 year old car sold for 18000,17900,17950,18100,18000,18000,18000,18000
 2 year old car sold for 16000,15900,15950,16100,16000,16000,16000,16000

 <!-- Historical Data -->
 <!-- 17900 to 18100  -->
 <!-- average for 18000,17900,17950,18100,18000,18000,18000,18000 = 18012.5 -->
 <!-- propose 18050 -->

learn from data
pattern recognition
prediction

Machine Learning: 
    - Data preprocessing
    - Feature engineering (selecting relevant features, transforming variables)
    <!-- car : feature: age, mileage, brand, condition, noofowners, kms driven -->
    - Model Selection (choosing the appropriate algorithm)

    Machine Learning :
        1. Supervised Learning
            Learning through labeled data

           input and output are labeled
           age, mileage,    noofowners, price
           1,   20kmpl,     1,          20000
           1,   19kmpl,     1,          19000
           1,   21kmpl,     1,          21000
           1,   20kmpl,     2,          19500
           1,   20kmpl,     1,          20000

        2. Unsupervised Learning
            Learning through unlabeled data
        3. Semi-Supervised Learning
            Combination of labeled and unlabeled data
            Useful when acquiring a fully labeled dataset is expensive or time-consuming
            Example: Using a small amount of labeled data to guide the learning process on a larger set of unlabeled data

        4. Reinforcement Learning
            Learning through interaction with an environment
            Agent takes actions and receives feedback in the form of rewards or penalties

        

        labelled data
        age, mileage, noofowners -> price
        1,   20kmpl,     1   12000
        1,   19kmpl,     1   11500
        1,   21kmpl,     1   12500
        1,   20kmpl,     2   13000



SUPERVISED LEARNING:
    Learned from labeled data
    W.r.t prediction:
        1. Regression: Predicting a continuous value (e.g., price)

Car Price Prediction:
Age, Price
1, 20000
1, 19950
1, 20050
1, 20000
1, 20000
2, 18000
2, 17950
2, 18100
2, 18000


input a-  age 
predict price: value => based on existing data / pattern

Regression: Predicting a continuous value (e.g., price)



75,80,85,75 -> B Grade
85,87,80,93 -> A Grade
90,91,92,93 -> A Grade
95,96,97,98 -> O Grade

Classification Algo: Predict the Group
input 4 values: 75, 80, 85, 75 : B Grade ->  Group / Classify 



Regression Algorithm: Predicting a continuous value (e.g., price)
a. Linear Regression
b. Polynomial Regression 

Deep Learning:
Special form of Machine Learning
- Uses neural networks with many layers (deep networks)
- Capable of learning complex patterns and representations
- Requires large amounts of data and computational power
- Applications: Image recognition, natural language processing, speech recognition


ML vs DL
- ML (Machine Learning):
  - Traditional algorithms (e.g., decision trees, SVM)
  - Requires feature engineering
  - Works well with structured data
- DL (Deep Learning):
  - Neural networks with many layers
  - Automatic feature extraction
  - Works well with unstructured data (e.g., images, text)


Generative AI:
Generate New Content

LLM 
   DL + NLP
   NLP : Natural Language Processing
   NLP: NLU, NLG

   NLP: System is able to understand and generate human language
   NLU: 
        System, able to understand human language and perform tasks 
        Siri, Alexa, Voice Assistats
         
         Hey Siri, set an alarm for 7 AM tomorrow.

         1. Tokenization: Breaking down the input into individual words or tokens
         2. Named Entity Recognition (NER): Identifying and classifying key entities (e.g., time, date, place, city, company name)
         3. Intent Recognition: Understanding the user's intent (e.g., setting an alarm)
         4. Lemmatization: Reducing words to their base or root form (e.g., "running" to "run")
         5. Stemming: Reducing words to their base or root form (e.g., "running" to "run")
         6. Stopword Removal: Eliminating common words that may not carry significant meaning (e.g., "and," "the," "is")
         7. Part of Speech Tagging: Identifying the grammatical category of each word (e.g., noun, verb, adjective)

         semantic functions
         sentiment analysis: Determining the emotional tone behind a series of words
         intent detection - what user wants

         1. User says: "Set an alarm for 7 AM tomorrow."
         2. System identifies intent: "Set Alarm"
         3. Extracts entities: Time (7 AM), Date (Tomorrow)

    NLU: Siri, Alexa, Google Assistant. Perform tasks based on user input text, voice 

    NLG: Generate human-like text responses (e.g., chatbots, virtual assistants)
    12 months sales raw data -> NLG -> Report based products, sales trends, customer insights, monthwise reports, visualizations. 

    NLG : is created to process raw data and generate human-like text outputs.
    it can be a report result, visualization, or any other form of text-based information.\


LLM - DL & NLP
   - LLM (Large Language Model)
   - DL (Deep Learning): to work on large datasets and complex patterns
   - NLP (Natural Language Processing) : to understand and generate human language with context from DL
   - Dialog Management: to handle conversations and maintain context over multiple turns
   Conversational AI

   GPT - LLM
   ChatGPT is Conversational AI based on LLM.