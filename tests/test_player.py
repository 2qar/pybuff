import pytest
import asyncio
from pybuff import get_player

@pytest.mark.asyncio
async def test_get_sr():
    player = await get_player('Tydra#11863')
    assert player.get_sr() != None

@pytest.mark.asyncio
async def test_get_sr_missing():
    player = await get_player('Tucker#4378')
    assert player.get_sr() == None

@pytest.mark.asyncio
async def test_get_roles():
    player = await get_player('heckoffnerd#1772')
    assert player.get_roles() != None

@pytest.mark.asyncio
async def test_get_roles_missing():
    player = await get_player('Tucker#4378')
    assert player.get_roles() == None

@pytest.mark.asyncio
async def test_get_role():
    player = await get_player('heckoffnerd#1772')
    assert player.get_role()[0] == 'Tank'

@pytest.mark.asyncio
async def test_get_role_missing():
    player = await get_player('Tucker#4378')
    assert player.get_role() == None
