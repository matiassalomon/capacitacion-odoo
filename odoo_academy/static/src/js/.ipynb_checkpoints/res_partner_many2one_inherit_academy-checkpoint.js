odoo.define('partner.autocomplete.many2one', function (require) {
    'use strict';
    window.console.log('Se ejecuta el script.');

    var PartnerField = require('partner.autocomplete.many2one').PartnerField;

    window.console.log(PartnerField);

    var ResPartnerMany2oneInheritAcademy = PartnerField.extend({
        _renderReadonly: function () {
            // implement some custom logic here
            window.console.log('Hola');
        },
    });

    var fieldRegistry = require('web.field_registry');

    fieldRegistry.add('res_partner_many2one_inherit_academy', ResPartnerMany2oneInheritAcademy);
});
