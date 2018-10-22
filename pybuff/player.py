import requests
from bs4 import BeautifulSoup

class PlayerNotFound(Exception):
	""" Raised when the GET request for a player returns 404 """

def _get_role(div):
	""" Make a role tuple from a role div """
	wins = int(div.contents[2].attrs['data-value'])
	role_name_div = div.contents[1]
	role_name = role_name_div.contents[0].string
	return (role_name, wins)

class Player:
	def __init__(self, btag, platform='pc'):
		self.btag = btag

		link = f"https://www.overbuff.com/players/{platform}/{btag}"
		req = requests.get(link, headers={'User-Agent': 'pybuff'})
		if req.status_code == 404:
			raise PlayerNotFound
		self.soup = BeautifulSoup(req.text, 'html.parser')

	def get_sr(self):
		""" Returns an sr int """
		sr_div = self.soup.find(class_='player-skill-rating')
		if not sr_div:
			return 0
		return int(sr_div.contents[0])

	def get_roles(self):
		""" Return a list of tuples with a role name and win count """
		roles_container = self.soup.find(class_='table-data')
		if not roles_container:
			return [('', 0)]

		roles = roles_container.contents[1].contents
		
		return [_get_role(div) for div in roles]

	def get_role(self):
		""" Get the main role of this player """
		return self.get_roles()[0]

	def __str__(self):
		return self.btag
