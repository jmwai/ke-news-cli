from setuptools import setup
#This won't work at the moment.

setup(
	name="ke-news-cli",
	version=0.1,
	py_modules=['news.py'],
	install_requires=[
		'Click',
		'BeautifulSoup',
		'Pillow',
		'argparse',
		'cssselect',
		'feedparser',
		'jieba',
		'lxml',
		'pyteaser',
		'requests',
		'wsgiref',
	],
	entry_points='''
			[console_script]
			news=news:cli
			''',
	author= "James Mwai",
	author_email= "smartemwa@gmail.com",
	license= "Coming",
	url='https://github.com/jmwai/ke-news-cli'
	description= "A simple command line interface to\
	 read summarized Kenyan news on the terminal without\
	  having to browse the boring news websites.",
	)