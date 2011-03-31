$(document).ready(function(){
	
	$("#user_profile_edit").submit(send_post);	
	$("#status").html("Ready")
	
	function toggle_ui(bool){
		if (bool == true){
			$("#user_profile_edit").slideToggle("slow");
			$("#user_profile_edit *").attr("disabled", true);
		}
		else{
			$("#user_profile_edit").slideToggle("slow");
			$("#user_profile_edit *").attr("disabled", false);
		}
		
	}

	function send_post(){
		$("#status").html("Sending");
		var POST = $('#user_profile_edit').formSerialize();
				
		toggle_ui(true);
		
		$.post("/edit-contacts/",
				POST,
				
				function(data){
					$('#user_profile_edit').html(data);
					$("#status").html("Done")
					//reinit datepicker 
					initDatePicker();
					toggle_ui(false);
				}
			);
		return false;
	}
});

	