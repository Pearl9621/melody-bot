good_things = ["awesome", "great", "cool", "good", "super", "interesting", "cute", "fun", "nice"]
bad_things = ["terrible", "stupid", "bad", "evil", "creepy", "weird", "crazy", "dumb"]

love_colours = ["lavender", "gray", "grey", "turquiose", "green"]
like_colours = ["pink", "orange", "brown", "violet", "magenta", "lime", "purple", "salmon", "coral", "chartreuse"]
dislike_colours = ["yellow", "blue", "hot pink", "burgandy", "indigo"]


    
def converse():
    def ask(question):
        answer = yield question
        answer = answer.strip().lower()
        return answer
        # return input(question + " ").strip().lower()

    answer = yield from ask("Hello, what do you think of me(Melody)?")

    if answer == "help":
        answer = yield from ask("I understand these answers: " + str(good_things + bad_things) + "?")

    if answer in good_things:
        yield "I already knew that."
    elif answer in bad_things:
        yield "Sure, you're the mortal."
    else:
        type_of_word = yield from ask("I don't know what '" + answer + "' means. Is it 'good' or 'bad'?")
        if type_of_word == "good":
            good_things.append(answer)
        elif type_of_word == "bad":
            bad_things.append(answer)
        else:
            yield "I don't understand"

        yield "Thanks for teaching me."


    # answer = ask("What colour do you think is the best?")

    # if answer in love_colours:
    #     print("I love that colour.")
    # elif answer in like_colours:
    #     print("I like that colour too but it's not my favourite.")
    # elif answer in dislike_colours:
    #     print("You have your own opinions.")
    # else:
    #     print("I don't know what '" + answer + "' looks like. Tell the creator to program me better.")


    # while 1:
    #     answer = ask("Ask me anything.")

    #     if answer == "what are you made of?": 
    #         print("NIGHTMARES.")
            
    #     elif answer == "what is your favourite animal?":
    #         print("Cats!")

    #     elif answer == "what is your favourite song?": 
    #         print("")

    #     elif answer == "what do you look like?":
    #         print("My form is not specific.")
            
    #     elif answer == "anything":
    #         print("Very funny.")

    #     elif answer == "goodbye":
    #         print("Farewell mortal!")
    #         break
    #    elif answer == "where do you come from"
    #          print ("Please don't make me answer that")
      
    #     else: 
    #         print("Try a different question, or tell the creator to program me better. ")

if __name__ == "__main__":
    cipher = converse()
    statement = next(cipher)
    try:
        while statement:
            if statement.endswith("?"):
                answer = input(statement + " ")
                statement = cipher.send(answer)
            else:
                print(statement)
                statement = next(cipher)
    except StopIteration:
        pass
