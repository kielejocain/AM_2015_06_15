
function deleteComment(e) {
       var target = e.target;
       var comment = target.parentNode;
       var parent = comment.parentNode;
       var output = comment.lastChild;

       var text = output.textContent;
       parent.removeChild(comment);

       var fd = new FormData();
       fd.append("text", text);

       request = new XMLHttpRequest();
       var url = "/api_delete_comment/";
       request.onloadend = function () {
           alert("Deleted following Comment: ------- " + this.responseText)
       };
       request.open("post", url, true);
       request.send(fd);
}


function addComment() {
  var cmtr_name = document.getElementById("cmtr_name");
  var cmt_text = document.getElementById("cmt_textf");
  var name = cmtr_name.value;
  console.log(name);
  var comment = cmt_text.value;
  console.log(comment);
  var fd = new FormData();
  fd.append("blog_id", blog_id);
  fd.append("cmtr_name", name);
  fd.append("cmt_text", comment);
  console.log(fd);

  request = new XMLHttpRequest();
  var url2 = "/api_add_comment/";

  request.onload = function() {
    if (request.status === 200) {
      var pub_time = request.responseText;
      console.log(pub_time);
      console.log(pub_time2);


      newContent = ''
      newContent += '<comment id="comment"';
      newContent += '><button id="delcmt">x</button';
      newContent += '><p id="cmt_name">' + name + '</p';
      newContent += '><p id="pub_time">' + pub_time + '</p';
      newContent += '><p id="cmt_txt">' + comment + '</p';
      newContent += '></comment>';

      document.getElementById("parent").innerHTML += newContent;
      footer = document.getElementById("footer");
      footer.setAttribute("style", 'height: 30px')
      setTimeout(function(){
        footer.setAttribute("style", '');
        var cmtr_name = document.getElementById("cmtr_name");
        var cmt_text = document.getElementById("cmt_textf");
        var cmtfrm = document.getElementById("cmtfrm");
        var save = document.getElementById("save");

        cmtfrm.removeChild(cmtr_name);
        cmtfrm.removeChild(cmt_text);
        cmtfrm.removeChild(save);
        cmt_reload = ''
        cmt_reload += '<textarea placeholder="Name" value="{{ comment.cmtr_name }}" name="cmtr_name" id="cmtr_name" class="form2"></textarea>';
        cmt_reload += '<textarea type="text" name="cmt_text" value="{{ comment.cmt_text }}" placeholder="Comment Here........" id="cmt_textf" class="form"></textarea>';
        cmt_reload += '<button id="save" class="form2">Save</button>'

        cmtfrm.innerHTML += cmt_reload;
        var add_comment = document.getElementById("save");
        add_comment.addEventListener('click', addComment, false);
      }, 1500);
    }
  };

  request.open('POST', url2, true);
  request.send(fd);
}


function editBlog() {
  window.location.hash = "#editBlog";
  var blog_content = document.getElementById("blog_content");
  var blog_form = document.getElementById("blog_form");
  var footer = document.getElementById("footer");
  var footer2 = document.getElementById("footer2");

  footer.setAttribute("style", 'display: none');
  footer2.setAttribute("style", 'display: block');
  blog_content.setAttribute("style", 'display: none');
  blog_form.setAttribute("style", 'display: block');


}


function init() {
  window.location.hash = "#blogDetail"
  var add_comment = document.getElementById("save");
  add_comment.addEventListener('click', addComment, false);

  var delete_button = document.getElementById("delcmt");
  delete_button.addEventListener('click', deleteComment, false);

  var edit_blog_button = document.getElementById("icon1");
  edit_blog_button.addEventListener('click', editBlog, false);

  window.addEventListener('hashchange',function() {
    if (window.location.hash == "#editBlog") {
      editBlog();
    } else if (window.location.hash == "#blogDetail") {
      window.location.reload();
    }
  });




}


document.addEventListener("DOMContentLoaded", init);
