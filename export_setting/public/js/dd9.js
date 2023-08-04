frappe.ui.form.on('Data Export', {
    onload: function(frm) {
        frm.add_custom_button(__('Export Settings'), function() {
            fetch_and_mark_fields(frm);
        });
    }
});

function fetch_and_mark_fields(frm) {
    // Check if 'export_settings' field is set
    if (frm.doc.export_settings) {
        frappe.call({
            method: 'export_setting.export_setting.api.get_export_fields',
            args: { 
                doctype: frm.doc.reference_doctype,
                docname: frm.doc.export_settings
            },
            callback: function(r) {
                let selected_fields = r.message || [];

                // Wait for the fields_multicheck field to be updated
                setTimeout(function() {
                    let checkboxes = $(frm.fields_dict.fields_multicheck.wrapper).find('input[type="checkbox"]');
                    checkboxes.each(function() {
                        let checkbox = $(this);
                        let fieldname = checkbox.attr('data-unit');  // Use 'data-unit' instead of 'data-fieldname'
                        console.log(fieldname)
                        let selected_field = selected_fields.find(f => f.fieldname === fieldname);
                        if (selected_field && selected_field.is_selected) {
                                checkbox.prop('checked', true);
                            } else {
                                checkbox.prop('checked', false);
                            }
                            checkbox.trigger("change")
                    });
                }, 1000);  // Adjust the delay as needed
            }
        });
    }
}