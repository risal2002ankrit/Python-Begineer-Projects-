# a dictonary that stores question and answers
# have a varaiable that tracks score of player
# loop through the dictonary using key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1":{
        "question": " what is the capital of france?",
        "answer": "Paris"
    },
    "question2":{
        "question": " what is the capital of germany?",
        "answer": "Berlin"

    },

    "question2": {
        "question" : " what is the capital of Italy?",
        "answer" : "Rome"
    },
    "question3": {
        "question" :" what is the capital of Spain?",
        "answer" : "Madrid"
    }
}

score= 0
for key, value in quiz.items():
    print(value['question'])
    answer= input("Answer?")

    if answer.lower()== value['answer'].lower():
        print('correct')
        score= score+1
        print("your score is:"+ str(score))

    else:
        print("wrong!")
        print("the answer is ;"+ value['answer'])
        print("your score is:"+ str(score))
        print("")
        print("")

print("you got" + str(score) +"out of 3 questions correctly")
print("your percentage is"+str(score/3 * 100)+"%")

