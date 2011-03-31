$(document).ready(function(){
form = $("#user_profile_edit");

	$("#user_profile_edit").submit(send_post);	
	$("#status").html("Ready")
	
	
	function toggle_ui(bool){
		if (bool == true){
			form.slideToggle("slow");
			$("#user_profile_edit *").attr("disabled", true);


		}
		else{
			form.slideToggle("slow");
			$("#user_profile_edit *").attr("disabled", false);
		}
		
	}
	
	
	function send_post(){
		$("#status").html("Sending");
		var POST = {
				other_contacts: form.attr("other_contacts").value,
				skype: form.attr("skype").value,
				jabber: form.attr("jabber").value,
				email: form.attr("email").value,
				bio: form.attr("bio").value,
				date_of_birth: form.attr("date_of_birth").value,
				last_name: form.attr("last_name").value,
				name: form.attr("name").value
				}
				
		toggle_ui(true);
		
		$.post("/edit-contacts/",
				POST,
				
				function(data){
					$('#user_profile_edit').html(data);
					$("#status").html("Done")
					//reinit datepicker 
					initDatePicker();
					//rebindform
					
					toggle_ui(false);
				}
			);
		return false;
	}
});

	