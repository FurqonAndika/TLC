#define button_parkingBrake 2
#define button_headLamp 3
#define led_indicator 4
#define pot_speed A5

bool now_state_parkingBrake = false;
bool prev_state_parkingBrake = false;
bool parkingBrake = false;

bool now_state_headLamp = false;
bool prev_state_headLamp = false;
bool headLamp = false;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

pinMode(led_indicator, OUTPUT);
pinMode(button_parkingBrake, INPUT_PULLUP);
pinMode(button_headLamp, INPUT_PULLUP);
pinMode(pot_speed, INPUT);
}



void loop() {
  // read potensio value
  int speed = analogRead(pot_speed); //0-1023
  speed = map(speed,0,1023,0,150); //0-150

  //read button parkingBrake
  now_state_parkingBrake = !digitalRead(button_parkingBrake);
  if(now_state_parkingBrake==true){
    if(prev_state_parkingBrake!=now_state_parkingBrake){
      //prev_state=now_state
      parkingBrake = !parkingBrake;
    }
  }
  prev_state_parkingBrake = now_state_parkingBrake;

  //read button headLamp
   now_state_headLamp = !digitalRead(button_headLamp);
  if(now_state_headLamp==true){
    if(prev_state_headLamp!=now_state_headLamp){
      //prev_state=now_state
      headLamp = !headLamp;
    }
  }
  prev_state_headLamp = now_state_headLamp;

  //send data to python via serial communication
  //data yang akan di kirim: speed, rpm, parkingBrake, headLamp

  String data_send ="";
  data_send +=String(speed);
  data_send +=",";
  data_send +=String(0);
  data_send +=",";
  data_send +=String(parkingBrake);
  data_send +=",";
  data_send +=String(headLamp);

  Serial.println(data_send);

  //receive data from python via serial
  if(Serial.available()>1){
    String data = Serial.readString();
    if(data=="on"){
      //do something
      digitalWrite(led_indicator,HIGH);
    }
    else{
      //do something
      digitalWrite(led_indicator,LOW);
    }
      
  }




}
