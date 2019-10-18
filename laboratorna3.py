input_text = "task for third lab, lab of di"
#output: <div><b>task for third lab, lab of di</b></div>
# input_text = input("Input your text: ")

#this one open tags list
openList = ["<div>", "<b>"]

def wrap_di(my_function):
    def wrapped():
        global openList
        closeList = [] #this one close list
        for item in openList:
            output = [x for x in item]
            output.insert(1, "\\")
            output = "".join(output)
            closeList.append(output)

        openList = "".join(openList)
        closeList.reverse()
        closeList = "".join(closeList)

        return htmlList + my_function() + closeList

    return wrapped


@wrap_di
def text_processing():
    return input_text


print(text_processing())
