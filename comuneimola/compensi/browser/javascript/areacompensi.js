jq(document).ready(function() {

    jq.extend(jq.fn.dataTableExt.oSort,
        {
        "date-ita-pre": function ( a )
            {
                var itaDatea = a.split('/');
                return (itaDatea[2] + itaDatea[1] + itaDatea[0]) * 1;
            },

        "date-ita-asc": function ( a, b )
            {
            return ((a < b) ? -1 : ((a > b) ? 1 : 0));
            },

        "date-ita-desc": function ( a, b )
            {
            return ((a < b) ? 1 : ((a > b) ? -1 : 0));
            }
        });

    jq('#compensitable').dataTable({
        "sPaginationType": "full_numbers",
        "oLanguage": {"sUrl": "@@collective.js.datatables.translation"},
        "aoColumns": [null, null, null, null, {"sType": "date-ita"} ]
   });
})
