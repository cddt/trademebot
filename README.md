# trademebot

A basic web scraper to determine the count of property listings on Trademe in each region, district, and suburb. 

Requires <a href="https://github.com/mozilla/geckodriver">Geckodriver</a>. 

An example of the data collected over the period of a year can be found <a href="https://cddt.nz/projects/tmchart.html">here</a>. 

To collect this data on a daily basis, it's useful to use a headless server, with the script executed via `crontab` and `xvfb` (see <a href="https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml">here</a>). For example: 

`01 17 * * * /usr/bin/xvfb-run -a  /usr/bin/python3 /home/trademebot/run.py`

NB: This was my first foray into both python and web scraping, and as such does not necessarily demonstrate good coding practices. 

