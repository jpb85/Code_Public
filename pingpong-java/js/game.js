// RequestAnimFrame: a browser API for getting smooth animations
window.requestAnimFrame = (function(){
	return  window.requestAnimationFrame       ||
			window.webkitRequestAnimationFrame ||
			window.mozRequestAnimationFrame    ||
			window.oRequestAnimationFrame      ||
			window.msRequestAnimationFrame     ||
		function( callback ){
			return window.setTimeout(callback, 1000 / 60);
		};
})();

window.cancelRequestAnimFrame = ( function() {
	return  window.cancelAnimationFrame              ||
			window.webkitCancelRequestAnimationFrame ||
			window.mozCancelRequestAnimationFrame    ||
			window.oCancelRequestAnimationFrame      ||
			window.msCancelRequestAnimationFrame     ||
		clearTimeout;
} )();
// DO NOT TOUCH CODE ABOVE!!

console.log('What UP');

// Initialize canvas and other variables
var canvas = document.getElementById("canvas"); // Store HTML5 canvas tag into JS variable
var ctx = canvas.getContext("2d"); // Create canvas 2d context
var W = window.innerWidth; // Browser window width
var H = window.innerHeight; // Browser window height
mouse = {}; // Mouse object to store its current position
startBtn = {}; // Start button Object
restartBtn = {}; // Restart Object
ball = {}; // Ball Object
var paddles = [];
var hits = 0;
var flagCollision = 0; // Flag variable is changed on collision
var flagGameOver = true; // Flag variable is changed on game over
var particles = []; //array of sparks when ball hits a paddle
var particleCount = 25; //number of sparks per contact
var particlePos = {} //object to contain the position of collisions
var particleDir = 1; //direction of sparks
var init; // Variable used to initalize animation
var paddleHit; // Which paddle was hit 0 (top) or 1 (bottom)
var overFlag = 0;
var keyDirL = 0;
var keyDirR = 0;
// console.log('the browser width is currently: ' + W);
// console.log('the browser height is currently: ' + H);

// Set the canvas width and height to match the browser
canvas.width = W;
canvas.height = H;

canvas.addEventListener("mousemove", trackPosition, true);
canvas.addEventListener("mousedown", btnClick, true);

document.addEventListener("keydown", keyPressed, true);
document.addEventListener("keyup", keyReleased, true);

var collision = document.getElementById("collide");

var currTime = 0;
var newTime = 0;
var min = 0;
var sec = 0;
var timeStr = '';
var timerDisplay ='00:00';
var watchID;

function updateWatch(){
 //call this function everysecond.
 currTime+=1;
 newTime = 0 + currTime;
 timerDisplay = clockTime(newTime);
}
//300
function clockTime(pTime){
 // convert seconds into clock time format.
 min = Math.floor(pTime/60);
 sec = pTime%60;
 if(sec >= 10){
  timeStr = '0' + min + ':' + sec;
  }else{
  timeStr = '0' + min + ':0' + sec; 
  }
 
 return timeStr;
 
}

function trackPosition(e) {
	mouse.x = e.pageX;
	mouse.y = e.pageY;
	// console.log("cursor X is at: " + mouse.x);
	// console.log("cursor Y is at: " + mouse.y);
}

function startScreen() {
	draw();
	startBtn.draw();
}

function paintCanvas() {
	ctx.fillStyle = "black";
	ctx.fillRect(0, 0, W, H);
}

function Paddle(pos) {
	// Height and Width
	this.h = 150;
	this.w = 5;

	// Paddle's position
	this.y = H/2 - this.h/2;
	this.x = (pos == "right") ? 0 : W - this.w;
}

paddles.push(new Paddle("left"));
//console.log("paddles array is: " + paddles);
paddles.push(new Paddle("right"));
//console.log("paddles array is: " + paddles);

ball = {
	x: 50,
	y: 50,
	r: 5,
	c: "white",
	vx: 4,
	vy: 8,

	draw: function() {
		ctx.beginPath();
		ctx.fillStyle = this.c;
		ctx.arc(this.x, this.y, this.r, 0, Math.PI*2, false);
		ctx.fill();
	}
};

function speedUpDraw(){
	ctx.fillStlye = "white";
	ctx.font = "16px Arial, sans-serif";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("Speed up", W/2 - 15, 50 );
}
function timerDraw(){
	ctx.fillStlye = "white";
	ctx.font = "16px Arial, sans-serif";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("Timer: " + timerDisplay, W/2 - 15, 50 );
}
function draw() {
	// Paint canvas the color black
	paintCanvas();
	
	// Put paddles on top of my fresh canvas
	for(var i = 0; i < paddles.length; i++) {
		p = paddles[i];
        if (i < 1){
		ctx.fillStyle = "orange";
		ctx.fillRect(p.x, p.y, p.w, p.h);
        } else if (i == 1){
        ctx.fillStyle = "purple";
		ctx.fillRect(p.x, p.y, p.w, p.h); 
        } else {
        }
	}
	
	
	// Put the ball on top of canvas
	ball.draw();

	// Update a.k.a animate all objects on the canvas
	update();
}

function update() {
	// Main game logic, including movement, score updates, collision, etc
    updateHit();
	timerDraw();
	// update paddles position
	
	
	//console.log(p.y);
	//console.log(keyDir);
	
	pR = paddles[0];
	if(pR.y > 0 && keyDirR < 0)
	pR.y = pR.y + keyDirR;
	if(pR.y < H - 150 && keyDirR > 0)
    pR.y = pR.y + keyDirR;
	console.log(pR.y);
	
	pL = paddles[1];
	if(pL.y > 0 && keyDirL < 0)
	pL.y = pL.y + keyDirL;
	if(pL.y < H - 150 && keyDirL > 0)
    pL.y = pL.y + keyDirL;
	
	
	//pR = paddles[0];
	//pR.y = pR.y + keyDirR;
	
	// Move ball
	ball.x += ball.vx;
	ball.y += ball.vy;

	pLeft = paddles[0];
	pRight = paddles[1];

	// If the ball strikes a paddle,
	// invert the y-velocity vector of ball
	if (collides(ball, pLeft)){
		collideAction(ball, pLeft);
	} else if (collides(ball, pRight)) {
		collideAction(ball, pRight);
	} else {
		// Check for game over
		if (ball.x + ball.r > W) {
			ball.x = H - ball.r;
			gameOver();
		} else if (ball.x < 0) {
			ball.x = ball.r;
			gameOver();
		}
		// If ball strikes a wall,
		// invert direction x-velocity.
		if (ball.y + ball.r > H) {
			// bounce from right to left
			ball.vy = -ball.vy;
			ball.y = H - ball.r;
		} else if (ball.y - ball.r < 0) {
			// bounce from left to right
			ball.vy = -ball.vy;
			ball.y = ball.r;
		}
    } 
    //if flagCollision is true, push the particles
    if (flagCollision == true){
        for (var k = 0; k < particleCount; k++){
            particles.push(new createParticles(particlePos.x, particlePos.y, particleDir));
        }
        
    }
    //emit particle sparks
    emitParticles();
    
    //reset flagCollision
    
    flagCollision=false;
} //Update function close



//USEd to create particle objects
function createParticles(x, y, d){
    this.x = x || 0;
    this.y = y || 0;
    
    this.radius = 1.2;
    
    this.vx = -1.5 + Math.random()*3;
    this.vy = d * Math.random() * 1.5;
}

function emitParticles(){
    for(var j = 0; j < particles.length; j++){
        par = particles[j];
        
        ctx.beginPath();
        ctx.fillStyle = ball.c;
        if (par.radius > 0) {
            ctx.arc(par.x, par.y, par.radius, 0, Math.PI*2, false);
        }
        ctx.fill();
        par.x += par.vx;
        par.y += par.vy;
        
        //reduce particle radius
        par.radius = Math.max(par.radius - 0.05, 0.0);
    }
}
// Function for updating hits
function updateHit() {
	ctx.fillStyle = "white";
	ctx.font = "20px Arial, sans-serif";
	ctx.textAlign = "left";
	ctx.textBaseline = "top";
	ctx.fillText("Hits: " + hits, W/2, 25 );
}
function gameOver() {
 ctx.fillStlye = "white";
 ctx.font = "20px Arial, sans-serif";
 ctx.textAlign = "center";
 ctx.textBaseline = "middle";
 ctx.fillText("Game Over", W/2, H/2 -100 );
 //stop time
 clearInterval(watchID);
 
 // Stop the Animation
 cancelRequestAnimFrame(init);
 
 // Set the over flag
 overFlag = 1;
 
 // Show the restart button
 restartBtn.draw();
 winner.draw();
}

winner = {
    draw: function(){
	  ctx.font = "20px , Arial, sans-serif";
	  ctx.textAlign = "center";
	  ctx.textBaseline = "middle";
	  ctx.fillStyle = ball.c;
	  if( ball.c == "white"){
	   ctx.fillStyle = "purple";
	  ctx.fillText("Left Player Wins", W/2, H/2 +50);
	  }
	   if( ball.c == "orange"){
	  ctx.fillText("Right Player Wins", W/2, H/2 +50);
	  }
	   if( ball.c == "purple"){
	  ctx.fillText("Left Player Wins", W/2, H/2 +50);
	  }
 }
};

restartBtn = {
	w: 100,
	h: 50,
	x: W/2 - 50,
	y: H/2 - 50,
	draw: function() {
		
		ctx.strokeStyle = "white";
		ctx.lineWidth = "1";
		ctx.strokeRect(this.x, this.y, this.w, this.h);
		ctx.font = "18px Arial, sans-serif";
		ctx.textAlign = "center";
		ctx.textBaseline = "middle";
		ctx.fillStyle = "white";
		ctx.fillText("Restart", W/2, H/2 -25);
	}
};

function collides(b, p) {
	// Check collision of ball with one paddle
	if (b.y + b.r >= p.y && b.y - b.r <= p.y + p.h) {
		if (b.x >= (p.x - p.w) && p.x > 0){
			//console.log ("paddle hit right");
			paddleHit = 0;
            ball.c = "orange";
			return true;
		} else if (b.x <= p.w && p.x === 0) {
			//console.log ("paddle hit left");
			paddleHit = 1;
            ball.c = "purple";            
			return true;
		}
	} else {
		return false;
	}
}

function collideAction(b, p) {
    collision.play();
 b.vx = -b.vx;
 if (paddleHit == 0) {
		b.x = p.x - p.w;
        particleDir = -1;
        particlePos.y = ball.y - ball.r;
 } else if (paddleHit == 1) {
		b.x = p.w + b.r;
        particleDir = 1;
        particlePos.y = ball.y + ball.r;
 }
	hits++;
	increaseSpeed();
    particlePos.x = ball.x;
    flagCollision = true;
}
function increaseSpeed() {
 if(hits % 5 == 0) {
   ball.vx += (ball.vx < 0) ? -1 : 1;
   ball.vy += (ball.vy < 0) ? -2 : 2;
 }
}

startBtn = {
	w: 100,
	h: 50,
	x: W/2 - 50,
	y: H/2 - 25,

	draw: function() {
		ctx.strokeStyle = "white";
		ctx.lineWidth = "2";
		ctx.strokeRect(this.x, this.y, this.w, this.h);

		ctx.font = "12px Arial, sans-serif";
		ctx.textAlign = "center";
		ctx.textBaseline = "middle";
		ctx.fillStyle = "white";
		ctx.fillText("Start", W/2, H/2);
	}
};

function animloop() {
	init = requestAnimFrame(animloop);
	draw();
}

function btnClick(e) {
 

 var mx = e.pageX,
   my = e.pageY;
 
 if(mx >= startBtn.x && mx <= startBtn.x + startBtn.w) {
	ball.c = "white";
  animloop();
  watchID = setInterval(updateWatch, 1000);
  startBtn = {};
  
 }
 

 
 if(overFlag == 1) {
  if(mx >= restartBtn.x && mx <= restartBtn.x + restartBtn.w) {
   ball.c = "white";
   ball.y = 20;
   hits = 0;
   ball.vx = 4;
   ball.vy = 8;
   
   newTime = 0;
   currTime = 0;
   
   timerDisplay = "00:00"
   watchID = setInterval(updateWatch, 1000);
   
   animloop();
   
   overFlag = 0;
  }
 }
}

function keyPressed(e) {
	var myKey = e.keyCode;
	console.log("Key pressed is: " + myKey);
	if (flagGameOver == 1) {
		if  (myKey == 87) { // "w" key move left paddle up
			keyDirL = -10;
			console.log("wwww");
		} else if (myKey == 83) { // "s" key move left paddle down
			keyDirL = 10;
		} else if(myKey == 79) { // "o" key move right paddle up
			keyDirR = -10;
		}else if(myKey == 76) {//"l" key move right paddle down
			keyDirR = 10;
		}
	}
}
function keyReleased(e){
	keyDirR = 0;
	keyDirL = 0;
	
}


// Show the start screen
startScreen();

















