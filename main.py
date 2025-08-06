from fpl_login import login
from fetch_team import fetch_current_team
from transfer_engine import suggest_transfers
from execute_transfers import make_transfers
from captain_picker import choose_captain

def run_agent():
    print("[FPL Agent] Starting...")
    fpl = login()
    current_team = fetch_current_team(fpl)
    suggested = suggest_transfers(current_team)
    make_transfers(fpl, suggested)
    choose_captain(fpl, current_team)
    print("[FPL Agent] Done.")

if __name__ == "__main__":
    run_agent()
