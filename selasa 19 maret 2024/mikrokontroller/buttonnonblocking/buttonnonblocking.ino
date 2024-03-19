#define led 3
#define button 4
void setup(){
  pinMode(led,OUTPUT);
  pinMode(button, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop(){
  // Serial.println(!digitalRead(button));
  Serial.print(now_time);
  Serial.print(" ");
  Serial.println(prev_time);
  now_time = millis();
  if(now_time-prev_time>1000){
    prev_time = now_time;
    led_state = !led_state;
    digitalWrite(led, led_state);
  }

}
