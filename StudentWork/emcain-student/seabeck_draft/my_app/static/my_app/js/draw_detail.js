var request = new XMLHttpRequest();

function draw(data) {
    console.log(data);

    //finds the div that we will be putting the data in

    var listdiv = document.getElementById("campers-list");

    //writes the input string "data" to the inside of the div. The line break may not be necessary.

    listdiv.innerHTML = "<br>\n" + data;
}

function drawFormSections(camperid) {

    //this function inserts form elements into a given camper's section. Uses 'addon' spans as the direct
    //parent--this is a Bootstrap feature that causes form elements and labels to line up nicely.

    //by the time this is called, the parent elements have already been created.
    //still need to implement GET and POST functions -- right now it just creates an inert form.

  var id = camperid;

  // food questions section

  var food_div = document.getElementById("food_div_" + id);

  // food_div.style.display = "none";

  var vegetarian = document.createElement("INPUT");
  vegetarian.setAttribute("type", "checkbox");
  vegetarian.setAttribute("id", "vegetarian_" + id);
  vegetarian.setAttribute("class", "diet_form_" + id);

  //not sure if this is the best way to assign classes to elements. Will depend on how they are used.


  document.getElementById("vegetarian_addon_" + id).appendChild(vegetarian);

  var vegan = document.createElement("INPUT");
  vegan.setAttribute("type", "checkbox");
  vegan.setAttribute("id", "vegan_" + id);
  vegan.setAttribute("class", "diet_form_" + id);

  document.getElementById("vegan_addon_" + id).appendChild(vegan);

  var gf = document.createElement("INPUT");
  gf.setAttribute("type", "checkbox");
  gf.setAttribute("id", "gf_" + id);
  gf.setAttribute("class", "diet_form_" + id);

  document.getElementById("gf_addon_" + id).appendChild(gf);

  var df = document.createElement("INPUT");
  df.setAttribute("type", "checkbox");
  df.setAttribute("id", "df_" + id);
  df.setAttribute("class", "diet_form_" + id);

  document.getElementById("df_addon_" + id).appendChild(df);

  // age questions section--only applies to campers under 18.

  var age_div = document.getElementById("age_div_" + id);

  //age_div.style.display = "none";

  var dob = document.createElement("INPUT");
  dob.setAttribute("type", "date");
  dob.setAttribute("id", "dob_" + id);
  dob.setAttribute("class", "diet_form_" + id);

  document.getElementById("dob_addon_" + id).appendChild(dob);

  var grade = document.createElement("INPUT");
  grade.setAttribute("type", "text");
  grade.setAttribute("id", "grade_" + id);
  grade.setAttribute("class", "diet_form_" + id);

  document.getElementById("grade_addon_" + id).appendChild(grade);

  var sponsor = document.createElement("INPUT");
  sponsor.setAttribute("type", "text");
  sponsor.setAttribute("id", "gf_" + id);
  sponsor.setAttribute("class", "diet_form_" + id);

  document.getElementById("sponsor_addon_" + id).appendChild(sponsor);
}


function onRequestChange() {
    console.log(request.readyState, request.status);
    if ((request.readyState == 4) && (request.status == 200)) {
        var data = JSON.parse(request.responseText);
        console.log(data);

        //creates an "output" string that will be used for the camper data's html

        var output = "<div class='container' id='campers_of_family'>";

        //this for loop writes the html for each camper's summary line and form elements

        for (var item in data) {

            //camper's id number will be used to construct DOM elements' id attributes

            var id = data[item].id.toString();

            //creates a div to hold all the stuff about a given camper.
            // Assigns to "active" if there is an attendance record associated with that camper
            // for the latest year.

            output += "<div class='camper-info";

            if (data[item].in_current_year) {
                output += " active' ";
            } else {
                output += "' ";
            }
            output += " data-id='" + id + "'>  ";

            //creates the row that has the camper's name, whether they are attending,
            // and the buttons to edit, delete and register/unregister for this year.
            //still need to add the other buttons and make the buttons do things.

            output += "<div class='row'> \n <div class='col-md-5'>"; //also starts the large column

            output += data[item].name;

            output += " - ";

            //depending on whether the person is attending, makes it say "attending" or "not attending"

            if (!data[item].in_current_year) {
                output += " not";
            }

            output += " attending this year</div> <div class='col-md-2'> <button type='button' class='btn btn-default'>"; // finishes the text section with the name and starts the small column

            //assigns button text depending on what it will do

            if (data[item].in_current_year) {
                output += 'Remove';
            } else {
                output += 'Sign-up';
            }

            // ends 1) the col-md-2 div 2) the row div
            output += "</button> </div></div> \n";


            //creates the food form section. Will eventually create a name change section above that
            //also allows you to check boxes for "food preferences" and "under 18" that will
            // bring up the following two sections if needed. These forms don't do anything yet.

            output += ' <div class="row" id="food_div_' + id + '" class="input-group">\n';
            output += ' <div class="col-md-3" id="vegetarian_col_' + id + '" class="input-group"><span class="input-group-addon">Vegetarian</span><span class="input-group-addon" id="vegetarian_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="vegan_col_' + id + '" class="input-group"><span class="input-group-addon">Vegan</span><span class="input-group-addon" id="vegan_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="gf_col_' + id + '" class="input-group"><span class="input-group-addon">Gluten Free</span><span class="input-group-addon" id="gf_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="df_col_' + id + '" class="input-group"><span class="input-group-addon">Dairy Free</span><span class="input-group-addon" id="df_addon_' + id + '" </span></div>\n </div>';

//creates the form section with questions about children

            output += '<div class="row" id="age_div_' + id + '" >';
            output += '<div class="col-md-4" id="dob_col_' + id + '"  class="input-group"><span class="input-group-addon">Date of Birth</span><span class="input-group-addon" id="dob_addon_' + id + '" </span></div>';
            output += '<div class="col-md-3" id="grade_col_' + id + '" class="input-group"><span class="input-group-addon">Grade</span><span class="input-group-addon" id="grade_addon_' + id + '" </span></div>';
            output += '<div class="col-md-5" id="sponsor_col_' + id + '" class="input-group"><span class="input-group-addon">Sponsor (adult responsible for child)</span><span class="input-group-addon sponsor-addon" id="sponsor_addon_' + id + '" </span></div> </div> </div>';
        }

        //ends the giant string 'output' with a div, and draws it to the appropriate section.

        output += '</div>';
        draw(output);

        //this for loop iterates over the sections we just made, using the original data input to
        //get the relevant camper id numbers and place form fields in the proper places.

        //we have to call 'draw' first so that the DOM elements exist to be appended into.

        for (var item in data) {

            var id = data[item].id.toString();

            drawFormSections(id);
        }
    }


}



function fetch(url) {
    request.onreadystatechange = onRequestChange;
    request.open("GET", url, true);
    request.send();
}



/**
 * Created by Emily on 8/6/2015.
 */
