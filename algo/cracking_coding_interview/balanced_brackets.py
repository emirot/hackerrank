
def is_opposite(a, b):
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    return False

def is_matched(expression):
    stack = []
    for e in expression:
        if '(' == e or '[' == e or '{' == e:
            stack.insert(0, e)
        elif ')' == e or '}' == e or ']' == e:
            try:
                a = stack.pop(0)
                #print("a,e: {}{}".format(a,e))
                if is_opposite(a, e) == False:
                    return False
            except:
                return False
    if len(stack) > 0:
        return False
    return True
            
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
