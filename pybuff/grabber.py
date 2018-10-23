import asyncio
import aiohttp
from bs4 import BeautifulSoup
from .player import Player

user_agent = {'User-Agent': 'pybuff'}

class PlayerNotFound(Exception):
	""" Raised when the GET request for a player returns 404 """
	def __init__(self, message, btag):
		super().__init__(message)
		self.errors = btag

class BadBattletag(Exception):
	""" Raised when trying to get a player with a bad battletag """
	def __init__(self, message, btag):
		super().__init__(message)
		self.errors = btag

async def get_player(battletag, platform='pc'):
	""" Return a player object from a battletag 
		Valid battletags:
			name-number
			name#number
	"""
	url_tag = battletag

	if '#' in url_tag:
		url_tag = url_tag.replace('#', '-')

	split = url_tag.split('-')
	if len(split) != 2:
		raise BadBattletag("# or - in weird spot", battletag)
	try:
		int(split[1])
	except:
		raise BadBattletag("Expected a num on right side of tag", battletag)

	url = f"https://overbuff.com/{platform}/{url_tag}"
	async with aiohttp.request('GET', url, headers=user_agent) as page:
		if page.status == '404':
			raise PlayerNotFound("Unable to find player.", battletag)
		
		soup = BeautifulSoup(await page.text(), 'html.parser')
		return Player(battletag, platform, soup)
