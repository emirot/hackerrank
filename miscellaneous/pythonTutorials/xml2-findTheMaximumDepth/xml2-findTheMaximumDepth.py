__author__ = 'nolanemirot'


from xml.etree.ElementTree import XMLParser

class MaxDepth:                     # The target object of the parser
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
        pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        return self.maxDepth


def find_depth(chaine):
    target = MaxDepth()
    parser = XMLParser(target=target)
    exampleXml = """<feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
    </feed>"""
    parser.feed(chaine)
    print(parser.close()-1)

if __name__ == '__main__':
    xml = ""
    nbAttrib = 0
    nbTests =  int(input())
    for i in range(0, nbTests):
        xml += input()
    find_depth(xml)


