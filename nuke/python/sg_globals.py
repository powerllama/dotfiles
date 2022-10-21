"""
sg_globals.py

putting all of the shotgun information into one small file so it's not easily lost. Always easy to call.

"""


import shotgun_api3 as shotgun
import tank

SERVER_PATH = "https://psyop.shotgunstudio.com"
SCRIPT_USER = "mlTools"
SCRIPT_KEY  = "e0078c0e80f09ee7a76de2c25afce6bd34a5bc601f598d446daf6a8e848d9089"

PROJECT_ID = tank.platform.current_engine().context.project['id']