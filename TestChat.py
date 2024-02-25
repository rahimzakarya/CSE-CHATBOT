from Chat import get_response

while True:
    question = input("Enter a question: ")
    if question == "exit":
        break
    print(get_response(question))