


def checkString(s):
    for e in s:
        if e not in ['{','}','[',']','(',')']:
            return False
    return True


def leftDelimiter(deli):
    if deli == '(' or deli == '[' or deli == '{':
        return True
    return False

def rightDelimiter(deli):
    if deli == ')' or deli == ']' or deli == '}':
        return True
    return False



def checkPair(a,b):
    if a == '{'  and b =='}':
        return True
    if a == '['  and b ==']':
        return True
    if a == '('  and b ==')':
        return True
    return False


def balancedDelimiter(s):
    if len(s) % 2 != 0:
        print("unbalanced")
        return False
    i = 0
    st = []
    while i < len(s):

        if leftDelimiter(s[i]):
            st.append(s[i])
        elif rightDelimiter(s[i]):
            if len(st) > 0:
                a = st.pop()
                if not checkPair(a,s[i]):
                    print("Not balanced")
                    return False
            else:
                print("stack empty")
        else:
            print("not good delimiter")
            return False
        i+=1
    print("balanced")


#balancedDelimiter("{ad}sakdmsad")
balancedDelimiter("[({[]})]")
