function setupAjaxForm(form_id, clear_form){
    var form = '#' + form_id;
    var form_message = form + '-message';
 
    // enable/disable form
    var disableSubmit = function(val){
    	for(var i=0; i < $(form)[0].elements.length; i++) {
    		$(form)[0].elements[i].disabled = val;
    	}
    };
    disableSubmit(false);
 
    // setup loading message
    $(form).ajaxSend(function(){
        $(form_message).removeClass().addClass('loading').html('Loading...').fadeIn();
    });
 
    // setup jQuery Plugin 'ajaxForm'
    var options = {
        dataType:  'json',
        beforeSubmit: function(){disableSubmit(true);},
        success: function(json){
        	$(form_message).hide();
            $(form_message).removeClass().addClass(json.type).html(json.message).fadeIn('slow');
            if(json.type == 'success' && clear_form === true)
                $(form).clearForm();
        },
        complete: function() {
            disableSubmit(false);
        }
    };
    $(form).ajaxForm(options);
}