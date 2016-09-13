;(function()
{
    'use strict';

    var CONFIG = {
        "apiUrl"    : "http://hasanagha.pythonanywhere.com/search/",
    };

    var SELECTORS = {
        'form'            : '#frm_search',
        'title_field'     : '#title',
        'submitBtn'       : '#btn_submit',
        'preLoader'       : '.fa-spinner',
        'resultsTable'    : '#tbl_results',
        'hb_item'         : '#presentation-item',
        'results'         : '.results ul',
    };

    var Presentation =
    {
        init: function()
        {
            var _this = this;

            $('body').on("click", SELECTORS.submitBtn, function(){
                $(SELECTORS.preLoader).show();
                $.ajax({
                    url: CONFIG.apiUrl,
                    type: 'POST',
                    data: $(SELECTORS.form).serialize(),
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                    },
                    success: function(response) {
                        _this.fillResults(response);
                        $(SELECTORS.preLoader).hide();
                    }
                });
            });
            $(SELECTORS.title_field).keypress(function (e) {
                if (e.which == 13) {
                    $(SELECTORS.submitBtn).click();
                    return false;
                }
            });
            $(SELECTORS.submitBtn).click();
        },
        fillResults: function(response){
            var _this = this;
            $('.counter').html(response.length + ' result(s) found').show();
            if(response.length) {
                var source   = $(SELECTORS.hb_item).html();
                var template = Handlebars.compile(source);
                var context = {presentations: response}
                var html    = template(context);
            } else {
                var html = '';
            }
            $(SELECTORS.results).html(html);
        }
    };
    $(document).ready(function(){
        Presentation.init();
    });

})();
