opf = []

opf.append('<?xml version="1.0" encoding="utf-8"?>' + "\n")
opf.append('<package unique-identifier="uid">' + "\n")
opf.append("\t" + '<metadata>' + "\n")
opf.append("\t\t" + '<dc-metadata xmlns:dc="http://purl.org/metadata/' +
            'dublin_core" xmlns:oebpackage="http://openebook.org/' +
            'namespaces/oeb-package/1.0/">' + "\n")\
#opf.append("\t\t" + '<dc:Title>Sparknotes: ' + index.title + '</dc:Title>' + "\n")
#opf.append("\t\t" + '<dc:Creator>Sparknotes</dc:Creator>' + "\n")
#opf.append("\t\t" + '<dc:Language>en-us</dc:Language>' + "\n")
opf.append("\t\t" + '<dc:Identifier id="uid">9095C522E6</dc:Identifier>' + "\n")
opf.append("\t" +  '</dc-metadata>' + "\n" + "\n")
opf.append("\t" + '<x-metadata>' + "\n")
opf.append("\t\t" + '<output encoding="utf-8"></output>' + "\n")
opf.append("\t\t" + '<EmbeddedCover>cover.jpg</EmbeddedCover>' + "\n")
opf.append("\t" + '</x-metadata>' + "\n" + '</metadata>' + "\n" + "\n")

# manifest
opf.append('<manifest>' + "\n")
opf.append('<item id="item1" media-type="application/xhtml+xml" href="toc.html"></item>' + "\n")


# repeated for every file
#opf.append('<item id="item' + str(i) + '" media-type="application/xhtml+xml" href="' + section.filename + '"></item>' + "\n")


opf.append('<item id="My_Table_of_Contents" media-type'
        + '="application/x-dtbncx+xml" href="toc.ncx"/>' + "\n")

opf.append('</manifest>' + "\n")

#spine
opf.append('<spine toc="My_Table_of_Contents">' + "\n")
opf.append('<itemref idref="item1"/>' + "\n")

#repeated for every file
#opf.append('<itemref idref="item' + str(i) + '"/>' + "\n")

opf.append('</spine><tours></tours><guide></guide></package>' + "\n")



