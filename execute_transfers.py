def make_transfers(fpl, transfers):
    import asyncio

    async def main():
        user = await fpl.get_user()
        if transfers:
            print(f"Transferring OUT: {transfers[0]['out']} -> IN: {transfers[0]['in']}")
            await user.transfer(transfers)
    asyncio.get_event_loop().run_until_complete(main())
