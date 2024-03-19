// ANALOG OUTPUT

#define led 3

void setup(){
  pinMode(led, OUTPUT);
}

void loop(){
  // analogWrite(led, 125);
  for (int x=0; x<255; x++){
    analogWrite(led, x);
    delay(5);
  }
  for (int x=255; x>0; x--){
    analogWrite(led, x);
    delay(5);
  }
}