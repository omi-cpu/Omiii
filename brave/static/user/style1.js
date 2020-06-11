console.log("connected")

$("#id_advert_parts").attr("placeholder", "Select Advert Part")
$("#id_advert_duration").attr("placeholder", "Enter Duration of Advert")
$("#id_sales_person").attr("placeholder", "Enter Name of Sales Person")
$("#id_company").attr("placeholder", "Enter Company Name")

$(document).ready(function(){
  $("input").click(function(){
    $("label").show();
  });
});

$("#id_username").attr("placeholder", "Username")
$("#id_password").attr("placeholder", "Password")

$("#id_prog_name").attr("placeholder", "Enter Name of Program")
$("#id_duration").attr("placeholder", "Enter the Duration of the Program")
$("#id_segmnt").attr("placeholder", "Select Segment")
$("#id_genre").attr("placeholder", "Enter Genre")
$("#id_prog_status").attr("placeholder", "Select Program Status")
$("#id_episode").attr("placeholder", "Select Episode")
$("#id_content_creator").attr("placeholder", "Content Creator")
$("#id_adv").attr("placeholder", "Select Advert(s)")
$("#id_advert_slot").attr("placeholder", "Enter Advert Slot")

$("#id_name").attr("placeholder", "Enter Name")
$("#id_email").attr("placeholder", "Email Address")
$("#id_first_name").attr("placeholder", "First Name")
$("#id_last_name").attr("placeholder", "Surname")
$("#id_dept").attr("placeholder", "Select Department")
$("#id_password1").attr("placeholder", "Password")
$("#id_password2").attr("placeholder", "Confirm Password")
