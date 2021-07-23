window.console.log('Se ejecuta el script.');

var PartnerField = require('web.basic_fields').PartnerField;

var ResPartnerMany2oneInheritAcademy = PartnerField.extend({
    _renderReadonly: function () {
        // implement some custom logic here
        window.console.log('Hola');
    },
});

var fieldRegistry = require('web.field_registry');

fieldRegistry.add('res_partner_many2one_inherit_academy', ResPartnerMany2oneInheritAcademy);