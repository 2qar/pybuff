import asyncio
# import sys or something and add the path to the library so i can actually test this shit
import pytest
import sys
sys.path.append('/home/tucker/Documents/git/pybuff/')
from pybuff.grabber import get_player

@pytest.mark.asyncio
async def test_get_player():
	print("test_get_player")
	player = await get_player('Tydra#11863')
	assert str(player) == 'Tydra#11863'
