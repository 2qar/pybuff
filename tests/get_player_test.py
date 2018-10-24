import asyncio
import pytest
import sys
sys.path.append('/home/tucker/Documents/git/pybuff/')

from pybuff.grabber import get_player
from pybuff.grabber import BadBattletag

@pytest.mark.asyncio
async def test_get_player_pc():
    player = await get_player('Tydra#11863')
    assert str(player) == 'Tydra#11863'

@pytest.mark.asyncio
async def test_get_player_console():
    for profile in [('Carried Reaper', 'xbl'), ('Im_Roadhog', 'psn')]:
        player = await get_player(profile[0], platform=profile[1])
        assert str(player) == profile[0]

@pytest.mark.asyncio
async def test_get_player_invalid_battletag():
    with pytest.raises(BadBattletag):
        await get_player('ogdog')

@pytest.mark.asyncio
async def test_get_player_nonexistent():
    with pytest.raises(BadBattletag):
        await get_player('Ogdog#1234')
