


///////////////// I LOST MY CODE DUE TO NOT SAVING AND TRIED TO RECREATE EVERYTHING
////////////////// BUT THERE WAS NO TIME, SO THE GAME IS NOT FUNCTIONAL


let SCREEN_WIDTH = 600;
let SCREEN_HEIGHT = 600;
let UNIT_SIZE = 25;
let GAME_UNITS = (SCREEN_WIDTH*SCREEN_HEIGHT)/UNIT_SIZE;
let DELAY = 75; //the higher the slower the game
x= [GAME_UNITS]; 
y =  [GAME_UNITS];
let bodyParts = 6;
let applesEaten; 
let appleX; //location of apple
let appleY;
let direction= 'R';
let running = false;
let timer;
let random; 
let sec = 0;
let context;
let div;





    function init() {

        canvas = document.getElementById( 'frame' );
        div = document.getElementById('snake')
        // console.log(canvas.getContext);
        if (canvas && canvas.getContext) {
            
            context = canvas.getContext('2d');
            console.log(context);

            // Register event listeners
            // document.addEventListener('mousemove', documentMouseMoveHandler, false);
            // window.addEventListener('resize', windowResizeHandler, false);
            // windowResizeHandler();
            startGame()

            // setInterval( loop, 1000 / 30 );
        }
    }

function GamePanel(){
    random = new random ();
    this.setPreferredSize(new Dimension(SCREEN_WIDTH,SCREEN_HEIGHT));
    this.setBackground(Color.black);
    this.setFocusable(true);
    this.addKeyListener(new MyKeyAdapter());
    canvas = document.getElementById( 'frame' );

    if (canvas && canvas.getContext) {
        context = canvas.getContext('2d');

         windowResizeHandler();

        setInterval( loop, 1000 / 30 );
    }



    startGame();

}

function startGame() {
    newApple();
    running = true; 
    // timer = new Timer(DELAY, this);
    // timer.start();
    timer = setInterval(()=>{
        sec++;
        DELAY++;
        console.log(DELAY);
        // this.paintComponent(context);
    draw(context);
    },1000)
}

function paintComponent() {
    this.paintComponent(context);
    draw(context);
};

function drawLine(x,y){
context.beginPath();
context.moveTo(x, y);
context.lineTo(x, y);
context.stroke();
}

function draw () {
 console.log(sec);
    if(running) {
        for (let i=0;i<SCREEN_HEIGHT/UNIT_SIZE;i++) {
            drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);
            drawLine(0,i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);
        }
    
      
        // context.style.color = 'red'
        
        context.ellipse(appleX, appleY, UNIT_SIZE, UNIT_SIZE);
        
    
        for(let i=0; i<bodyParts; i++) {
            if(i==0) {
               
                div.style.color = 'green'
                div.fillRect(x[i],y[i],UNIT_SIZE, UNIT_SIZE);
            }
            else {
                // div.setColor(new Color(45,180,0));
                // div.setColor(new Color(random.nextInt(255)));
                div.fillRect(x[i],y[i],UNIT_SIZE, UNIT_SIZE);
            
            }
        }
        context.setColor(Color.red);
        context.setFont(new Font("Ink Free",Font.BOLD, 40));
        //lines up in centre of screen
        // metrics = getFontMetrics(context.getFont());
        metrics = TextMetrics(context.getFont());
        context.filltext("Score: "+applesEaten, (SCREEN_WIDTH - metrics.stringWidth("Score: "+applesEaten))/2, g.getFont().getSize());
        
        }
    else {
        gameOver(context);
        }
};

function newApple() {
    // console.log(random);
    appleX = Math.random(SCREEN_WIDTH/UNIT_SIZE)*UNIT_SIZE;
    appleY = Math.random(SCREEN_HEIGHT/UNIT_SIZE)*UNIT_SIZE;

}

function move() {
    //iterates through all the bodyparts
    for(let i=bodyParts;i>0;i--) {
        //shifting arrays by one spot
        x[i] = x[i-1];
        y[i] = y[i-1];
        
    }
    //switch the direction where the snake is headed
    switch(direction) {
    case 'U':
        y[0] = y[0]- UNIT_SIZE;
        break;
    case 'D':
        y[0] = y[0] + UNIT_SIZE;
        break;
    case 'L':
        x[0] = x[0]- UNIT_SIZE;
        break;
    case 'R':
        x[0] = x[0] +UNIT_SIZE;
        break;
    }
    
};

function checkApple() {
    if((x[0] == appleX) && (y[0] == appleY)) {
        //snake grows after each eaten apple
        bodyParts++;
        //score
        applesEaten++;
        //generates new apple
        newApple();
    }
    
};
function checkCollisions() {
    //check if head collides with body, if so game over
    //x[0] is the head of the snake
    for(let i =bodyParts;i>0;i--) {
        if((x[0] == x[i]) && (y[0] == y[i])) {
            running = false;
        }
    }
    //check if head touches left border
    if(x[0] <0 ) {
        running = false;
    }
    //check if head touches right border
    if(x[0] > SCREEN_WIDTH ) {
        running = false;
    }
    //check if head touches top border
    if(y[0] < 0) {
        running = false;
    }
    //check if head touches bottom border
    if(y[0] > SCREEN_HEIGHT ) {
        running = false;
    }
    if(!running) {
        // timer.stop();
        clearInterval(timer)
    }
    
};
function gameOver() {
    //Score
    // cpntext.setColor(Color.red);
    // context.setFont(new Font("Ink Free",Font.BOLD, 40));
    //lines up in centre of screen
    //  metrics1 = TextMetrics(context.getFont());
    // context.drawString("Score: "+applesEaten, (SCREEN_WIDTH - metrics1.stringWidth("Score: "+applesEaten))/2, g.getFont().getSize());
    
    //Game over text 
    // context.setColor(Color.red);
    context.style.color = 'red'
    // context.setFont.BOL
    // context.setFont(new Font("Ink Free",Font.BOLD, 75));
    //lines up in centre of screen
    //  metrics2 = getFontMetrics(g.getFont());
     metrics2 = TextMetrics(context.getFont());
    context.filltext("Game over", (SCREEN_WIDTH - metrics2.stringWidth("Game Over"))/2, SCREEN_HEIGHT/2);
    clearInterval(timer)
};

// @Override
function actionPerformed() {
    // TODO Auto-generated method stub
    //check if game is running
    
    if(running) {
        //move the snake
        move();
        //check if we ran into apple
        checkApple();
        checkCollisions();
    }
    //if game is no longer running 
    // repaint();
}


//inner class

    // @Override
    function keyPressed() {
        switch(e.getKeyCode()) {
        case KeyEvent.VK_LEFT:
        if(direction != 'R') {
            direction = 'L';
        }
        break;
        case KeyEvent.VK_RIGHT:
            if(direction != 'L') {
                direction = 'R';
            }
            break;
        case KeyEvent.VK_UP:
            if(direction != 'D') {
                direction = 'U';
            }
            break;
        case KeyEvent.VK_DOWN:
            if(direction != 'U') {
                direction = 'D';
            }
            break;
        
        
        }
        
    }

    init()


// }	