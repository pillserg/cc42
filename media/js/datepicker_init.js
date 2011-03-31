function initDatePicker(){
  $(document).ready(function() {
    $( "#id_date_of_birth" ).datepicker({ altFormat: 'yy-mm-dd',
                                         dateFormat: 'yy-mm-dd' });
  });
};

initDatePicker();