#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

// Set up software serial on pins D4 (Rx) and D5 (Tx)
SoftwareSerial Serial1(2, 3);  // RX on D2, TX on D3
DFRobotDFPlayerMini Player1;

SoftwareSerial Serial2(4, 5);  // RX on D4, TX on D5
DFRobotDFPlayerMini Player2;

SoftwareSerial Serial3(6, 7);  // RX on D6, TX on D7
DFRobotDFPlayerMini Player3;

SoftwareSerial Serial4(8, 9);  // RX on D8, TX on D9
DFRobotDFPlayerMini Player4;

int state = 0;

int a = 20;
int b = 20;
int c = 20;
int d = 20;


void setup() {
  // put your setup code here, to run once:

  Serial1.begin(9600);
  Serial2.begin(9600);
  Serial3.begin(9600);
  Serial4.begin(9600);

  Serial.begin(115200); 

//potentiometer
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);

 // pinMode(8,INPUT);
  // Initialize DFPlayer Mini

  Serial1.listen();
    if (!Player1.begin(Serial1)) { 
        Serial.println("DFPlayer Mini 1 not detected or error.");
        while(true);
    }
    //Player1.volume(a);

  Serial2.listen();
    if (!Player2.begin(Serial2)) { 
        Serial.println("DFPlayer Mini 2 not detected or error.");
        while(true);
    }
    //Player2.volume(b);

  Serial3.listen();
    if (!Player3.begin(Serial3)) { 
        Serial.println("DFPlayer Mini 3 not detected or error.");
        while(true);
    }
    //Player3.volume(c);


  Serial4.listen();
    if (!Player4.begin(Serial4)) { 
        Serial.println("DFPlayer Mini 4 not detected or error.");
        while(true);
    }

  
}

void loop() {
  // put your main code here, to run repeatedly:

  Player1.volume(a);
  Player2.volume(b);
  Player3.volume(c);
  Player4.volume(d);

   // if (digitalRead(8)==LOW) {
      Player1.playFolder(01, 1);
      Player2.playFolder(01, 2);
      Player3.playFolder(01, 3);
      Player4.playFolder(01, 4);
      //delay(100000);
    //}


  int  sensor_value1 = analogRead(A0);
  int  sensor_value2 = analogRead(A1);
  int  sensor_value3 = analogRead(A2);
  int  sensor_value4 = analogRead(A3);

  Serial.print("Value 1:");
  Serial.print(sensor_value1);
  Serial.print("\t");
  
  Serial.print("Value 2:");
  Serial.print(sensor_value2);
  Serial.print("\t");
  
  Serial.print("Value 3:");
  Serial.print(sensor_value3);
  Serial.print("\t");

  Serial.print("Value 4:");
  Serial.print(sensor_value4);
  Serial.print("\t");

  Serial.print(state);
  Serial.println();
  Serial.print("\t");
  delay(100);


  if (sensor_value1<550){
    state=0;
    a=0;
  }

  if (sensor_value1>550){
    state=1;
    a=20;
  }
}
