jq(document).ready(function() {

    jq.extend(jq.fn.dataTableExt.oSort,
        {
        "date-ita-pre": function ( a )
            {
            var itaDatea = a.split('/');
            if (itaDatea == "")
                return 0;
            return (itaDatea[2] + itaDatea[1] + itaDatea[0]) * 1;
            },

        "date-ita-asc": function ( a, b )
            {
            return ((a < b) ? -1 : ((a > b) ? 1 : 0));
            },

        "date-ita-desc": function ( a, b )
            {
            return ((a < b) ? 1 : ((a > b) ? -1 : 0));
            },
        "euro-ita-pre": function ( a )
            {
            return a.replace(/\./g,'').replace(',','.')*1;
            },
        "euro-ita-asc": function ( a, b )
            {
            return ((a < b) ? -1 : ((a > b) ? 1 : 0));
            },
        "euro-ita-desc": function ( a, b )
            {
            return ((a < b) ? 1 : ((a > b) ? -1 : 0));
            }
        });

    jq('#compensitable').dataTable({
        "sPaginationType": "full_numbers",
        "oLanguage": {"sUrl": "@@collective.js.datatables.translation"},
        "aoColumns": [null, {"sType": "euro-ita"}, null, null, {"sType": "date-ita"} ]
   });
})
