# rsp2k - Reddit Self Posts to Kindle

Inspired by Instapaper service this app is meant to be quick and
effective tool to get reddit (and maybe in future other services)
posts with comments, convert them to mobi format and optionally 
mail ready mobi file to user's Kindle.

For any questions or suggestions write me on [hgrzywacz@gmail.com](mailto:hgrzywacz@gmail.com).

Code is tested with Python v 3.2.

## Get\_top

Tool for making lists. It's called get top but it's for getting top, new, controversial and hot.
Interface is as simple as possible:

	$ get_top.py kindle 10 new

Gets ten newest submissions from r/kindle.

	$ get_top.py 60 day askreddit

Gets 60 top (default action) from day from r/askreddit.

	$ get_top.py controversial 321 all world_news

Gets 321 most controversial submissions of all time from r/world\_news.
As you can see order of arguments is irrelevant and none of them is mandatory! Just type out what you want.
If you ask me it's "don't make me think" rule personified (codified?).

List will be seved with a proper name (that will be displayed) in current directory OR if you want 
to lists/ folder - just create it.

## Temporary testing

Mobi content file creation, opf, toc.html, toc.ncx from few .rhtml files I've prepared:

	$ python test.py clean
	$ python test.py test_mobi

Getting posts with comments from reddit:

	$ ./get_post.py

Name of created file will be printed

## Most important things to do:

* Fetching more comments than API returns in one response, as shown [here](https://github.com/reddit/reddit/wiki/API)
* Main script that links uses all the parts as one - option parser, Kindlegen runner.
* Mailing .mobi as attachment.
