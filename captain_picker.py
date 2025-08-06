def choose_captain(fpl, current_team):
    import asyncio

    async def main():
        if not current_team:
            return
        top_player = max(current_team, key=lambda x: x['points'])
        user = await fpl.get_user()
        print(f"Setting captain: {top_player['element']}")
        await user.pick_captain(top_player['element'])

    asyncio.get_event_loop().run_until_complete(main())
