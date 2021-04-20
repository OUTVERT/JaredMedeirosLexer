#JARED MEDEIROS
#COMP340 HW5




def tokenize(string):  # method tokenize
    lis = []  # empty list to return

    for i in range(0, len(string)):
        dic = {}
        if string[i] == "(":
            dic["type"] = "LPAREN"
            dic["value"] = string[i]
        elif string[i] == ")":
            dic["type"] = "RPAREN"
            dic["value"] = string[i]
        elif string[i].isdigit():
            if string[i - 1].isdigit():
                continue

            val = ""
            while string[i].isdigit():  # while the string[i] is digit add the string[i] to value
                val = val + string[i]
                i += 1

            dic["type"] = "NUMBER"
            dic["value"] = val
        elif string[i] == "+":
            dic["type"] = "PLUS"
            dic["value"] = string[i]
        elif string[i] == "-":
            dic["type"] = "MINUS"
            dic["value"] = string[i]
        elif string[i] == "*":
            dic["type"] = "MULTIPLICATION"
            dic["value"] = string[i]
        elif string[i] == "/":
            dic["type"] = "DIVISION"
            dic["value"] = string[i]

        dic = dotdict(dic)  # making the dictionary keys,values to be able to access by the Dot(.) operator
        lis.append(dic)  # add the dictionary to the list

    return lis  # return the list


class dotdict(dict):  # class to make the dictionary values to be able to accessed by DOT(.) operator
    __getattr__ = dict.get

