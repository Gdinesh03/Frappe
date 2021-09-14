import frappe
def on_session_creation():
	user = frappe.session.user
	if user == "boopathy@gmail.com":
		frappe.msgprint("hii Boopathy")