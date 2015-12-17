// Stepper Motor Sketch to use with Lidar
// Rotates NEMA 17 350 mA motor at 20 sec / 1 revolution

// resolution of capture: 1, 2, 4, or 8 (1 is standard, 8 is highres)
const int resolution = 1;

const int directionPin = 9;
const int stepPin = 8;

unsigned long curMillis;
unsigned long prevStepMillis = 0;

// milliseconds between each step of the motor
unsigned long millisBetweenSteps = 100;

int nSteps;

void setup () {
  Serial.begin(9600);
  
  // set pin modes
  pinMode(directionPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  
  // set direction
  // CW:   directionPin = LOW
  // CCW:  directionPin = HIGH
  digitalWrite(directionPin, HIGH);
  
  // based on the resolution, find the number of 1/8 steps the motor will take
  // each time
  double power = log(double(resolution)) / log(2.);
  power = 3. - power;
  nSteps = int(pow(2., power));
  Serial.println(nSteps);
}

void loop () {
  // find the next time
  curMillis = millis();
  
  // if the current time is more than the previous time + the step,
  // move the motor one step
  if (curMillis - prevStepMillis >= millisBetweenSteps) {
    prevStepMillis += millisBetweenSteps;
    
    // make the motor turn a 1/8 step nSteps times
    for (int i = 0; i < nSteps; i ++) { // put 8 to get max (reference) step
      
      digitalWrite(stepPin, HIGH);
      digitalWrite(stepPin, LOW);
      
      delay(10); // wait for the motor to move to position
    }
  }
  
}
