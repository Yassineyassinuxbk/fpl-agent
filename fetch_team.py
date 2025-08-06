import asyncio

def fetch_current_team(fpl):
    async def main():
        user = await fpl.get_user()
        team = await user.get_team()
        return team
    return asyncio.get_event_loop().run_until_complete(main())
