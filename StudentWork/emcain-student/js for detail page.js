function drawFormSections(camperid) {

  var id = camperid;

  // food questions section

  var food_div = document.getElementById("food_div_" + id);

  // food_div.style.display = "none";

  //need to create this section in the HTML when drawing initial form
  //change this to create <label> or similar objects e.g. <span> and appendChild the inputs into them. won't work otherwise.


  var vegetarian = document.createElement("INPUT");
  // vegetarian.style.display = "none";
  vegetarian.setAttribute("type", "checkbox");
  vegetarian.setAttribute("id", "vegetarian_" + id);
  vegetarian.setAttribute("class", "diet_form " + id);

  document.getElementById("vegetarian_col_" + id).appendChild(vegetarian);

  var vegan = document.createElement("INPUT");
  // vegan.style.display = "none";
  vegan.setAttribute("type", "checkbox");
  vegan.setAttribute("id", "vegan_" + id);
  vegan.setAttribute("class", "diet_form " + id);

  document.getElementById("vegan_col_" + id).appendChild(vegan);

  var gf = document.createElement("INPUT");
  // gf.style.display = "none";
  gf.setAttribute("type", "checkbox");
  gf.setAttribute("id", "gf_" + id);
  gf.setAttribute("class", "diet_form " + id);

  document.getElementById("gf_col_" + id).appendChild(gf);

  var df = document.createElement("INPUT");
  // df.style.display = "none";
  df.setAttribute("type", "checkbox");
  df.setAttribute("id", "df_" + id);
  df.setAttribute("class", "diet_form " + id);

  document.getElementById("df_col_" + id).appendChild(df);

  // edit this to create the age questions section

  var age_div = document.getElementById("age_div_" + id);

  age_div.style.display = "none";

  //need to create this section in the HTML when drawing initial form

  var dob = document.createElement("INPUT");
  // vegetarian.style.display = "none";
  dob.setAttribute("type", "date");
  dob.setAttribute("id", "dob_" + id);
  dob.setAttribute("class", "diet_form " + id);

  document.getElementById("dob_col_" + id).appendChild(dob);

  var grade = document.createElement("INPUT");
  // vegan.style.display = "none";
  grade.setAttribute("type", "text");
  grade.setAttribute("id", "_" + id);
  grade.setAttribute("class", "diet_form " + id);

  document.getElementById("grade_col_" + id).appendChild(grade);

  var sponsor = document.createElement("INPUT");
  // gf.style.display = "none";
  sponsor.setAttribute("type", "text");
  sponsor.setAttribute("id", "gf_" + id);
  sponsor.setAttribute("class", "diet_form " + id);

  document.getElementById("sponsor_col_" + id).appendChild(sponsor);


}
