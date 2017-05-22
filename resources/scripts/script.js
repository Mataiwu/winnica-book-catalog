//console.log('ready')


//grab author
var authors_grab=document.querySelectorAll(".authors-list-q");
//when hovering

function fName(){
  var d={{author.first_name}};
  this.textContent=d;
}

function authorAddInfo(){
    console.log('helou');
    for (var i=0; i<authors_grab.length; i++){
      authors_grab[i].addEventListener('mouseover', fName);
    //  authors_grab[i].style.color='red';
    //  console.log('how du ju du');
    }
}
