/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PivotRenderer } from "@web/views/pivot/pivot_renderer";

import { useEffect, signal } from "@odoo/owl";

patch(PivotRenderer.prototype, {
    setup() {
        super.setup();
        this.root = signal.ref();
        if (this.env.services.ui.isSmall) {
            useEffect(() => {
                const rootEl = this.root();
                if (rootEl) {
                    const tooltipElems = rootEl.querySelectorAll("*[data-tooltip]");
                    for (const el of tooltipElems) {
                        el.removeAttribute("data-tooltip");
                        el.removeAttribute("data-tooltip-position");
                    }
                }
            });
        }
    },

    getPadding(cell) {
        if (this.env.services.ui.isSmall) {
            return 5 + cell.indent * 5;
        }
        return super.getPadding(...arguments);
    },
});
