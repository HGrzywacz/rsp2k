# rsp2k - Reddit Self Posts to Kindle

Inspired by Instapaper service this app is meant to be quick and
effective tool to get reddit (and maybe in future other services)
posts with comments, convert them to mobi format and optionally 
mail ready mobi file to user's Kindle.

For any questions or suggestions write me on [hgrzywacz@gmail.com](mailto:hgrzywacz@gmail.com).

Code is tested with python '''3.2.'''

## Temporary testing

Mobi content file creation, opf, toc.html, toc.ncx from few .rhtml files I've prepared:

	$ python test.py clean
	$ python test.py test_mobi

Getting posts with comments from reddit:

	$ ./get_post.py

Name of created file will be printed

## Most important things to do:

* Fetching more comments than API returns in one response, as shown [here](https://github.com/reddit/reddit/wiki/API)
* Main script that links uses all the parts as one
** Option parser.
** Kindlegen runner.
* Mailing .mobi as attachment.
