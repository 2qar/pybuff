import asyncio
import pytest
from aiohttp import ClientSession

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

@pytest.mark.asyncio
async def test_get_player_with_session():
    async with ClientSession() as session:
        player = await get_player('Tydra#11863', session=session)
        assert str(player) == 'Tydra#11863'

@pytest.mark.asyncio
async def test_get_multiple_players_with_session():
    async with ClientSession() as session:
        for btag in ['Tydra#11863', 'heckoffnerd#1772', 'Tucker#4378']:
            player = await get_player(btag, session=session)
            assert str(player == btag)

@pytest.mark.asyncio
async def test_get_multiple_players_with_session_with_invalid_player():
    async with ClientSession() as session:
        for i, btag in enumerate(['Tydra#11863', 'Ogdog#1234', 'Tucker#4378']):
            if i == 1:
                with pytest.raises(BadBattletag):
                    await get_player(btag, session=session)
            else:
                player = await get_player(btag, session=session)
                assert str(player) == btag
