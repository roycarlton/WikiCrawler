# WikiCrawler
Python webcrawler to attempt to find (theoretically) every wikipedia article by starting at an arbitrary page and following links.

Uses the python module urllib.request to fetch web pages using a url.

Implements a breadth-first approach - A page is searched for wiki links which are added to the queue, then each queued page is visited in turn, queueing each of their links.

This leads to many duplicate pages so I'm currently working on a way to eliminate duplicates from the text files either while the crawler is running or when it has stopped.
