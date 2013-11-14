!function()
{
    document.onreadystatechange = function()
    {
        var state = document.readyState;

        if (state == 'complete')
        {
            load_djpikaday();
        }
    }

    if (typeof window['gettext'] == 'undefined')
    {
        window['gettext'] = function(s)
        {
            return s;
        }
    }

    function load_djpikaday()
    {
        var inputs = document.querySelectorAll('[data-pikaday="true"]');

        for (var i = 0; i < inputs.length, inp = inputs[i]; ++i)
        {
            var picker = new Pikaday({
                field: inp,
                format: 'DD/MM/YYYY',
                onSelect: function(){
                    inp.value = picker.toString();
                },
                i18n: {
                    previousMonth : gettext('Previous Month'),
                    nextMonth     : gettext('Next Month'),
                    months        : [
                        gettext('January'),
                        gettext('February'),
                        gettext('March'),
                        gettext('April'),
                        gettext('May'),
                        gettext('June'),
                        gettext('July'),
                        gettext('August'),
                        gettext('September'),
                        gettext('October'),
                        gettext('November'),
                        gettext('December')
                    ],
                    weekdays      : [
                        gettext('Sunday'),
                        gettext('Monday'),
                        gettext('Tuesday'),
                        gettext('Wednesday'),
                        gettext('Thursday'),
                        gettext('Friday'),
                        gettext('Saturday')
                    ],
                    weekdaysShort : [
                        gettext('Sun'),
                        gettext('Mon'),
                        gettext('Tue'),
                        gettext('Wed'),
                        gettext('Thu'),
                        gettext('Fri'),
                        gettext('Sat')
                    ]
                }
            });
        }
    }
}();
