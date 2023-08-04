// Copyright (c) 2023, zaid and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Export Settings', {
// 	// refresh: function(frm) {

// 	// }
// });
// frappe.ui.form.on('Export Settings', {
//     reference_doctype: function(frm) {
//         if (frm.doc.doctype) {
//             frappe.call({
//                 method: 'export_setting.export_setting.doctype.export_settings.export_settings.get_doctype_fields',
//                 args: {
//                     doctype: frm.doc.reference_doctype
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         let fields = r.message;
//                         let html = `<div style="display: flex; flex-wrap: wrap;">`;
//                         fields.forEach((field, index) => {
//                             html += `
//                             <div style="flex: 1 1 30%; padding: 5px;">
//                                 <input type="checkbox" name="${field.fieldname}"> ${field.label}
//                             </div>`;
//                         });
//                         html += `</div>`;
//                         frm.set_df_property('dynamic_field_container', 'options', html);
//                         frm.refresh_field('dynamic_field_container');
//                     }
//                 }
//             });
//         }
//     },
//     before_save: function(frm) {
//         // Get the list of checkboxes
//         let checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
//         // Prepare the data to be sent to the Python method
//         let data = Array.from(checkboxes).map(checkbox => {
//             return {
//                 fieldname: checkbox.name,
//                 is_selected: checkbox.checked
//             };
//         });

//         // Call the Python method to save the data
//         frappe.call({
//             method: 'export_setting.export_setting.doctype.export_settings.export_settings.save_selected_fields',
//             args: {
//                 parent: frm.doc.name,
//                 data: data
//             }
//         });
//     }
// });


frappe.ui.form.on('Export Settings', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Existing form, fetch the checked fields
            fetch_and_render_fields(frm);
        }
    },
    reference_doctype: function(frm) {
        if (frm.doc.reference_doctype) {
            // When reference_doctype is set, fetch the fields
            fetch_and_render_fields(frm);
        }
    },
    after_save: function(frm) {
		if (!frm.is_new()){
        // Get the list of checkboxes
        let checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
        // Prepare the data to be sent to the Python method
        let data = Array.from(checkboxes).map(checkbox => {
            return {
                fieldname: checkbox.name,
                is_selected: checkbox.checked
            };
        });

        // Call the Python method to save the data
        frappe.call({
            method: 'export_setting.export_setting.doctype.export_settings.export_settings.save_selected_fields',
            args: {
                parent: frm.doc.name,
                data: data,
				doctype: frm.doc.reference_doctype
            }
        });
		frm.reload_doc();}
    },
	before_save : function(frm) {
		if (!frm.is_new()){
        // Get the list of checkboxes
        let checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
        // Prepare the data to be sent to the Python method
        let data = Array.from(checkboxes).map(checkbox => {
            return {
                fieldname: checkbox.name,
                is_selected: checkbox.checked
            };
        });

        // Call the Python method to save the data
        frappe.call({
            method: 'export_setting.export_setting.doctype.export_settings.export_settings.save_selected_fields',
            args: {
                parent: frm.doc.name,
                data: data,
				doctype: frm.doc.reference_doctype
            }
        });
    }},
});

function fetch_and_render_fields(frm) {
    frappe.call({
        method: 'export_setting.export_setting.doctype.export_settings.export_settings.get_doctype_fields',
        args: {
            doctype: frm.doc.reference_doctype
        },
        callback: function(r) {
            // Get the selected fields
            frappe.call({
                method: 'export_setting.export_setting.doctype.export_settings.export_settings.get_selected_fields',
                args: {
                    docname: frm.doc.name,
                    doctype: frm.doc.reference_doctype
                },
                callback: function(response) {
                    // Get the list of selected fields
                    let selected_fields = response.message;
					if (r.message) {
						let fields = r.message;
						let html = `<div style="display: flex; flex-wrap: wrap;">`;
						fields.forEach((field, index) => {
							// Find the field in selected_fields
							let selected_field = selected_fields.find(f => f.fieldname === field.fieldname);
							let is_selected = selected_field && selected_field.is_selected ? 'checked' : '';
							html += `
							<div style="flex: 1 1 30%; padding: 5px;">
								<input type="checkbox" name="${field.fieldname}" ${is_selected}> ${field.label}
							</div>`;
						});
						html += `</div>`;
						frm.set_df_property('dynamic_field_container', 'options', html);
						frm.refresh_field('dynamic_field_container');
					}
                }
            });
        }
    });
}
