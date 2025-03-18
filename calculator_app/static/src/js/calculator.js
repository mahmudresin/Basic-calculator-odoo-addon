/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onMounted } from "@odoo/owl";
import { Dialog } from "@web/core/dialog/dialog";
import { _t } from "@web/core/l10n/translation";

class CalculatorAction extends Component {
    setup() {
        this.state = useState({
            displayValue: '0',
            history: []
        });
        
        onMounted(() => this.loadHistory());
    }
    
    async loadHistory() {
        try {
            const result = await this.env.services.rpc({
                route: '/calculator/history',
                params: { limit: 10 },
            });
            this.state.history = result || [];
        } catch (error) {
            console.error("Failed to load calculator history", error);
        }
    }
    
    onButtonClick(ev) {
        const value = ev.target.dataset.value;
        
        if (this.state.displayValue === '0' && value !== '.') {
            this.state.displayValue = value;
        } else {
            this.state.displayValue += value;
        }
    }
    
    onClearClick() {
        this.state.displayValue = '0';
    }
    
    onBackspaceClick() {
        this.state.displayValue = this.state.displayValue.length > 1
            ? this.state.displayValue.slice(0, -1)
            : '0';
    }
    
    onEqualsClick() {
        try {
            const expression = this.state.displayValue;
            // Evaluate the expression locally instead of using RPC
            const result = eval(expression);
            if (!isFinite(result)) {
                throw new Error("Invalid Calculation");
            }
            this.state.displayValue = String(result);
            // Add to local history
            this.state.history.unshift({ expression, result });
        } catch (error) {
            this.state.displayValue = 'Error';
        }
    }
    
    async onHistoryClick() {
        this.env.services.dialog.add(Dialog, {
            title: _t("Calculator History"),
            body: this.state.history.map(h => `${h.expression} = ${h.result}`).join("<br>"),
        });
    }
}

CalculatorAction.template = 'calculator_app.Calculator';

registry.category("actions").add("calculator_app", CalculatorAction);
