/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { SectionAndNoteListRenderer } from "@account/components/section_and_note_fields_backend/section_and_note_fields_backend";

const { Component, useEffect } = owl;

patch(SectionAndNoteListRenderer.prototype, "/aspl_section_sub_total/static/src/js/section_and_note_fields_backend", {
    setup() {
        var args = this._super(...arguments)
    },
    getSectionColumns(columns) {
        const sectionCols = columns.filter((col) => col.widget === "handle" || col.type === "field" && col.name === this.titleField || col.name === "price_subtotal");
        return sectionCols.map((col) => {
            if (col.name === this.titleField) {
                return { ...col, colspan: columns.length - sectionCols.length + 1 };
            } else {
                return { ...col };
            }
        });
    },
});