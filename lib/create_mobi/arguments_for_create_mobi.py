"""Name is self-explanatory."""


class MetaData(object):
    'Metadata container'
    

    creator = str()
    title = str()
    language = str()
    date = str()


class ReadyFile(object):
    'Description of rhtml file'


    filename = str()
    name = str()

    def __init__(self, filename=None, name=None):
        self.filename = filename
        self.name = name


class ReadyFiles(list):
    'List of ready files'


    directory = str()

    def add(self, filename, name):
        self.append(ReadyFile(filename, name))


