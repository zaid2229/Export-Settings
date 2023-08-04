// const set_field_options = (frm) => {
//     const parent_wrapper = frm.fields_dict.fields_multicheck.$wrapper;
//     const filter_wrapper = frm.fields_dict.filter_list.$wrapper;
//     const doctype = frm.doc.reference_doctype;
//     const related_doctypes = get_doctypes(doctype);

//     parent_wrapper.empty();
//     filter_wrapper.empty();

//     frm.filter_list = new frappe.ui.FilterGroup({
//         parent: filter_wrapper,
//         doctype: doctype,
//         on_change: () => {},
//     });

//     // Add 'Select All' and 'Unselect All' button
//     make_multiselect_buttons(parent_wrapper);

//     frm.fields_multicheck = {};
//     related_doctypes.forEach((dt) => {
//         // Here, you should fetch the data from the back end. For example:
//         frappe.call({
//             method: 'export_setting.export_setting.doctype.export_settings.export_settings.get_selected_fields',
//             args: {
//                 docname: frm.doc.name,
//                 doctype: dt
//             },
//             callback: (response) => {
//                 let selected_fields = response.message.map(field => field.fieldname);
//                 frm.fields_multicheck[dt] = add_doctype_field_multicheck_control(dt, parent_wrapper, selected_fields);
//             }
//         });
//     });

//     frm.refresh();
// };
