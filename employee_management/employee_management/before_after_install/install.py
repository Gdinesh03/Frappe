import frappe


def before_install():
    print("get context ****************************/////////////////////////--------------------------------")
    print("Before Install Working")


def after_install():
    print("get context ****************************/////////////////////////--------------------------------")
    print("After install Working")


def get_context(context):
    pass
    # context.s = frappe.db.get_list('Wallet Transaction', filters={
    # 'docstatus': 1}, fields=['name', 'date', 'customer_name', 'product_price'])


def on_session_creation():
    frappe.msgprint("You Are logged In sucessfully")


def on_logout():
    frappe.msgprint("Your Are Logged Out Sucessfully")


def after_sync():
    print("****************************/////////////////////////--------------------------------")
    frappe.msgprint("aftrer_sync Working")


def before_migrate():
    print(" before migrate****************************/////////////////////////--------------------------------")


def after_migrate():
    print("after migrate ****************************/////////////////////////--------------------------------")


def before_write_file():
    print("before write file ****************************/////////////////////////--------------------------------")
    # frappe.msgprint("Before Write File Working")


def write_file():
    print("work file****************************/////////////////////////--------------------------------")
    # frappe.msgprint("Write File Working")


def delete_file_data_content(self, only_thumbnail=None):
    print("delete_file_data_content****************************/////////////////////////--------------------------------")
    frappe.msgprint("delete_file_data_content Working")
    print(self)
    print(only_thumbnail)
