var request = new XMLHttpRequest();

function draw(data) {
    console.log(data);
    var listdiv = document.getElementById("campers-list");


    listdiv.innerHTML = "<br>\n" + data;
}

function drawFormSections(camperid) {

  var id = camperid;

  // food questions section

  var food_div = document.getElementById("food_div_" + id);

  // food_div.style.display = "none";


  var vegetarian = document.createElement("INPUT");
  vegetarian.setAttribute("type", "checkbox");
  vegetarian.setAttribute("id", "vegetarian_" + id);
  vegetarian.setAttribute("class", "diet_form " + id);

  document.getElementById("vegetarian_addon_" + id).appendChild(vegetarian);

  var vegan = document.createElement("INPUT");
  // vegan.style.display = "none";
  vegan.setAttribute("type", "checkbox");
  vegan.setAttribute("id", "vegan_" + id);
  vegan.setAttribute("class", "diet_form " + id);

  document.getElementById("vegan_addon_" + id).appendChild(vegan);

  var gf = document.createElement("INPUT");
  // gf.style.display = "none";
  gf.setAttribute("type", "checkbox");
  gf.setAttribute("id", "gf_" + id);
  gf.setAttribute("class", "diet_form " + id);

  document.getElementById("gf_addon_" + id).appendChild(gf);

  var df = document.createElement("INPUT");
  // df.style.display = "none";
  df.setAttribute("type", "checkbox");
  df.setAttribute("id", "df_" + id);
  df.setAttribute("class", "diet_form " + id);

  document.getElementById("df_addon_" + id).appendChild(df);

  // edit this to create the age questions section

  var age_div = document.getElementById("age_div_" + id);

  //age_div.style.display = "none";

  //need to create this section in the HTML when drawing initial form

  var dob = document.createElement("INPUT");
  // vegetarian.style.display = "none";
  dob.setAttribute("type", "date");
  dob.setAttribute("id", "dob_" + id);
  dob.setAttribute("class", "diet_form " + id);

  document.getElementById("dob_addon_" + id).appendChild(dob);

  var grade = document.createElement("INPUT");
  // vegan.style.display = "none";
  grade.setAttribute("type", "text");
  grade.setAttribute("id", "grade_" + id);
  grade.setAttribute("class", "diet_form " + id); // fix the class here

  document.getElementById("grade_addon_" + id).appendChild(grade);

  var sponsor = document.createElement("INPUT");
  // gf.style.display = "none";
  sponsor.setAttribute("type", "text");
  sponsor.setAttribute("id", "gf_" + id);
  sponsor.setAttribute("class", "diet_form " + id);

  document.getElementById("sponsor_addon_" + id).appendChild(sponsor);

}


function onRequestChange() {
    console.log(request.readyState, request.status);
    if ((request.readyState == 4) && (request.status == 200)) {
        var data = JSON.parse(request.responseText);
        console.log(data);
        var output = "<div class='container' id='campers_of_family'>";
        for (var item in data) {

            var id = data[item].id.toString();

            output += "<div class='camper-info";

            if (data[item].in_current_year) {
                output += " active' ";
            } else {
                output += "' ";
            }
            output += " data-id='" + id + "'>  ";



            output += "<div class='row'> \n <div class='col-md-5'>";

            output += data[item].name;

            output += " - ";

            if (!data[item].in_current_year) {
                output += " not";
            }

            output += " attending this year</div> <div class='col-md-2'> <button type='button' class='btn btn-default'>";

            if (data[item].in_current_year) {
                output += 'Remove';
            } else {
                output += 'Sign-up';
            }
            output += "</button> </div></div></div> \n";

            //output += "</div>";



            console.log("adding form elements for id " + id);

            output += ' <div class="row" id="food_div_' + id + '" class="input-group">\n';
            output += ' <div class="col-md-3" id="vegetarian_col_' + id + '" class="input-group"><span class="input-group-addon">Vegetarian</span><span class="input-group-addon" id="vegetarian_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="vegan_col_' + id + '" class="input-group"><span class="input-group-addon">Vegan</span><span class="input-group-addon" id="vegan_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="gf_col_' + id + '" class="input-group"><span class="input-group-addon">Gluten Free</span><span class="input-group-addon" id="gf_addon_' + id + '" </span></div>\n';
            output += ' <div class="col-md-3" id="df_col_' + id + '" class="input-group"><span class="input-group-addon">Dairy Free</span><span class="input-group-addon" id="df_addon_' + id + '" </span></div>\n </div>';

            console.log('form elements added');


<!--  concat the id number of the person onto the end of id numbers above-->
            output += '<div class="row" id="age_div_' + id + '" >';
            output += '<div class="col-md-4" id="dob_col_' + id + '"  class="input-group"><span class="input-group-addon">Date of Birth</span><span class="input-group-addon" id="dob_addon_' + id + '" </span></div>';
            output += '<div class="col-md-3" id="grade_col_' + id + '" class="input-group"><span class="input-group-addon">Grade</span><span class="input-group-addon" id="grade_addon_' + id + '" </span></div>';
            output += '<div class="col-md-5" id="sponsor_col_' + id + '" class="input-group"><span class="input-group-addon">Sponsor (adult responsible for child)</span><span class="input-group-addon sponsor-addon" id="sponsor_addon_' + id + '" </span></div> </div> </div>';
        }
        output += '</div>';
        draw(output);
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


// add another function that uses JS to add the elements

/**
 * Created by Emily on 8/6/2015.
 */
