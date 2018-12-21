#include <Servo.h>
#define LEFT_AHEAD 10
#define LEFT_BACK 9
#define RIGHT_AHEAD 12
#define RIGHT_BACK 13
#define STEER 14
#define RUN 60
#define RUN1 50
#define RUNFAST 255
#define STOP 0
Servo servo;
char operation;

void setup() {
  Serial.begin(9600);
  pinMode(LEFT_AHEAD, OUTPUT);
  pinMode(LEFT_BACK, OUTPUT);
  pinMode(RIGHT_AHEAD, OUTPUT);
  pinMode(RIGHT_BACK, OUTPUT);
  digitalWrite(LEFT_AHEAD, LOW);
  digitalWrite(LEFT_BACK, LOW);
  digitalWrite(RIGHT_AHEAD, LOW);
  digitalWrite(RIGHT_BACK, LOW);
  servo.attach(STEER);
  digitalWrite(STEER, LOW);
}

void loop() {
  if(Serial.available() > 0)
  {
    operation = Serial.read();
    switch(operation)
    {
      case 'A':
        Serial.println("GO STRAIGHT");
        goAhead();
        break;
      case 'L':
        Serial.println("TURN LEFT");
        turnLeft();
        break;
      case 'R':
        Serial.println("TURN RIGHT");
        turnRight();
        break;
      case 'B':
        Serial.println("GO BACK");
        goBack();
        break;
      case 'P': case 'S':
        Serial.println("PARK");
        park();
        break;
      case 'F':
        Serial.println("GO AHEAD FAST");
        goAheadFast();
        break;
      case 'C':
        Serial.println("GO BACK FAST");
        goBackFast();
        break;
      case 'M':
        Serial.println("GO LEFT ANGLE");
        turnLeftAngle();
        break;
      case 'N':
        Serial.println("GO RIGHT ANGLE");
        turnRightAngle();
        break;
    }
  }
}

void park()
{
 servo.write(90);
 analogWrite(LEFT_AHEAD, STOP);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, STOP);
 analogWrite(RIGHT_BACK, STOP);
}

void goAhead()
{
 servo.write(90);
 analogWrite(LEFT_AHEAD, RUN);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, RUN);
 analogWrite(RIGHT_BACK, STOP);
}

void goBack()
{
 servo.write(90);
 analogWrite(LEFT_AHEAD, STOP);
 analogWrite(LEFT_BACK, RUN);
 analogWrite(RIGHT_AHEAD, STOP);
 analogWrite(RIGHT_BACK, RUN);
}

void turnLeft()
{
 servo.write(60);
 analogWrite(LEFT_AHEAD, STOP);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, RUN);
 analogWrite(RIGHT_BACK, STOP);
}

void turnRight()
{
 servo.write(120);
 analogWrite(LEFT_AHEAD, RUN);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, STOP);
 analogWrite(RIGHT_BACK, STOP);
}

void goAheadFast()
{
 servo.write(90);
 analogWrite(LEFT_AHEAD, RUNFAST);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, RUNFAST);
 analogWrite(RIGHT_BACK, STOP);
}

void goBackFast()
{
 servo.write(90);
 analogWrite(LEFT_AHEAD, STOP);
 analogWrite(LEFT_BACK, RUNFAST);
 analogWrite(RIGHT_AHEAD, STOP);
 analogWrite(RIGHT_BACK, RUNFAST);
}

void turnLeftAngle()
{
 servo.write(60);
 analogWrite(LEFT_AHEAD, RUN1);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, RUNFAST);
 analogWrite(RIGHT_BACK, STOP);
}

void turnRightAngle()
{
 servo.write(120);
 analogWrite(LEFT_AHEAD, RUNFAST);
 analogWrite(LEFT_BACK, STOP);
 analogWrite(RIGHT_AHEAD, RUN1);
 analogWrite(RIGHT_BACK, STOP);
}
