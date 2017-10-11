//var canvas = document.querySelector("canvas");
var canvas = document.getElementById("myCanvas");

var dc = document.getElementById("dc");
canvas.width = 100;
canvas.height = 100;

//canvas.width = 100;
//canvas.height = 100;

var c = canvas.getContext("2d");
//onload="init()"


var mouse = {
	x: undefined,
	y: undefined
};

var mousepress = false;




window.addEventListener('mousedown', function(event) {
console.log('down');
mousepress = true;
mouse.x = event.x - dc.offsetLeft - canvas.offsetLeft;
mouse.y = event.y - dc.offsetTop - canvas.offsetTop;
console.log('off', mouse.x, mouse.y, dc.offsetTop, dc.offsetLeft);
c.beginPath()
c.moveTo(mouse.x, mouse.y);
});


window.addEventListener('mousemove', function(event) {
console.log('mouse');
mouse.x = event.x - dc.offsetLeft - canvas.offsetLeft;
mouse.y = event.y - dc.offsetTop - canvas.offsetTop;
if (mousepress == true){
	draw();
}
});	

	
window.addEventListener('mouseup', function(event) {
console.log('up');
mousepress = false;
c.closePath();
});
	
window.addEventListener('mouseleave', function(event) {
console.log('up');
mousepress = false;
c.closePath();
});
	
	
function draw(){
	//console.log(mouse.x);
	//console.log(mouse.y);
	c.lineWidth = 8;
	c.lineJoin = "round";
	c.lineTo(mouse.x, mouse.y);
	//c.lineTo(mouse.x - dc.offsetLeft - canvas.offsetLeft, mouse.y - dc.offsetTop - canvas.offsetTop);
	c.stroke();
}


function erase() {
	c.clearRect(0, 0, c.canvas.width, c.canvas.height);
}

function guess(){
	//var digit = {{ digit }}
	//document.getElementById("dc").value = digit;
	console.log('guess');
		}
