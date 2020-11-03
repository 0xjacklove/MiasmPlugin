import graph_ir
import depgraph
import symbol_exec_module
import ida_kernwin as kw
def ask_desired_maturity():
	"""Displays a dialog which lets the user choose a maturity level
	of the microcode to generate."""
	choose_num = [
	["graph_ir", 0],
	["symbol_exec", 1],
	["depgraph",2]]

	class MaturityForm(kw.Form):
		def __init__(self):
			self.title = "Choose exec"
			form = ("STARTITEM {id:mat_lvl}\n"
				"%s\n"
				" \n"
				"<Select:{mat_lvl}>\n\n"
				"<##Options##Output includes comments:{flags_short}>{chkgroup_flags}>\n\n" %
				self.title)

			dropdown_ctl = kw.Form.DropdownListControl(
				[text for text, _ in choose_num])
			chk_ctl = kw.Form.ChkGroupControl(("flags_short",))

			controls = {"mat_lvl": dropdown_ctl,
			"chkgroup_flags": chk_ctl}

			kw.Form.__init__(self, form, controls)

	form = MaturityForm()
	form, args = form.Compile()
	form.flags_short.checked = True
	ok = form.Execute()

	choose = None
	text = None
	flags = 0
	if ok == 1:
		text, choose = choose_num[form.mat_lvl.value]
	form.Free()
	return (text, choose, flags)
	
def choose_exec():
	text, choose_num,flags = ask_desired_maturity()
	if text is None and choose_num is None:
		return (True, "Cancelled")
	if choose_num==0:
		graph_ir.function_graph_ir()
	elif choose_num==1:
		symbol_exec_module.symbolic_exec()
	else:
		depgraph.launch_depgraph()