
class Player:
	def __init__(self, btag, platform, soup):
		self.btag = btag
		self.platform = platform
		self.soup = soup

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

		def create_role(div):
			""" Make a role tuple from a role div """
			wins = int(div.contents[2].attrs['data-value'])
			role_name_div = div.contents[1]
			role_name = role_name_div.contents[0].string
			return (role_name, wins)
		
		return [create_role(div) for div in roles]

	def get_role(self):
		""" Get the main role of this player """
		return self.get_roles()[0]

	def __str__(self):
		return self.btag
