frappe.pages['order-disolay'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Order Details ',
		single_column: true
	});
}