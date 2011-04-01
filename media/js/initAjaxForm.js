$(document).ready(function() { 
	$("#status").html("Ready")
	
	function toggle_ui(bool){
		$("#user_profile_edit").slideToggle("slow");
		if (bool == true){
			$("#user_profile_edit *").attr("disabled", true);
			$("#status").html("Sending...")
		}
		else{
			$("#user_profile_edit *").attr("disabled", false);
			$("#status").html("Done")
		}
	}
	
	var options = {
		target:        "#user_profile_edit",
        beforeSubmit:   function(){
							toggle_ui(true);
						},
        success:		function(){
							toggle_ui(false);
							initDatePicker();
						}
    };

    $('#user_profile_edit').ajaxForm(options);
});



