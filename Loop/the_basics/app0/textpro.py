# messages = []
# while True :
#     flag = False
#     listOfQuestion = ["when", "how", "what"]
#     msg = input("Say something: ")

#     for val in listOfQuestion :
#         if msg.__contains__(val) :
#             flag = True
#         else :
#             pass
    
#     if flag :
#         messages.append(msg.capitalize() + "?")
#     else :
#         messages.append(msg.capitalize() + ".")

#     if msg == '\end' :
#         for val in messages :
#             if(val == '\end.') :
#                 pass
#             else :
#                 print(val, end=" ")
#         break
#     else :
#         continue

def sentence_maker(phrase) :
    interrogatives = ('how', 'what', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives) :
        return "{}?".format(capitalized)
    else :
        return "{}.".format(capitalized)

results = []
while True :
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else :
        results.append(sentence_maker(user_input))

print(" ".join(results))