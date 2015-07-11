__author__ = 'nolanemirot'

import re

a='^[0-9]{5}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'

n = int(input())
for i in range(n):
    s = input()
    if re.match(a, s):
        print("VALID")
    else:
        print("INVALID")