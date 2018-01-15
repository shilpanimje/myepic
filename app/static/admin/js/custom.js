$(function(){

})

function saveprofile(){
     $.ajax({
      type: 'POST',
      url: '/saveprofile',
      data: $('#profileform').submit(),
      success:function(){
          alert("testing");
      },
      error:function(){
         alert("error");
      }
  });
}
