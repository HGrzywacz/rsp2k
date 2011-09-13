#!/usr/bin/env python

#head
h1 = ('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
h2 = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + "\n")
h3 = ('<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en-US">' + "\n" +"\n")
h4 = ('<head>' + "\n\t")
h5 = ('<meta name="dtb:uid" content="BookId"/>' + "\n\t" + '<meta name="dtb:depth" content="2"/>' + "\n\t" + '<meta name="dtb:totalPageCount" content="0"/>')
h6 = ("\n\t" + '<meta name="dtb:maxPageNumber" content="0"/>' + "\n" + '</head>' + "\n\t")




# h7 = ('<docTitle><text>' + index.title + '</text></docTitle>' + "\n")
# h8 = ('<docAuthor><text>' + index.author + '</text></docAuthor>' + "\n\n" + '<navMap>' + "\n")


h9 = ('<navPoint class="toc" id="toc" playOrder="1">' + "\n")
h10 = ('<navLabel>' + "\n" + '<text>Table of Contents</text>' + "\n" + '</navLabel>' + "\n")
h11 = ('<content src="toc.html"/>' + "\n" + '</navPoint>' + "\n\n")

#repeated for navpoints
# s1 = ('<navPoint class="' + section.filename + '" id="' + section.filename + '" playOrder="' + str(i) + "\">\n")
# s2 = ('<navLabel>' + "\n" + '<text>' + section.title + '</text>' + "\n" + '</navLabel>' + "\n")
# s3 = ('<content src="' + section.filename + '"/>' + "\n" + '</navPoint>' + "\n\n")

#bottom
b1 =('</navMap>' + "\n" + '</ncx>' + "\n")

