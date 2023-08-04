# import frappe
# @frappe.whitelist()
# def apply_export_settings(doc, method):
#     if doc.export_settings:
#         # Get the Export Settings document
#         export_settings = frappe.get_doc('Export Settings', doc.export_settings)

#         # Apply the settings to the data export
#         for field in export_settings.selected_fields:
#             # The actual implementation will depend on your needs
#             # and the structure of your Export Settings doctype
#             if not field.is_selected:
#                 # Remove this field from the data export
#                 doc.remove_field(field.fieldname)

#         # Save the changes to the Data Export document
#         doc.save()

# # Register the hook
# # doc_events = {
# #     "Data Export": {
# #         "before_insert": apply_export_settings,
# #     }
# # }
