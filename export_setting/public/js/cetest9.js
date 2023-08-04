function appendButton() {
    let $wrapper = $('[data-fieldname="select_all_buttons"]').find("div");

    // Remove existing button
    $wrapper.find('[data-action="export_settings"]').remove();

    // Append new button
    console.log('Appending button');
    $wrapper.append('<button class="btn btn-default btn-xs" data-action="export_settings">Export Settings</button>');
    $wrapper.find('[data-action="export_settings"]').click(() => {
        let doctype = $('h3.title-text').attr('title');
        frappe.call({
            method: 'export_setting.export_setting.api.get_export_fields',
            args: {
                doctype: doctype,
                docname: doctype
            },
            callback: (response) => {
                let selected_fieldnames = response.message.map((field) => field.fieldname);
                // Assuming you have access to the dialog's context
                let checkboxes = $wrapper.closest('.modal-body').find('input[type="checkbox"]');
                checkboxes.each(function() {
                    let checkbox = $(this);
                    let fieldname = checkbox.attr('data-unit');
                    if (selected_fieldnames.includes(fieldname)) {
                        checkbox.prop('checked', true);
                    } else {
                        checkbox.prop('checked', false);
                    }
                    checkbox.trigger("change");
                });
            }
        });
    });

    console.log('Button appended');
}

// Function containing the MutationObserver
function observeDialog() {
    let observer = new MutationObserver((mutations) => {
        for (let mutation of mutations) {
            for (let node of mutation.addedNodes) {
                if (node.nodeType === 1 && $(node).find('[data-fieldname="select_all_buttons"]').length > 0) {
                    appendButton();
                }
            }
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
}

// Start observing
observeDialog();
