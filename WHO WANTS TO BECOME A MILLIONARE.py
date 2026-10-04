questions = [ 
    ["who is guneesh kohli?", "hero", "a gym boy", "a passionate boy who is passionate for his future", "a studios boy", 3],
    ["which is my best place?", "punjab", "kashmir", "indore", "kalburgi", 1],
    ["my roommate name is?", "prakshit", "pranav", "ketan", "mayank", 1],
    ["my favourite part of my body?", "chest", "biceps", "penis", "shoulders", 3],
    ["Who painted the Mona Lisa?", "GUNEESH KOHLI", "PRAKSHIT", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i=0
for question in questions:
    print("\n" + question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    correct = int(input(" enter the correct answer for the question 1 for a,2 for b, 3 for c, 4 for d ?\n"))

    if question[5] == correct:
        print("✅ CORRECT ANSWER")
    else:
        print("❌ WRONG ANSWER 😭😭 BETTER LUCK NEXT TIME")  
        break   
    
    print(f" you won rupees: {prizes[i]}")
    i+=1

