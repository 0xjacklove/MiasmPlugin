
import os

import ida_idaapi
import ida_loader
import ida_kernwin
import ida_hexrays

my_dirname, _ = os.path.split(__file__)

#setattr(ida_hexrays, "MMAT_DEOB_MAP", getattr(ida_hexrays, "MMAT_LOCOPT"))

class MiasmPluginT(ida_idaapi.plugin_t):
	flags = 0
	comment = "This is miasm plugin"
	help = ""
	wanted_name = "Python Miasm Plugin"
	wanted_hotkey = ""

	def __init__(self):
		print("start")


	def init(self):
		if not ida_hexrays.init_hexrays_plugin():
			print("MiasmPlugin: no decompiler, skipping")
			return ida_idaapi.PLUGIN_SKIP
		print("Hex-rays version %s has been detected, %s ready to use" % (
			ida_hexrays.get_hexrays_version(),
			self.wanted_name))

		import sys
		modules_path = os.path.join(my_dirname, "miasm_modules")
		if not modules_path in sys.path:
			sys.path.append(modules_path)
		import menu
		menu.create_miasm_menu()
		return ida_idaapi.PLUGIN_OK
	def run(self, arg):
		return True
	def term(self):
		return True
def PLUGIN_ENTRY():
	return MiasmPluginT()
PLUGIN_ENTRY()


