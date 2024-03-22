#define button_hazard 3
#define button_belt 2
#define led_indicator 4
#define pot_speed A0


bool now_state_hazard = false;
bool prev_state_hazard = false;
bool hazard=false;

bool now_state_belt = false;
bool prev_state_belt = false;
bool belt=false;

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);

  pinMode(led_indicator, OUTPUT);
  pinMode(button_hazard, INPUT_PULLUP); //pullup for bouncing
  pinMode(button_belt, INPUT_PULLUP);
  pinMode(pot_speed,INPUT);

}



void loop() {
    // Read potensio value
    int speed = analogRead(pot_speed);  //0-1023
    speed = map(speed,0,1023, 0,150);  //0-150

    //read button hazard
    now_state_hazard = !digitalRead(button_hazard);
    if(now_state_hazard==true){
        if (prev_state_hazard!=now_state_hazard){
        // prev_state=now_state;
        hazard = !hazard;

        
        }
    }
    prev_state_hazard = now_state_hazard;

    // read button belt
    now_state_belt = !digitalRead(button_belt);
    if(now_state_belt==true){
        if (prev_state_belt!=now_state_belt){
        // prev_state=now_state;
        belt = !belt;
        
        }
    }
    prev_state_belt = now_state_belt;


    // send data to python via serial communication
    // data yang akan di kirim: speed, rpm, belt, hazard
    String data_send ="";
    data_send +=String(speed);
    data_send +=",";
    data_send +=String(0);
    data_send +=",";
    data_send +=String(belt);
    data_send +=",";
    data_send +=String(hazard);
    
    Serial.println(data_send);


    // receive data from python via serial
    if (Serial.available()>1){
        String data = Serial.readString();
        if (data=="on"){
            // do something
            digitalWrite(led_indicator,HIGH);
        }

        else{
            // do something
            digitalWrite(led_indicator,LOW);
        }
    }

}
