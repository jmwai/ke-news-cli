import click
import feedparser
from pyteaser import SummarizeUrl


@click.command()
@click.option('--count', default=2, help='Number of times to announce')
@click.argument('name')
def hello(count, name):
	for x in range(count):
		click.echo("Hello Mr. %s" % name)

	click.echo(click.style('Hello World!', fg='green'))
	click.echo(click.style('Some more text', bg='blue', fg='white'))
	click.echo(click.style('ATTENTION', blink=True, bold=True))

@click.command()
def nation_news():
	click.echo("Harvesting nation news")
	feed_url = "http://www.nation.co.ke/-/1148/1148/-/view/asFeed/-/vtvnjq/-/index.xml"
	feed = feedparser.parse(feed_url)
	entries = feed['entries']
	for entry in entries:
		# click.echo(entries.index(entry))
		# click.echo(entry['title'])
		number = entries.index(entry) + 1 #We add one for user friendlines
		title = entry['title']
		click.echo(click.style("%s. %s" %(number, title), blink=True, bold=True))
		click.echo(click.style(entry['description'], fg='green'))
		click.echo("----------------------------------")
	item = click.prompt('Please enter an entry number for more', type=int)

	entry_select = entries[item-1]

	entry_url = entry_select['link']

	summary = SummarizeUrl(entry_url)

	click.echo(click.style(entry_select['title'], fg='red'))

	for x in summary:
		click.echo(x)

	# click.echo(entries[item - 1]) #Do more stuff with the return value



if __name__ == '__main__':
	# hello()
	nation_news()