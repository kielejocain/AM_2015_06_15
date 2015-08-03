/**
 * Created by Emily on 7/30/2015.
 */


/**
 * Things to accomplish:
 * - hide unused form sections (start with name stuff from "edit camper" page)
 * - create edit and delete functions
 * - assign edit and delete functions to appropriate buttons--find by regex?????
 * - create a save/post function
 * - create save button; assign save function to button and to edit/delete buttons clicked when an edit line is open
 * --------
 * after above is done:
 * - add other sections as hidden, reveal dynamically based on options chosen in basic "edit" form
 * - create another section to list attendances of campers who are in this year's registration
 * - have campers you create above automatically added to the bottom section as attendances
 * - create buttons to add individual campers (line by line) as well as one to add all campers.
 * - have buttons to remove or edit attendances. (eventually figure out how to handle housing and part time people)*/


var registrant_id = 1;
function campers(e) {
    console.log(e);
    var data = JSON.parse(e.target.responseText)
    console.log(data)
}
function getCampers() {
    var request = new XMLHttpRequest();
    request.open("GET", "/api_campers/" + registrant_id);
    request.onload = campers;
    request.send();
}
getCampers();


