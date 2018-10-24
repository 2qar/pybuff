
class Player:
	def __init__(self, btag, platform, soup):
		self.btag = btag
		self.platform = platform
		self.soup = soup

	def get_sr(self):
		""" Get the SR of this player.
			If SR isn't displayed on their profile, returns none.

			:rtype:
				integer | None
			:returns:
				The SR of this player.
		"""

		sr_div = self.soup.find(class_='player-skill-rating')
		if sr_div:
			return int(sr_div.contents[0])

	def get_roles(self):
		""" Get the amount of wins on each role for this player.

			:rtype:
				list of tuples
			:returns:
				A list with each role as a tuple in this format:

					(str: name, int: wins)

					For example:
					('Tank', 112)
		"""

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
		""" Get the main role of this player.
			This assumes that the role with the most wins is their main.

			:rtype:
				tuple
			:returns:
				A tuple with the name and win count of their main role.
		"""

		return self.get_roles()[0]

	def __str__(self):
		return self.btag
