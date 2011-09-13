import os
import sys
import webbrowser
from . import arguments_for_create_mobi as arguments
from . import toc_strings as tc
from . import ncx_strings as ncx
from .opf_strings import opf


def create_mobi(readyfiles, metadata):
    create_toc(readyfiles)
    create_ncx(readyfiles, metadata)
    create_opf(readyfiles, metadata)


def create_toc(rfs):

    filename = os.path.join(rfs.directory, 'toc.html')

    if os.path.exists(filename):
        print("toc.html file already exists. Nothing changed.")
        return

    print('Creating toc.html')


    f = open(filename, 'w')

    f.write(tc.h1)
    f.write(tc.h2)
    f.write(tc.h3)
    f.write(tc.h4)
    f.write(tc.h5)

    for rf in rfs:
        f.write('<li><a href="' + rf.filename + '">' + rf.name +
                '</a></li>' + "\n")

    f.write(tc.b1)
    f.close()


def create_ncx(rfs, md):

    filename = os.path.join(rfs.directory, 'toc.ncx')

    if os.path.exists(filename):
        print('toc.ncx file already exists. Nothing changed.')
        return

    print('Creating toc.ncx')


    f = open(filename, 'w')

    f.write(ncx.h1)
    f.write(ncx.h2)
    f.write(ncx.h3)
    f.write(ncx.h4)
    f.write(ncx.h5)
    f.write(ncx.h6)

    f.write('<docTitle><text>' + md.title + '</text></docTitle>' + "\n")
    f.write('<docAuthor><text>' + md.creator + '</text></docAuthor>' + "\n\n"
            + '<navMap>' + "\n")

    f.write(ncx.h9)
    f.write(ncx.h10)
    f.write(ncx.h11)

    for rf in rfs:
        i = rfs.index(rf) #NOT SURE IF RIGHT OR +1
        f.write('<navPoint class="' + rf.filename + '" id="'
                + rf.filename + '" playOrder="' + str(i) + "\">\n")
        f.write('<navLabel>' + "\n" + '<text>' + rf.name
                + '</text>' + "\n" + '</navLabel>' + "\n")
        f.write('<content src="' + rf.filename + '"/>'
                + "\n" + '</navPoint>' + "\n\n")

    f.write(ncx.b1)

    f.close()


def create_opf(rfs, md):

    filename = os.path.join(rfs.directory, 'book.opf')

    if os.path.exists(filename):
        print('book.opf file already exists. Nothing changed.')
        return

    print('Creating book.opf')


    f = open(filename, 'w')

    for i in range(0,4):
        f.write(opf[i])

    f.write("\t\t" + '<dc:Title>' + md.title
            + '</dc:Title>' + "\n")
    f.write("\t\t" + '<dc:Creator>' + md.creator
            + '</dc:Creator>' + "\n")
    f.write("\t\t" + '<dc:Language>' + md.language
            + '</dc:Language>' + "\n")

    for i in range(5,12):
        f.write(opf[i])

    for rf in rfs:
        i = rfs.index(rf) + 2
        f.write('<item id="item' + str(i) +
                '" media-type="application/xhtml+xml" href="' +
                rf.filename + '"></item>' + "\n")

    for i in range(12,15):
        f.write(opf[i])

    for rf in rfs:
        i = rfs.index(rf) + 2
        f.write('<itemref idref="item' + str(i) + '"/>' + "\n")

    f.write(opf[15])


    f.close()


def kindlegen(md):
    #webbrowser.open_new_tab("http://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000234621")
    pass

