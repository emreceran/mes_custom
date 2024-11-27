/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";

const FIXED_FIELD_COLUMN_WIDTHS = {
    boolean: "70px",
    date: "92px",
    datetime: "146px",
    float: "92px",
    integer: "74px",
    monetary: "104px",
    handle: "33px",
};


patch(ListRenderer.prototype, "/aspl_section_sub_total/static/src/js/section_and_note_fields_backend", {
    setup() {
        var args = this._super(...arguments)
    },
    calculateColumnWidth(column) {
        $('.o_list_char').each(function() {
            var self = this
            $('.o_is_line_section').each(function() {
                if ($(this)[0].children[1].dataset.tooltip === $(self)[0].innerText){
                    $(this)[0].children[2].classList.remove('o_hidden');
                    $(this)[0].children[2].innerHTML = $(self)[0].parentElement.children[1].innerText;
                };
            });
        });
        if (column.options && column.rawAttrs.width) {
            return { type: "absolute", value: column.rawAttrs.width };
        }

        if (column.type !== "field") {
            return { type: "relative", value: 1 };
        }

        const type = column.widget || this.props.list.fields[column.name].type;
        if (type in FIXED_FIELD_COLUMN_WIDTHS) {
            return { type: "absolute", value: FIXED_FIELD_COLUMN_WIDTHS[type] };
        }

        return { type: "relative", value: 1 };
    },
});