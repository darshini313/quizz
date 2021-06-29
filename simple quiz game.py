class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What does the AC button on a calculator stand for?\n (a)All Conditions\n(b)All Clear",
     "How many elements are there in the periodic table?\n(a)118\n(b)119",
     "What was the most streamed show on Netflix in 2020?\n(a)The Last Dance\n(b)Money Heist",
     "Typically, what is the weakest muscle in the human body?\n(a)stapedius\n(b)clavicle",
     "How many countries are there in the world?\n(a)193\n(b)194",
     "In what year was the first iPhone released?\n(a)2009\n(b)2007",
     "What was the name of the first man-made satellite launched by the Soviet Union in 1957?\n(a)Sputnik 1\n(b)INSAT-1A",
     "In which direction does the sunrise?\n(a)West\n(b)East",
     "Which is the world’s largest flower?\n(a)Rafflesia\n(b)Sunflower",
     "Which is the continent with the most number of countries?\n(a)Africa\n(b)Asia",
     
]

questions = [
     Question(question_prompts[0], "b"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
     Question(question_prompts[5], "b"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "a"),
     Question(question_prompts[9], "a"),
            
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)

