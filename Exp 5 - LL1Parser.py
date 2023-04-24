def constructParseTable(productions,first,follow):
    parseTable=[]
    for i in range(len(nonTerminals)):
        lst=[]
        for j in range(len(terminals)):
            lst.append(0)
        parseTable.append(lst)
    print(parseTable)
    for prod in productions:
        prodS=prod.split("->")
        #now checking for the RHS
        firstElem=prodS[1][0]
        lhs=prodS[0]
        if firstElem in terminals:
            parseTable[nonTerminals.index(lhs)][terminals.index(firstElem)]=prod
        elif firstElem=='@':
            followSet=follow[lhs]
            for elem in followSet:
                parseTable[nonTerminals.index(lhs)][terminals.index(elem)] = prod
        else:
            firstSet=first[lhs]
            for elem in firstSet:
                if elem!='@':
                    parseTable[nonTerminals.index(lhs)][terminals.index(elem)] = prod
    print(parseTable)
    return parseTable

def verifyString(strToParse,parseTable):
    buffer=strToParse+"$"
    stack=[]
    #initially the stack is filled with the stack symbol '$'
    stack.append('$')
    stack.append('S')
    ptr=0
    while True:
        if stack[-1] in nonTerminals:
            prod=parseTable[nonTerminals.index(stack[-1])][terminals.index(buffer[ptr])]
            stack.pop(-1)
            prod=prod.split("->")
            if(prod[1]!='@'):
                for i in range(len(prod[1]) - 1, -1, -1):
                    stack.append(prod[1][i])
        elif stack[-1]==buffer[ptr]!='$':
                ptr+=1
                stack.pop(-1)
        elif stack[-1]==buffer[ptr]=='$':
            if len(stack)==1:
                print("Valid sting")
            break
        elif stack[-1]=='$':
            print("Invalid string")
            break
    print(buffer)
    print(stack)

prods=int(input("Enter the number of productions"))
productions=[]
print("Enter the productions one by one")
for _ in range(prods):
    productions.append(input())
print(productions)
nonTerminals = [i for i in input("Enter the nonterminals as comma seperated").split(",")]
terminals=[i for i in input("Enter the terminals as comma seperated").split(",")]

first = {}
follow = {}
for _ in range(len(nonTerminals)):
    nonTerminal = input("Enter the nonterminal")
    print("Enter the elements in its first set seperated by comma")
    first[nonTerminal] = {i for i in input().split(",")}
    print("Enter the elements in its follow set seperated by comma")
    follow[nonTerminal] = {i for i in input().split(",")}
print(first)
print(follow)
strToParse = input("Enter the string to be parsed")
parseTable=constructParseTable(productions,first,follow)
verifyString(strToParse,parseTable)
